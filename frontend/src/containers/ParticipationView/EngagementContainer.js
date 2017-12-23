// @flow
import React, { Component } from 'react'
import { AcceptedRequirements, LoggedRequirements } from 'components'
import { withLoadingAndError } from 'decorators'
import { getEngagement } from 'utils/api'
import type { Requirement, Student } from 'flow/types'

type Props = {
  student: Student,
  resetState: () => void
}

type State = {
  isLoading: boolean,
  isError: boolean,
  service: number,
  civilMil: string,
  requirements: Array<Requirement>,
}

class EngagementContainer extends Component<Props, State> {

  state = {
    isLoading: true,
    isError: false,
    service: 0,
    civilMil: 0,
    requirements: []
  }

  componentDidMount () {
    getEngagement(this.props.student.id)
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

  resetState = () => this.props.resetState() // Quirk with decorators and scope of this. Don't delete.

  @withLoadingAndError('There was an error. Please try again.')
  render () {
    const {service, civilMil, requirements} = this.state
    return [
      <AcceptedRequirements service={service} civilMil={civilMil} key={2} />,
      <LoggedRequirements requirements={requirements} key={3} />
    ]
  }
}

export default EngagementContainer
