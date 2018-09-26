// @flow
import React from "react";
import type { Name } from "types";
import s from "./Bio.module.css";

type Props = {
  pictureURL: string,
  position: string,
  name: Name,
  email: string
};

const Bio = ({ pictureURL, position, name, email }: Props) => (
  <div className={s.container}>
    <img
      src={pictureURL}
      className={s.image}
      alt={`Head shot of ${name.first} ${name.last}`}
    />
    <p>{position}</p>
    <p>
      {name.first} {name.last}
    </p>
    <p>{email}</p>
  </div>
);

export default Bio;
