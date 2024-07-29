import React from "react";
import { Alert } from "react-bootstrap";

const AlertDismissable = ({
  show,
  variant = "danger",
  onClose,
  title,
  message,
}) => {
  if (!show) return null;

  return (
    <Alert variant={variant} onClose={onClose} dismissible>
      {title && (
        <h5>
          <strong>{title}</strong>
        </h5>
      )}
      <div dangerouslySetInnerHTML={{ __html: message }} />
    </Alert>
  );
};

export default AlertDismissable;
