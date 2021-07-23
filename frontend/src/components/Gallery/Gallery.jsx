import React, { useEffect, useState } from "react";
import { getUserImages } from "../../calls/getUserImages";
import { Image } from "./Image";
import { GalleryOverlay } from "./GalleryOverlay/GalleryOverlay";

import "./Gallery.css";

export const Gallery = () => {
  const [isLoading, setIsLoading] = useState(true);
  const [fetchedImages, setFetchedImages] = useState([]);
  const [showOverlay, setShowOverlay] = useState(false);
  const [seleted, setSelected] = useState(null);

  const fetchImages = async () => {
    try {
      const images = await getUserImages();
      setFetchedImages(images);
    } catch (err) {
      console.log(err);
    }
    setIsLoading(false);
  };

  useEffect(() => {
    fetchImages();
  }, []);

  return isLoading ? (
    <div>Loading</div>
  ) : (
    <div className="gallery__main">
      {showOverlay && (
        <GalleryOverlay
          images={fetchedImages}
          setFetchedImages={setFetchedImages}
          selected={seleted}
          setSelected={setSelected}
          setShowOverlay={setShowOverlay}
        />
      )}
      {fetchedImages.map((image, index) => {
        return (
          <Image
            image={image}
            index={index}
            setSelected={setSelected}
            setShowOverlay={setShowOverlay}
            key={index}
          />
        );
      })}
    </div>
  );
};
