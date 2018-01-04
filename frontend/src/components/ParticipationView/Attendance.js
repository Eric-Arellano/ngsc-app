// @flow
import React from 'react'
import { Entry, PanelWithLoading } from 'components'

type Props = {
  noShows: number,
  missionTeamAttendance: string,
  committeeAttendance: string,
  olsAttendance: string,
  isLoading: boolean
}

const Attendance = ({noShows, missionTeamAttendance, committeeAttendance, olsAttendance, isLoading}: Props) => (
  <PanelWithLoading header='Attendance' isLoading={isLoading}>
    <Entry>On Leadership Seminars: {olsAttendance}</Entry>
    <Entry>Mission Team: {missionTeamAttendance}</Entry>
    {committeeAttendance && <Entry>Committee: {committeeAttendance}</Entry>}
    <Entry>No-shows: {noShows}</Entry>
    <br />
    <p><em>
      * No-shows indicates the number of times that you RSVPed for an event but did not show up without telling the
      event organizer in advance. If you need to dispute this number, please e-mail the Admin chair Diana at
      dkchen@asu.edu.
    </em></p>
  </PanelWithLoading>
)

export default Attendance
