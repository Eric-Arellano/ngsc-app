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
  missionTeam: ?number,
  committee: ?string,
  cohort: ?number,
  leadership: ?string,
  name: Name
}

class AppContainer extends Component<Props, State> {

  state = {
    isLoading: false,
    isValidated: false,
    isConfirmed: false,
    id: null,
    missionTeam: null,
    committee: null,
    cohort: null,
    leadership: null,
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
          missionTeam: data.missionTeam,
          committee: data.committee,
          cohort: data.cohort,
          leadership: data.leadership,
          id
        })
      })
      .catch(err => {
        this.setState({
          isLoading: false,
          isValidated: false,
          name: { first: '', last: '' },
          missionTeam: null,
          id: null,
          committee: null,
          cohort: null,
          leadership: null,
        })
      })
  }

  resetState = () => {
    this.setState({
      isLoading: false,
      isValidated: false,
      isConfirmed: false,
      userNotFound: false,
      id: null,
      missionTeam: null,
      committee: null,
      cohort: null,
      leadership: null,
      name: {
        first: '',
        last: ''
      }
    })

    window.location.reload()
  }

  confirmCorrectStudent = (isConfirmed: boolean) => {
    this.setState({
      isConfirmed,
      isValidated: isConfirmed,
    })
  }

  render () {
    return <App {...this.state} verifyStudentId={this.verifyStudentId} confirmCorrectStudent={this.confirmCorrectStudent} resetState={this.resetState}/>
  }
}

export default AppContainer
