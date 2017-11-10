// @flow
import React, { Component } from 'react';
import './App.css';

import Header from './../../components/Header/Header'
import StudentInfoContainer from '../StudentInfo/StudentInfoContainer';
import RequirementsContainer from '../Requirements/RequirementsContainer';

type Props = { }

type State = {
  isValidatedUser: boolean,
  id: number,
  firstName: string,
  lastName: string,
}

class App extends Component<Props, State> {

  // real code
  // state = {
  //   id: 0,
  //   firstName: '',
  //   lastName: '',
  // };

  // demo
  state = {
    isValidatedUser: false,
    id: 1208587250,
    firstName: "Eric",
    lastName: "Arellano",
  };

  updateValidatedUser = (value: boolean) => {
    this.setState({
      isValidatedUser: value
    })
  };

  updateID = (value: number) => {
    this.setState({
      id: value
    })
  };

  updateName = (firstName: string, lastName: string) => {
    this.setState({
      firstName: firstName,
      lastName: lastName
    })
  };

  render() {
    return (
      <div className="App">
        <Header />
        { !this.state.isValidatedUser && <StudentInfoContainer updateID={this.updateID} updateName={this.updateName} updateValidatedUser={this.updateValidatedUser} /> }
        { this.state.isValidatedUser && <RequirementsContainer id={this.state.id} firstName={this.state.firstName} lastName={this.state.lastName} /> }
      </div>
    );
  }
}

export default App;
