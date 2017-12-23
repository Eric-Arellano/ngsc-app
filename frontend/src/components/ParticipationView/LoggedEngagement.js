// @flow
import React from 'react'
import { Table } from 'react-bootstrap'
import type { EngagementEvent } from 'flow/types'
import { Panel } from 'components'

type Props = {
  engagementEvents: Array<EngagementEvent>
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

const LoggedEngagement = ({engagementEvents}: Props) => (
  <Panel header='Logged Engagement'>
    <Table striped bordered responsive>
      <thead>
      <tr>
        <th>Event name</th>
        <th>Engagement type</th>
        <th>Status</th>
        <th>Engagement hours</th>
      </tr>
      </thead>
      <tbody>
      {engagementEvents.map((event, index) => (
        <tr key={index}>
          <td>{event.name}</td>
          <td>{event.type}</td>
          <td>{translateStatus(event.status)}</td>
          <td>{translateHours(event.type, event.hours)}</td>
        </tr>
      ))}
      </tbody>
    </Table>
  </Panel>
)

export default LoggedEngagement
