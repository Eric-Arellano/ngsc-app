// @flow
import React from 'react'
import { Panel } from 'react-bootstrap'
import type { Student } from 'flow/types'
import Entry from './Entry'

type Props = {
  student: Student
}

const DemographicSummary = (props: Props) => {
  const {name, missionTeam, id, committee, cohort, leadership} = props.student
  return (
    <Panel header={'Student info'} bsStyle={'info'} className="ngsc">
      <Entry header={'Name'} value={`${name.first} ${name.last}`} />
      <Entry header={'ID number'} value={id} />
      <Entry header={'Cohort'} value={cohort} />
      <Entry header={'Mission team'} value={missionTeam} />
      {committee && <Entry header={'Committee'} value={committee} />}
      {leadership && <Entry header={'Leadership'} value={leadership} />}
    </Panel>
  )
}

export default DemographicSummary