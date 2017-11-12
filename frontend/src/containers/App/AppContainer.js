// @flow
import React, { Component } from 'react'
import { App } from 'components'
import { getUserInfo } from 'utils/api'
import type { Name } from 'flow/types'
import { mockStudent } from 'data/mock'

type Props = {}

type State = {
  isLoading: boolean,
  isValidated: boolean,
  isConfirmed: boolean,
  id: ?number,
  name: Name
}

class AppContainer extends Component<Props, State> {

  state = {
    isLoading: false,
    isValidated: false,
    isConfirmed: false,
    id: null,
    name: {
      first: '',
      last: ''
    }
  }

  verifyStudentId = (id: number) => {
    getUserInfo(id)
      .then(data => {
        this.setState({
          isLoading: false,
          isValidated: true,
          name: {
            first: data.firstName,
            last: data.lastName
          },
          id
        })
      })
      .catch(err => {
        const mock = mockStudent(id)
        this.setState({
          isLoading: false,
          isValidated: true,
          name: mock.name,
          id: mock.id
        }, this.confirmCorrectStudent)
      })
  }

  confirmCorrectStudent = (isConfirmed: boolean) => {
    this.setState({
      isConfirmed,
      isValidated: isConfirmed,
      isLoading: true
    })
  }

  render () {
    return <App {...this.state} verifyStudentId={this.verifyStudentId} confirmCorrectStudent={this.confirmCorrectStudent} />
  }
}

export default AppContainer
