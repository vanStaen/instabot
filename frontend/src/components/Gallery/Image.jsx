import React from "react";

export const Image = (props) => {
  const onClickHandler = () => {
    props.setSelected(props.index);
    props.setShowOverlay(true);
  };
  return (
    <div className="images__container">
      <img
        onClick={onClickHandler}
        id={props.image.id}
        src={props.image.file_s3}
        alt={props.image.id}
        key={props.index}
        width="100%"
      />
    </div>
  );
};
