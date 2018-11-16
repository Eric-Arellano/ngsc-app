// @flow
import React, { Component } from "react";
import CalculatorView from "./CalculatorView";

type Props = {};

type State = {
  estimatedAward: ?number,
  totalScholarship: ?number
};

class CalculatorViewContainer extends Component<Props, State> {
  state = {
    estimatedAward: undefined,
    totalScholarship: undefined
  };

  updateTotalScholarship = (value: string): void => {
    const num = Number(value); // parse to number; non-numeric answers will parse to NaN
    const isNumber = !isNaN(num);
    const updatedValue = isNumber ? num : undefined;
    this.setState({ totalScholarship: updatedValue });
  };

  submit = () => {
    this.setState({ estimatedAward: this.state.estimatedAward * 1.2 });
  };
  render() {
    return (
      <CalculatorView
        estimatedAward={this.state.estimatedAward}
        submit={this.submit}
        updateTotalScholarship={this.updateTotalScholarship}
      />
    );
  }
}

export default CalculatorViewContainer;
