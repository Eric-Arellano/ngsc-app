// @flow
import * as React from "react";
import { Button, Input } from "components";
type Props = {
  estimatedAward: number,
  updateTotalScholarship: string => void,
  submit: () => void
};
const CalculatorView = ({
  estimatedAward,
  submit,
  updateTotalScholarship
}: Props) => (
  <React.Fragment>
    <p>
      Fill out the following and click "Calculate Your Award" to find out what
      your NGSC Scholarship should be!
    </p>
    <Input
      label="Total Scholarships"
      placeholder="0"
      updateCurrentValue={updateTotalScholarship}
      inputType="number"
    />
    <Button handleClick={submit}>{"Calculate Your Award"}</Button>
    <p>Total Estimated Annual Award: {estimatedAward}</p>
  </React.Fragment>
);

export default CalculatorView;
