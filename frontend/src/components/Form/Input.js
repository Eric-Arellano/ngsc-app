import * as React from "react";
import type { ValidationState } from "types";
import { Label } from "components";
import s from "./Input.module.css";

type Props = {
  validationState: ValidationState,
  inputType?: string,
  placeholder?: string,
  label?: string,
  updateCurrentValue: string => void,
  handleEnterKey?: (SyntheticKeyboardEvent<HTMLInputElement>) => void
};

type State = {
  currentValue: string
};

class Input extends React.Component<Props, State> {
  static defaultProps = {
    validationState: "neutral",
    inputType: "text"
  };

  state = {
    currentValue: ""
  };

  handleKeyInput = (e: SyntheticInputEvent<HTMLInputElement>) => {
    const { updateCurrentValue } = this.props;
    const input = e.currentTarget.value;
    this.setState({ currentValue: input }, () => {
      const { currentValue } = this.state;
      updateCurrentValue(currentValue);
    });
  };

  render() {
    const {
      validationState,
      label,
      placeholder,
      handleEnterKey,
      inputType
    } = this.props;
    const { currentValue } = this.state;
    return (
      <div className={s.container}>
        {label !== undefined && <Label>{label}</Label>}
        <input
          type={inputType}
          value={currentValue}
          placeholder={placeholder}
          onKeyDown={handleEnterKey}
          onChange={this.handleKeyInput}
          className={s[validationState]}
        />
      </div>
    );
  }
}

export default Input;
