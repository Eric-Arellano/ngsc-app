// @flow
import React, { Component } from 'react';

import ConfirmationPopup from './../../components/ConfirmationPopup/ConfirmationPopup';

// TODO: Pull from the Master Spreadsheet the first and last name of student, then render below and ask them to confirm

// -----------------
// Actual code
// -----------------

type Props = {
  id: number,
  updateName: (string, string) => void,
}

type State = {
  firstName: string,
  lastName: string,
  isAccepted: boolean,
  isRejected: boolean,
}

class Confirmation extends Component<Props, State> {

  // real code
  // state = {
  //   firstName: '',
  //   lastName: '',
  //   isAccepted: false,
  //   isRejected: false
  // };

  // demo
  state = {
    firstName: 'Eric',
    lastName: 'Arellano',
    isAccepted: false,
    isRejected: false
  };

  updateAccepted = (b: boolean) => {
    this.props.updateName(this.state.firstName, this.state.lastName);
    this.setState({
      isAccepted: b
    })
  };

  updateRejected = (b: boolean) => {
    this.props.updateName('', '');
    this.setState({
      isRejected: b
    })
  };

  render() {
    return (
        <ConfirmationPopup firstName={this.state.firstName} lastName={this.state.lastName}
                           updateAccepted={this.updateAccepted} updateRejected={this.updateRejected}
        />
    )
  }

}

export default Confirmation;
