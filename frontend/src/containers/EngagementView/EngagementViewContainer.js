// @flow
import React, { Component } from 'react'
import { EngagementView } from 'components'
import { withLoadingAndError } from 'decorators'
import { getAttendance, getRequirements } from 'utils/api'
import type { Requirement, Student } from 'flow/types'

type Props = {
  student: Student,
  resetState: () => void
}

type State = {
  isLoading: boolean,
  isError: boolean,
  service: number,
  civilMil: number,
  noShows: number,
  mt_percent: string,
  com_percent: string,
  requirements: Array<Requirement>,
}

class EngagementViewContainer extends Component<Props, State> {

  state = {
    isLoading: true,
    isError: false,
    service: 0,
    civilMil: 0,
    noShows: 0,
    mt_percent: 0,
    com_percent: 0,
    requirements: []
  }

  setErrorState = () => {
      this.setState({
          service: 0,
          civilMil: 0,
          noShows: 0,
          mt_percent: 0,
          com_percent: 0,
          requirements: [],
          isLoading: false,
          isError: true,
      })
  }

  componentDidMount () {
    getRequirements(this.props.student.id)
      .then((data) => {
        this.setState({
          service: data.acceptedService,
          civilMil: data.acceptedCivilMil,
          requirements: data.requirements,
        })
      })
      .catch((error) => {
        this.setErrorState();
      })

    getAttendance(this.props.student.id)
          .then((data) => {
            this.setState({
              noShows: data.noShows,
              mt_percent: data.mt_percent,
              com_percent: data.com_percent,
              isLoading: false,
            })
          })
          .catch((error) => {
            this.setErrorState();
          })
  }

  resetState = () => this.props.resetState() // Quirk with decorators and scope of this. Don't delete.

  @withLoadingAndError('There was an error. Please try again.')
  render () {
    return <EngagementView {...this.props} {...this.state} />
  }
}

export default EngagementViewContainer
