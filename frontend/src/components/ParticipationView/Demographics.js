// @flow
import React from 'react'
import type { Student } from 'flow/types'
import { Entry, Panel } from 'components'

type Props = {
  student: Student
}

const Demographics = ({name, missionTeam, id, committee, cohort, leadership}: Props) => (
  <Panel header='Student info'>
    <Entry>Name: {name.first} {name.last}</Entry>
    <Entry>ID number: {id}</Entry>
    <Entry>Cohort: {cohort}</Entry>
    <Entry>Mission team: {missionTeam}</Entry>
    {committee && <Entry>Committee: {committee}</Entry>}
    {leadership && <Entry>Leadership: {leadership}</Entry>}
  </Panel>
)

export default Demographics