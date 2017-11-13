// @flow
import React, { Component } from 'react'
import { App } from 'components'
import { getUserInfo } from 'utils/api'
import type { Name } from 'flow/types'

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
    this.setState({
      isLoading: true
    })
    getUserInfo(id)
      .then(data => {
        this.setState({
          isLoading: false,
          isValidated: true,
          name: {
            first: data.name.first,
            last: data.name.last
          },
          id
        })
      })
      .catch(err => {
        this.setState({
          isLoading: false,
          isValidated: false,
          name: { first: '', last: '' },
          id: 0
        })
      })
  }

  confirmCorrectStudent = (isConfirmed: boolean) => {
    this.setState({
      isConfirmed,
      isValidated: isConfirmed,
    })
  }

  render () {
    return <App {...this.state} verifyStudentId={this.verifyStudentId} confirmCorrectStudent={this.confirmCorrectStudent} />
  }
}

export default AppContainer
