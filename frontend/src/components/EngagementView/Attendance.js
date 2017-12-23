// @flow
import React from 'react'
import { Entry, Panel } from 'components'

type Props = {
  noShows: number
}

const Attendance = ({noShows}: Props) => (
  <Panel header='Attendance'>
    <Entry>No-shows: {noShows}</Entry>
    <p><em>
      * No-shows indicate the number of times that you have RSVP'd that you will be attending an event but did
      not sign in on our records. If you need to dispute this number, please let e-mail the Admin chair.
    </em></p>
  </Panel>
)

export default Attendance