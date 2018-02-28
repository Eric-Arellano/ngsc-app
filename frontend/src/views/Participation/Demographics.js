// @flow
import React from 'react'
import type { Student } from 'types'
import { Entry, Panel } from 'components'

type Props = {
  student: Student
}

const Demographics = ({student: {name, missionTeam, committee, cohort, leadership}}: Props) => (
  <Panel header='Student info'>
    <Entry>Name: {name.first} {name.last}</Entry>
    <Entry>Cohort: {cohort}</Entry>
    <Entry>Mission team: {missionTeam}</Entry>
    {committee && <Entry>Committee: {committee}</Entry>}
    {leadership && <Entry>Leadership: {leadership}</Entry>}
  </Panel>
)

export default Demographics