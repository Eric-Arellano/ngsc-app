// @flow
import React from 'react'
import BigCalendar from 'react-big-calendar'
import moment from 'moment'
import 'react-big-calendar/lib/css/react-big-calendar.css'
import type { CalendarEvent } from 'types'
import s from './EventsView.module.css'

BigCalendar.momentLocalizer(moment)

type Props = {
  events: Array<CalendarEvent>,
}

const EventsView = ({events}: Props) => (
  <BigCalendar
    events={events}
    className={s.container}
    defaultView='agenda'
    views={['agenda', 'month', 'week']}
    defaultDate={new Date()}
  />
)

export default EventsView