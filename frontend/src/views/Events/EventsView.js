// @flow
import React from 'react'
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

const customAgendaEvent = (event: CalendarEvent) => (
  <span>
    <em>{event.title}</em>
    <p>{event.description}</p>
  </span>
)

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