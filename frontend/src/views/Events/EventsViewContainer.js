// @flow
import React, { Component } from 'react'
import EventsView from './EventsView'
import { withError } from 'decorators'
import { getEngagement } from 'api'
import type { CalendarEvent } from 'types'

type Props = {}

type State = {
  isLoading: boolean,
  isError: boolean,
  events: Array<CalendarEvent>,
}

class EventsViewContainer extends Component<Props, State> {

  state = {
    isLoading: true,
    isError: false,
    events: [],
  }

  // componentDidMount () {
  //   getEngagement(this.props.student.id)
  //     .then((data) => {
  //       this.setState({
  //         events: data.events,
  //         isLoading: false,
  //       })
  //     })
  //     .catch((error) => {
  //       this.setState({
  //         events: [],
  //         isLoading: false,
  //         isError: true,
  //       })
  //     })
  // }

  resetState = () => {
    this.setState({
      events: [],
      isLoading: false,
      isError: false,
    })
  } // Quirk with decorators and scope of this. Don't delete.

  @withError('There was an error. Please try again.')
  render () {
    return (<EventsView {...this.state} />)
  }
}

export default EventsViewContainer
