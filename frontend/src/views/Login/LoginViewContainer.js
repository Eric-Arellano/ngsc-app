// @flow
import React, { Component } from 'react'
import LoginView from './LoginView'
import { withLoadingAndError } from 'decorators'
import { getDemographics } from 'api'
import type { Student } from 'types'

type Props = {
  login: (Student) => void
}

type State = {
  isLoading: boolean,
  isError: boolean,
  isValidated: boolean,
  isConfirmed: boolean,
  student: ?Student
}

class LoginViewContainer extends Component<Props, State> {

  state = {
    isLoading: false,
    isError: false,
    isValidated: false,
    isConfirmed: false,
    student: null
  }

  verifyStudentId = (id: number) => {
    this.setState({
      isLoading: true
    })
    getDemographics(id)
      .then(data => {
        this.setState({
          isLoading: false,
          isValidated: true,
          student: {
            id,
            name: {
              first: data.name.first,
              last: data.name.last
            },
            missionTeam: data.missionTeam,
            committee: data.committee,
            cohort: data.cohort,
            leadership: data.leadership,
          }
        })
      })
      .catch(err => {
        this.setState({
          isLoading: false,
          isError: true,
        })
      })
  }

  resetState = () => {
    this.setState({
      isLoading: false,
      isError: false,
      isValidated: false,
      isConfirmed: false,
      student: null
    })
  }

  confirmCorrectStudent = (isConfirmed: boolean) => {
    this.setState({isConfirmed}, () => {
      if (isConfirmed) {
        this.props.login(this.state.student)
      }
    })
  }

  @withLoadingAndError('User not found. Please enter a valid student ID.')
  render () {
    return <LoginView {...this.state} verifyStudentId={this.verifyStudentId}
                      confirmCorrectStudent={this.confirmCorrectStudent} resetState={this.resetState} />
  }
}

export default LoginViewContainer
