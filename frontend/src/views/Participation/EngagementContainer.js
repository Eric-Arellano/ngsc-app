// @flow
import * as React from 'react'
import AcceptedEngagement from './AcceptedEngagement'
import LoggedEngagement from './LoggedEngagement'
import { withError } from 'decorators'
import { getEngagement } from 'api'
import type { EngagementEvent, Student } from 'types'

type Props = {
  student: Student,
  resetState: () => void
}

type State = {
  isLoading: boolean,
  isError: boolean,
  service: number,
  civilMil: number,
  engagementEvents: Array<EngagementEvent>,
}

class EngagementContainer extends React.Component<Props, State> {

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

  @withError('There was an error. Please try again.')
  render () {
    return (
      <React.Fragment>
        <AcceptedEngagement {...this.state} key={0} />
        <LoggedEngagement {...this.state} key={1} />
      </React.Fragment>
    )
  }
}

export default EngagementContainer
