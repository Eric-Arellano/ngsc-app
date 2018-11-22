import React from "react";
import { render } from "react-dom";
import { BrowserRouter } from "react-router-dom";
import { AppViewContainer } from "views";

const root = document.getElementById("root");
if (root == null) {
  throw new Error("Invalid index.html. <root> is not present.");
} else {
  render(
    <BrowserRouter>
      <AppViewContainer />
    </BrowserRouter>,
    root
  );
}
