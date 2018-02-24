// @flow
import React, {Component} from 'react'
import {AppView} from 'components'
import type {Student} from 'flow/types'

type Props = {}

type State = {
  isLoggedIn: boolean,
  student: ?Student
}

class AppContainer extends Component<Props, State> {

  state = {
    isLoggedIn: false,
    student: null
  };

  login = (student: Student) => {
    this.setState({
      student,
      isLoggedIn: true
    })
  };

  resetState = () => {
    this.setState({
      isLoggedIn: false,
      student: null
    })
  };

  render () {
      return <AppView {...this.state} login={this.login} resetState={this.resetState}/>
  }
}

export default AppContainer
