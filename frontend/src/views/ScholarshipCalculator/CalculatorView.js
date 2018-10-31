// @flow
import * as React from "react";
import { Button } from "components";
type Props = {
  estimatedAward: number,
  submit: () => void
};
const CalculatorView = ({ estimatedAward, submit }: Props) => (
  <React.Fragment>
    <p>
      Fill out the following and click "Calculate Your Award" to find out what
      your NGSC Scholarship should be!
    </p>
    <Button handleClick={submit}>{"Calculate Your Award"}</Button>
    <p>Total Estimated Annual Award: {estimatedAward}</p>
  </React.Fragment>
);

export default CalculatorView;
