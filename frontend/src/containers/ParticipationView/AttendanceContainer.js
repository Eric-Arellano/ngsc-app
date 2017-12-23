// @flow
import React, { Component } from 'react'
import { Attendance } from 'components'
import { withLoadingAndError } from 'decorators'
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
  mt_percent: string,
  com_percent: string
}

class AttendanceContainer extends Component<Props, State> {

  state = {
    isLoading: true,
    isError: false,
    noShows: 0,
    mt_percent: 0,
    com_percent: 0
  }

  componentDidMount () {
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
        this.setState({
          noShows: 0,
          mt_percent: 0,
          com_percent: 0,
          isLoading: false,
          isError: true,
        })
      })
  }

  resetState = () => this.props.resetState() // Quirk with decorators and scope of this. Don't delete.

  @withLoadingAndError('There was an error. Please try again.')
  render () {
    return <Attendance {...this.props} {...this.state} />
  }
}

export default AttendanceContainer
