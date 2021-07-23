import React, { useEffect, useCallback, useRef, useState } from "react";
import {
  LeftOutlined,
  RightOutlined,
  CloseOutlined,
  DeleteOutlined,
} from "@ant-design/icons";
import { Popconfirm } from "antd";

import { postSingleUserData } from "../../../calls/postSingleUserData";
import { deleteUserImage } from "../../../calls/deleteUserImage";
import "./GalleryOverlay.css";

export const GalleryOverlay = (props) => {
  const throttling = useRef(false);
  const [userData, setUserData] = useState();
  const [isLoading, setIsLoading] = useState(true);

  const fetchSingleUserData = async () => {
    try {
      const fetchedSingleUserData = await postSingleUserData(
        props.images[props.selected].author_id
      );
      setUserData(fetchedSingleUserData);
    } catch (err) {
      console.log(err);
    }
    setIsLoading(false);
  };

  useEffect(() => {
    fetchSingleUserData();
  }, [props.selected]);

  const incrementSelected = () => {
    props.setSelected(props.selected + 1);
    setIsLoading(true);
  };

  const decrementSelected = () => {
    if (props.selected > 0) {
      props.setSelected(props.selected - 1);
      setIsLoading(true);
    }
  };

  const mouseHoverHandler = (hover) => {
    const closeButton = document.getElementById(`closeButton`);
    if (hover) {
      closeButton.style.visibility = "hidden";
      closeButton.style.opacity = 0;
    } else {
      closeButton.style.visibility = "visible";
      closeButton.style.opacity = 1;
    }
  };

  const keyDownHandler = useCallback(
    (event) => {
      event.preventDefault();
      const keyPressed = event.key.toLowerCase();
      const nextButton = document.getElementById(`nextButton`);
      const previousButton = document.getElementById(`previousButton`);
      if (throttling.current === false) {
        throttling.current = true;
        if (keyPressed === "arrowdown" || keyPressed === "arrowright") {
          nextButton.style.backgroundColor = "rgba(255,255,255,.15)";
          incrementSelected();
          setTimeout(() => {
            nextButton.style.backgroundColor = "rgba(255,255,255, 0)";
          }, 100);
        } else if (keyPressed === "arrowup" || keyPressed === "arrowleft") {
          previousButton.style.backgroundColor = "rgba(255,255,255,.15)";
          decrementSelected();
          setTimeout(() => {
            previousButton.style.backgroundColor = "rgba(255,255,255, 0)";
          }, 100);
        } else if (keyPressed === "escape") {
          props.setShowOverlay(false);
        }
        setTimeout(() => {
          throttling.current = false;
        }, 100);
      }
    },
    [incrementSelected, decrementSelected, props.setShowOverlay]
  );

  useEffect(() => {
    document.addEventListener("keydown", keyDownHandler);
    return () => {
      document.removeEventListener("keydown", keyDownHandler);
    };
  }, [keyDownHandler]);

  return (
    <div className="overlay__overlay">
      <div
        className="overlay__background"
        onClick={() => {
          props.setShowOverlay(false);
        }}
      ></div>
      <div
        className="overlay__columnLeft"
        id="previousButton"
        onClick={decrementSelected}
      >
        <LeftOutlined />
      </div>
      <div
        className="overlay__columnRight"
        id="nextButton"
        onMouseEnter={() => mouseHoverHandler(true)}
        onMouseLeave={() => mouseHoverHandler(false)}
        onClick={incrementSelected}
      >
        <RightOutlined />
      </div>
      <div
        className="overlay__closeButton"
        id="closeButton"
        onClick={() => {
          props.setShowOverlay(false);
        }}
      >
        <CloseOutlined />
      </div>
      <div className="overlay__pictureContainer">
        <img
          className="overlay__picture"
          src={props.images[props.selected].file_s3}
          alt={props.images[props.selected].file_path}
        />
        {!isLoading &&
          (userData && userData.username != undefined ? (
            <div className="overlay__tags">
              <span>{userData.username}</span>
            </div>
          ) : userData && userData.first_name != undefined ? (
            <div className="overlay__tags">
              <span>{userData.first_name}</span>
            </div>
          ) : userData && userData.telegram_id != undefined ? (
            <div className="overlay__tags">
              <span>id #{userData.telegram_id}</span>
            </div>
          ) : (
            <div className="overlay__tags error">
              <span>USER NOT FOUND</span>
            </div>
          ))}
        <div className="overlay__action">
          <div className="overlay__delete">
            <Popconfirm
              placement="topRight"
              title={"Are you sure? This can't be undone."}
              onConfirm={() => {
                deleteUserImage(props.images[props.selected].file_path);
                const ArrayImagesNew = props.images;
                ArrayImagesNew.splice(props.selected, 1);
                props.setShowOverlay(false);
                props.setFetchedImages(ArrayImagesNew);
              }}
              okText="Delete"
              cancelText="Cancel"
            >
              <DeleteOutlined />
            </Popconfirm>
          </div>
        </div>
      </div>
    </div>
  );
};
