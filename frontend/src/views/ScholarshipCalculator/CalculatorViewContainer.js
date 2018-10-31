// @flow
import React, { Component } from "react";
import CalculatorView from "./CalculatorView";

type Props = {};

type State = {
  estimatedAward: number
};

class CalculatorViewContainer extends Component<Props, State> {
  state = {
    estimatedAward: 10
  };

  submit = () => {
    this.setState({ estimatedAward: this.state.estimatedAward * 1.2 });
  };
  render() {
    return (
      <CalculatorView
        estimatedAward={this.state.estimatedAward}
        submit={this.submit}
      />
    );
  }
}

export default CalculatorViewContainer;
