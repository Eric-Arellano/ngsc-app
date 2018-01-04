// @flow
import React, { Component } from 'react'
import { Attendance } from 'components'
import { withError } from 'decorators'
import { getAttendance } from 'utils/api'
import type { Student } from 'flow/types'

type Props = {
  student: Student,
  resetState: () => void
}

type State = {
  isLoading: boolean,
  isError: boolean,
  noShows: number,
  missionTeamAttendance: string,
  committeeAttendance: string,
  olsAttendance: string
}

class AttendanceContainer extends Component<Props, State> {

  state = {
    isLoading: true,
    isError: false,
    noShows: 0,
    missionTeamAttendance: '',
    committeeAttendance: '',
    olsAttendance: ''
  }

  componentDidMount () {
    getAttendance(this.props.student.id)
      .then((data) => {
        this.setState({
          noShows: data.noShows,
          missionTeamAttendance: data.missionTeamAttendance,
          committeeAttendance: data.committeeAttendance,
          olsAttendance: data.olsAttendance,
          isLoading: false,
        })
      })
      .catch((error) => {
        this.setState({
          noShows: 0,
          missionTeamAttendance: '',
          committeeAttendance: '',
          olsAttendance: '',
          isLoading: false,
          isError: true,
        })
      })
  }

  resetState = () => this.props.resetState() // Quirk with decorators and scope of this. Don't delete.

  @withError('There was an error. Please try again.')
  render () {
    return <Attendance {...this.props} {...this.state} />
  }
}

export default AttendanceContainer
