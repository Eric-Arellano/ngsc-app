// @flow
import React, { Component } from 'react';

import IDInput from './../../components/IDInput/IDInput';
import ConfirmationPopup from './../../components/ConfirmationPopup/ConfirmationPopup';
import { getUserInfo } from './../../api'

type Props = {
  updateName: (string, string) => void,
  updateID: (number) => void,
  updateValidatedUser: (boolean) => void
}

type State = {
  id: number,
  firstName: string,
  lastName: string,
  isUserFound: boolean,  // TODO: probably need more booleans, e.g. isLoading
  isUserAccepted: boolean,
  isUserRejected: boolean,
}

class StudentInfoContainer extends Component<Props, State> {

  state = {
    id: 1208487250,
    firstName: 'Eric',
    lastName: 'Arellano',
    isUserFound: false,
    isUserAccepted: false,
    isUserRejected: false
  };

  componentDidUpdate(prevProps: Props, prevState: State) {
    if (this.state.id !== 0 && prevState.id !== this.state.id) {
      getUserInfo(this.state.id)
        .then((data) => {
          this.setState({
            firstName: data.firstName,
            lastName: data.lastName,
            isUserFound: true
          })
        })
        .catch((error) => {
          this.setState({

          })
        })
    }
  };

  updateID = (value: number) => {
    this.setState({
      id: value
    })
  };

  updateAccepted = (b: boolean) => {
    this.setState({
      isUserAccepted: b
    });
    this.props.updateName(this.state.firstName, this.state.lastName);
    this.props.updateID(this.state.id);
    this.props.updateValidatedUser(true);
  };

  updateRejected = (b: boolean) => {  // TODO: nothing happens when rejected. Add logic to re-request ID
    this.setState({
      isUserRejected: b
    });
    this.props.updateName('', '');
    this.props.updateID(0);

  };

  render() {
    return (
      <div>
        <IDInput onSubmit={this.updateID} />
        { this.state.isUserFound && <ConfirmationPopup firstName={this.state.firstName} lastName={this.state.lastName}
                           updateAccepted={this.updateAccepted} updateRejected={this.updateRejected}
        /> }
      </div>
    )
  }

}

export default StudentInfoContainer;
