// @flow
import React, { Component } from 'react';
import './App.css';

import Header from './../../components/Header/Header'
import IDInput from './../../components/IDInput/IDInput';
import Confirmation from './../Confirmation/Confirmation';
import Summary from './../Summary/Summary';

type Props = { }

type State = {
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
    id: 1208587250,
    firstName: "Eric",
    lastName: "Arellano",
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
        <IDInput onSubmit={this.updateID} />
        <Confirmation id={this.state.id} updateName={this.updateName} />
        <Summary id={this.state.id} firstName={this.state.firstName} lastName={this.state.lastName} />
      </div>
    );
  }
}

export default App;
