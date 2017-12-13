// @flow
import React from 'react'
import { Panel } from 'react-bootstrap'
import type { Student } from 'flow/types'
import { Entry } from 'components'

type Props = {
  student: Student
}

const DemographicSummary = (props: Props) => {
  const {name, missionTeam, id, committee, cohort, leadership} = props.student
  return (
    <Panel header={'Student info'} bsStyle={'info'} className="ngsc">
      <Entry>Name: {name.first} {name.last}</Entry>
      <Entry>ID number: {id}</Entry>
      <Entry>Cohort: {cohort}</Entry>
      <Entry>Mission team: {missionTeam}</Entry>
      {committee && <Entry>Committee: {committee}</Entry>}
      {leadership && <Entry>Leadership: {leadership}</Entry>}
    </Panel>
  )
}

export default DemographicSummary