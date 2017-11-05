// @flow
import React, { Component } from 'react';
import { Form, FormGroup, FormControl, ControlLabel, HelpBlock, Button } from 'react-bootstrap';

type Props = { }

type State = {
  idValue: string
};

class IDInput extends Component<Props, State> {

  state = {
    idValue: ''
  };

  getValidationState() {
    const num = +this.state.idValue;  // parse to number; non-numeric answers will parse to NaN
    const isNumber = !isNaN(num);
    const length = num.toString().length;
    if (length === 10 && isNumber) return 'success';
    else if (length <= 1) return null;
    else if (length !== 10) return 'error';
    return null;
  }

  handleIDInput = (e: SyntheticInputEvent<HTMLInputElement>) => {
      this.setState({
          idValue: e.currentTarget.value
        });
  };

  render() {
    return (
      <Form inline>
        <FormGroup
          controlId={"ID"}
          validationState={this.getValidationState()}
        >
          <ControlLabel>Student ID:</ControlLabel>
          {' '}
          <FormControl
            type={"text"}
            value={this.state.idValue}
            onChange={this.handleIDInput}
          />
          <FormControl.Feedback />
          <HelpBlock>Please enter a valid student ID.</HelpBlock>
        </FormGroup>
        <Button type="submit">Submit</Button>
      </Form>
    )
  }
}

export default IDInput;