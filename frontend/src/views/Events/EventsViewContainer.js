// @flow
import React, { Component } from 'react'
import moment from 'moment'
import { getRequest } from 'api'
import EventsView from './EventsView'
import { withError } from 'decorators'
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

  componentDidMount () {
    this.getEvents()
      .then(data => this.setState({
        isLoading: false,
        events: this.parseEvents(data.items)
      }))
      .catch(error => this.setState({
        isError: true,
        isLoading: false,
        events: [],
      }))
  }

  getEvents = (): Promise<any> => {
    const calendar_id = 'nldr7mmpe52c337cdf0kdj5va4@group.calendar.google.com'
    const api_key = 'AIzaSyCrUF2cdnFowx-MKlEnMNFUweOXlnU4Vc8'
    const url = `https://www.googleapis.com/calendar/v3/calendars/${calendar_id}/events?key=${api_key}`
    return getRequest(url)
  }

  parseEvents = (googleEvents: Array<any>): Array<CalendarEvent> => (
    googleEvents.map((event) => (
      {
        start: moment(event.start.date || event.start.dateTime).toDate(),
        end: moment(event.start.date || event.end.dateTime).toDate(),
        title: event.summary,
        description: event.description || '',
        location: event.location || '',
      }))
  )

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
