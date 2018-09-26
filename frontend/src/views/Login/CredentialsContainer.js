// @flow
import React, { Component } from "react";
import Credentials from "./Credentials";
import type { ValidationState } from "types";

type Props = {
  onSubmit: string => void
};

type State = {
  currentValue: string,
  validationState: ValidationState
};

class CredentialsContainer extends Component<Props, State> {
  state = {
    currentValue: "",
    validationState: "neutral"
  };

  // TODO: add debounce to validation, using Lodash's debounce function.
  // componentDidMount() {
  //   this.determineValidationState = debounce(this.determineValidationState, 400)
  // }

  determineValidationState = (input: string) => {
    if (!input) {
      return "neutral";
    } else {
      return this.checkIsValidAsurite(input) ? "valid" : "invalid";
    }
  };

  checkIsValidAsurite = (input: string): boolean => {
    const regex = /^[a-z][a-z0-9]*/;
    return regex.test(input);
  };

  updateCurrentValue = (currentValue: string) => {
    const validationState = this.determineValidationState(currentValue);
    this.setState({
      currentValue,
      validationState
    });
  };

  handleEnterKey = (e: SyntheticInputEvent<HTMLInputElement>) => {
    if (e.key === "Enter") {
      this.handleSubmit();
    }
  };

  handleSubmit = () => {
    const { onSubmit } = this.props;
    const { currentValue, validationState } = this.state;
    if (validationState === "valid") {
      onSubmit(currentValue);
    }
  };

  render() {
    return (
      <Credentials
        {...this.state}
        handleSubmit={this.handleSubmit}
        handleEnterKey={this.handleEnterKey}
        updateCurrentValue={this.updateCurrentValue}
      />
    );
  }
}

export default CredentialsContainer;
