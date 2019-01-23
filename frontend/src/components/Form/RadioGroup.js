import * as React from "react";
import { Label } from "components";
import type { RadioOption } from "types";
import s from "./RadioGroup.module.css";

type Props = {
  options: Array<RadioOption>,
  default?: RadioOption,
  label?: string,
  updateCurrentSelection: RadioOption => void
};

type State = {
  currentSelection: ?RadioOption
};

class RadioGroup extends React.Component<Props, State> {
  state = {
    currentSelection: this.props.default
  };

  handleSelection = (e: SyntheticInputEvent<HTMLInputElement>) => {
    const { options, updateCurrentSelection } = this.props;
    const input = e.currentTarget.value;
    const newSelection: RadioOption = options.find(
      option => option.label === input
    );
    this.setState({ currentSelection: newSelection }, () => {
      updateCurrentSelection(newSelection);
    });
  };

  render() {
    const { currentSelection } = this.state;
    const { options, label } = this.props;
    return (
      <div className={s.container}>
        {label !== undefined && <p className={s.label}>{label}</p>}
        <ul>
          {options.map((option: RadioOption, index: number) => (
            <li key={index}>
              <Label>
                <input
                  type="radio"
                  value={option.label}
                  checked={currentSelection === option}
                  onChange={this.handleSelection}
                  className={s.radio}
                />
                {option.label}
              </Label>
            </li>
          ))}
        </ul>
      </div>
    );
  }
}

export default RadioGroup;
