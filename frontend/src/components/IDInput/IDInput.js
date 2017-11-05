import React, { Component } from 'react';
import { Form, FormGroup, FormControl, ControlLabel, HelpBlock, Button } from 'react-bootstrap';

class IDInput extends Component {

  constructor(props) {
    super(props);
    this.state = {
      value: ''
    };
    this.handleChange = this.handleChange.bind(this);
  }

  getValidationState() {
    const length = this.state.value.length;
    if (length === 10) return 'success';
    else if (length !== 10) return 'error';
  }

  handleChange(e) {
    this.setState( {
      value: e.target.value
      }
    );
  }


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
            value={this.state.value}
            onChange={this.handleChange}
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