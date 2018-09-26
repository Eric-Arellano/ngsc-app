// @flow
import React from "react";
import s from "./Footer.module.css";
import { Social } from "components";

const Footer = () => (
  <footer className={s.container}>
    <Social />
  </footer>
);

export default Footer;
