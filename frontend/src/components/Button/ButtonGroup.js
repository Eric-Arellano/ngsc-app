// @flow
import * as React from "react";
import Button from "./Button";
import s from "./Button.module.css";

type Props = {
  children: React.ChildrenArray<React.Element<typeof Button>>
};

const ButtonGroup = ({ children }: Props) => (
  <div className={s.group}>{children}</div>
);

export default ButtonGroup;
