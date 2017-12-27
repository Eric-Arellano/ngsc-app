// @flow
import React, { Component } from 'react'
import { AcceptedEngagement, LoggedEngagement } from 'components'
import { withLoadingAndError } from 'decorators'
import { getEngagement } from 'utils/api'
import type { EngagementEvent, Student } from 'flow/types'

type Props = {
  student: Student,
  resetState: () => void
}

type State = {
  isLoading: boolean,
  isError: boolean,
  service: number,
  civilMil: string,
  engagementEvents: Array<EngagementEvent>,
}

class EngagementContainer extends Component<Props, State> {

  state = {
    isLoading: true,
    isError: false,
    service: 0,
    civilMil: 0,
    engagementEvents: []
  }

  componentDidMount () {
    getEngagement(this.props.student.id)
      .then((data) => {
        this.setState({
          service: data.acceptedService,
          civilMil: data.acceptedCivilMil,
          engagementEvents: data.loggedEvents,
          isLoading: false,
        })
      })
      .catch((error) => {
        this.setState({
          service: 0,
          civilMil: 0,
          engagementEvents: [],
          isLoading: false,
          isError: true,
        })
      })
  }

  resetState = () => this.props.resetState() // Quirk with decorators and scope of this. Don't delete.

  @withLoadingAndError('There was an error. Please try again.')
  render () {
    const {service, civilMil, engagementEvents} = this.state
    return [
      <AcceptedEngagement service={service} civilMil={civilMil} key={0} />,
      <LoggedEngagement engagementEvents={engagementEvents} key={1} />
    ]
  }
}

export default EngagementContainer
