// @flow
import React from 'react'
import { Entry, Panel } from 'components'

type Props = {
  noShows: number,
  missionTeamAttendance: string,
  committeeAttendance: string,
  olsAttendance: string
}

const Attendance = ({noShows, missionTeamAttendance, committeeAttendance, olsAttendance}: Props) => (
  <Panel header='Attendance'>
    <Entry>On Leadership Seminar: {olsAttendance}</Entry>
    <Entry>Mission Team: {missionTeamAttendance}</Entry>
    {committeeAttendance && <Entry>Committee: {committeeAttendance}</Entry>}
    <Entry>No-shows: {noShows}</Entry>
    <p><em>
      * No-shows indicate the number of times that you have RSVP'd that you will be attending an event but did
      not sign in on our records. If you need to dispute this number, please let e-mail the Admin chair.
    </em></p>
  </Panel>
)

export default Attendance
