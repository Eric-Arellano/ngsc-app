// @flow
import React, {Component} from 'react'
import axios from 'axios'
import EventsView from './EventsView'
import {withError} from 'decorators'
import {getEngagement} from 'api'
import type {CalendarEvent} from 'types'

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

  componentDidMount() {
    const events = this.getEvents()
    if (!events.length) {
      this.setState({
        isError: true,
        isLoading: false,
        events: [],
      })
    } else {
      this.setState({
        isLoading: false,
        events: events,
      })
    }
  }

  getEvents = (): Array<CalendarEvent> => {
    const calendar_id = 'nldr7mmpe52c337cdf0kdj5va4@group.calendar.google.com'
    const api_key = 'AIzaSyCrUF2cdnFowx-MKlEnMNFUweOXlnU4Vc8'
    const url = `https://www.googleapis.com/calendar/v3/calendars/${calendar_id}/events?key=${api_key}`
    let events = []
    axios
      .get(url)
      .then(info => {
        events = (info.data.items).map((event) => (
            {
              start: event.start.date || event.start.dateTime,
              end: event.start.date || event.end.dateTime,
              title: event.summary,
            }
          )
        )
      })
      .catch(error => { console.log(error)
      })
    return events
  }


  resetState = () => {
    this.setState({
      events: [],
      isLoading: false,
      isError: false,
    })
  } // Quirk with decorators and scope of this. Don't delete.

  @withError('There was an error. Please try again.')
  render() {
    return (<EventsView {...this.state} />)
  }
}

export default EventsViewContainer
