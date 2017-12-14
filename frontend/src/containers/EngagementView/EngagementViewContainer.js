// @flow
import React, { Component } from 'react'
import { EngagementView } from 'components'
import { getRequirements } from 'utils/api'
import type { Requirement, Student } from 'flow/types'

type Props = {
  student: Student
}

type State = {
  isLoading: boolean,
  isError: boolean,
  service: number,
  civilMil: number,
  requirements: Array<Requirement>,
}

class EngagementViewContainer extends Component<Props, State> {

  state = {
    isLoading: true,
    isError: false,
    service: 0,
    civilMil: 0,
    requirements: []
  }

  componentDidMount () {
    getRequirements(this.props.student.id)
      .then((data) => {
        this.setState({
          service: data.acceptedService,
          civilMil: data.acceptedCivilMil,
          requirements: data.requirements,
          isLoading: false,
        })
      })
      .catch((error) => {
        this.setState({
          service: 0,
          civilMil: 0,
          requirements: [],
          isLoading: false,
          isError: true,
        })
      })
  }

  render () {
    return <EngagementView {...this.props} {...this.state} />
  }
}

export default EngagementViewContainer
