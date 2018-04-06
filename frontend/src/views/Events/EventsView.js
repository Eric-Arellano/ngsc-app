// @flow
import * as React from 'react'
import BigCalendar from 'react-big-calendar'
import moment from 'moment'
import 'react-big-calendar/lib/css/react-big-calendar.css'
import type { CalendarEvent } from 'types'
import './EventsView.css'
import s from './EventsView.module.css'

BigCalendar.momentLocalizer(moment)

type Props = {
  events: Array<CalendarEvent>,
}

const customAgendaEvent = ({event}) => (
  <span key={event.title}>
    <em>{event.title}</em>
    {event.location && <p>{event.location}</p>}
    {event.description && <React.Fragment>{event.description}</React.Fragment>}
  </span>
)

// TODO: get this code working to convert links to <a> elements
// const linkify = (text: string) => {
//   const regex = /(\b(https?|ftp|file):\/\/[-A-Z0-9+&@#\/%?=~_|!:,.;]*[-A-Z0-9+&@#\/%=~_|])/ig
//   return text.split(regex).map((part, index) => index % 2 === 0 ? part : <a href={part}>{part}</a>)
// }

const today = (): Date => {
  const today = new Date()
  return new Date(today.getUTCFullYear(), today.getUTCMonth(), today.getUTCDay())
}

const EventsView = ({events}: Props) => (
  <BigCalendar
    events={events}
    className={s.container}
    defaultView='agenda'
    views={['agenda', 'month', 'week']}
    defaultDate={today()}
    components={{
      agenda: {
        event: customAgendaEvent
      }
    }}
  />
)

export default EventsView