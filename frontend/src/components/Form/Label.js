import * as React from "react";
import s from "./Label.module.css";

type Props = {
  children: React.ChildrenArray<string | React.Element<"input">>
};

const Label = ({ children }: Props) => (
  <label className={s.container}>{children}</label>
);

export default Label;
