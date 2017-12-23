// @flow
import React, { Component } from 'react'
import { LoginView } from 'components'
import { withError, withLoading } from 'HOCs'
import { getDemographics } from 'utils/api'
import type { Student } from 'flow/types'

type Props = {
  login: (Student) => void,
  resetState: () => void
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
    this.setState({
      isConfirmed,
      isValidated: isConfirmed,
    })
    this.props.login(this.state.student)
  }

  render () {
    const LoginViewWithLoading = withLoading(LoginView)
    const LoginViewWithErrorAndLoading = withError(LoginViewWithLoading, this.resetState, 'User not found. Please enter a valid student ID.')
    return <LoginViewWithErrorAndLoading {...this.state} verifyStudentId={this.verifyStudentId}
                                         confirmCorrectStudent={this.confirmCorrectStudent} />
  }
}

export default LoginViewContainer
