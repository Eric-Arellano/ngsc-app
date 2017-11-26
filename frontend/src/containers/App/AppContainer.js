// @flow
import React, { Component } from 'react'
import { App } from 'components'
import { getDemographics } from 'utils/api'
import type { Name } from 'flow/types'

type Props = {}

type State = {
  isLoading: boolean,
  isError: boolean,
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
    isError: false,
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
    getDemographics(id)
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
  }

  confirmCorrectStudent = (isConfirmed: boolean) => {
    this.setState({
      isConfirmed,
      isValidated: isConfirmed,
    })
  }

  render () {
    return <App {...this.state} verifyStudentId={this.verifyStudentId}
                confirmCorrectStudent={this.confirmCorrectStudent} resetState={this.resetState} />
  }
}

export default AppContainer
