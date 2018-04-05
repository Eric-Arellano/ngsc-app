// @flow
import React from 'react'
import BigCalendar from 'react-big-calendar'
import moment from 'moment'
import 'react-big-calendar/lib/css/react-big-calendar.css'
import type { CalendarEvent } from 'types'

BigCalendar.momentLocalizer(moment)

const fakeEvents = [
  {
    id: 0,
    title: 'NGSC Event',
    start: new Date(2018, 2, 1, 9, 0, 0),
    end: new Date(2018, 2, 1, 10, 0, 0),
  },
  {
    id: 1,
    title: 'NGSC Event 1',
    start: new Date(2018, 3, 2),
    end: new Date(2018, 3, 2),
  }, {
    id: 2,
    title: 'NGSC Event 2',
    start: new Date(2018, 3, 3),
    end: new Date(2018, 3, 3),
  },
]

type Props = {
  events: Array<CalendarEvent>,
}

const EventsView = ({events}: Props) => (
  <BigCalendar
    events={events}
    startAcessor={'startDate'}
    endAccessor={'endDate'}
  />
)

export default EventsView