import * as React from "react";
import Bio from "./Bio";
import s from "./BioGroup.module.css";

type Props = {
  header: string,
  children: React.ChildrenArray<React.Element<typeof Bio>>
};

const BioGroup = ({ header, children }: Props) => (
  <div>
    <h3 className={s.header}>{header}</h3>
    <div className={s.children}>{children}</div>
  </div>
);

export default BioGroup;
