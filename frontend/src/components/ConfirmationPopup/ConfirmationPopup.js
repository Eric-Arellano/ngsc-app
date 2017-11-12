// @flow
import React, { Component } from 'react';
import { ButtonToolbar, Button } from 'react-bootstrap';

type Props = {
  firstName: string,
  lastName: string,
  updateAccepted: (boolean) => void;
  updateRejected: (boolean) => void;
}

class ConfirmationPopup extends Component<Props> {

  handleYesClick = () => {
    this.props.updateAccepted(true);
  };

  handleNoClick = () => {
    this.props.updateRejected(true);
  };

  render() {
    return (
      <div>
        <p>Are you {this.props.firstName} {this.props.lastName}?</p>
        <ButtonToolbar>
          <Button bsStyle={"success"} onClick={() => this.props.confirmCorrectStudent(true)}>Yes</Button>
          <Button bsStyle={"danger"} onClick={() => this.props.confirmCorrectStudent(false)}>No, wrong person!</Button>
        </ButtonToolbar>
      </div>
    )
  }
}

export default ConfirmationPopup;