// @flow
import React from 'react'
import type {Student} from 'types'
import {Entry, Panel} from 'components'

type Props = {
  student: Student
}

const Demographics = ({student: {name, missionTeam, committee, cohort, leadership, email, phone, campus}}: Props) => (
  <Panel header='Student info'>
    <Entry>Name: {name.first} {name.last}</Entry>
    <Entry>Cohort: {cohort}</Entry>
    {missionTeam && <Entry>Mission team: {missionTeam}</Entry>}
    {committee && <Entry>Committee: {committee}</Entry>}
    {leadership && <Entry>Leadership: {leadership}</Entry>}
    <Entry>Email: {email}</Entry>
    <Entry>Phone: {phone}</Entry>
    <Entry>Campus: {campus}</Entry>
    <br/>
    <p><em>
      * If any of this information is incorrect, please email the Admin chair Jeremy at
      jseidne@asu.edu.
    </em></p>
  </Panel>
)

export default Demographics