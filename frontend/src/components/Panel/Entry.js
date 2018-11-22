import * as React from "react";

type Props = {
  children: React.ChildrenArray<string | number | React.Element<"a">>
};

const Entry = ({ children }: Props) => <p>{children}</p>;

export default Entry;
