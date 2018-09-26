// @flow
import React from "react";
import NavButton from "./NavButton";
import s from "./Nav.module.css";

const Nav = () => (
  <nav>
    <ul className={s.container}>
      <NavButton link="./" label="Participation" />
      <NavButton link="./events" label="Events" />
      <NavButton link="./leadership" label="Leadership" />
    </ul>
  </nav>
);

export default Nav;
