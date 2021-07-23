import React, { useState, useCallback, useEffect } from "react";
import { Input, notification, Button } from "antd";
import { ArrowRightOutlined } from "@ant-design/icons";

import "./Login.css";

export const Login = (props) => {
  const [codeFromInput, setCodeFromInput] = useState(undefined);

  const handlerInputChange = (e) => {
    setCodeFromInput(e.target.value);
  };

  const handlerButtonClick = () => {
    if (codeFromInput === process.env.REACT_APP_ACCESS_PWD) {
      props.setHasAccess(true);
    } else {
      setCodeFromInput(null);
      document.getElementById("password").value = null;
      notification.error({ message: "Wrong password" });
    }
  };

  const keyDownListener = useCallback(
    (event) => {
      const keyPressed = event.key.toLowerCase();
      if (keyPressed === "enter") {
        handlerButtonClick();
      }
    },
    [props, codeFromInput]
  );

  useEffect(() => {
    document.addEventListener("keydown", keyDownListener);
    return () => {
      document.removeEventListener("keydown", keyDownListener);
    };
  }, [keyDownListener]);

  return (
    <div className="containerLogin">
      <span className="Title">Golden Circle</span>
      <div>
        <div className="containerInput">
          <Input.Password
            id="password"
            onChange={handlerInputChange}
            placeholder="confirm with enter"
            className="passwordInput"
          />
        </div>
        <Button
          className="passwordButton"
          shape="circle"
          icon={<ArrowRightOutlined />}
          onClick={handlerButtonClick}
        />
        <br />
        <br />
        <br />
      </div>
    </div>
  );
};
