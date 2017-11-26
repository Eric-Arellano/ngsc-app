// @flow
import React from 'react'
import { Panel, Table } from 'react-bootstrap'
import type { Requirement } from 'flow/types'

type Props = {
  requirements: Array<Requirement>
}

const translateHours = (reqType: string, hours: number) => {
  if (reqType === 'Service') return `${hours} hour${hours > 1 ? 's' : ''}`
  else if (reqType === 'Civil-Mil OR Service') return `${hours} hour${hours > 1 ? 's' : ''} or 1 civil-mil event`
  else if (reqType === 'Civil-Mil') return `1 civil-mil event`
  return ''
}

const translateStatus = (status: string) => {
  if (status === '') return 'Not yet evaluated'
  return status
}

const SubmittedRequirementsTable = (props: Props) => (
  <Panel header={'Logged Requirements'} bsStyle={'info'} className="ngsc">
    <Table striped bordered responsive>
      <thead>
      <tr>
        <th>Event name</th>
        <th>Requirement type</th>
        <th>Status</th>
        <th>Requested hours</th>
      </tr>
      </thead>
      <tbody>
      {props.requirements.map((requirement, index) => (
        <tr key={index}>
          <td>{requirement.name}</td>
          <td>{requirement.reqType}</td>
          <td>{translateStatus(requirement.status)}</td>
          <td>{translateHours(requirement.reqType, requirement.hours)}</td>
        </tr>
      ))}
      </tbody>
    </Table>
  </Panel>
)

export default SubmittedRequirementsTable
