// @flow
import React from 'react'
import ReactTable from 'react-table' // see https://react-table.js.org/#/story/readme
import type { EngagementEvent } from 'flow/types'
import { PanelWithLoading } from 'components'
import 'react-table/react-table.css'

type Props = {
  engagementEvents: Array<EngagementEvent>,
  isLoading: boolean
}

const translateHours = (reqType: string, hours: number) => {
  if (reqType === 'Service') return `${hours} hour${hours > 1 ? 's' : ''}`
  else if (reqType === 'Civil-Mil OR Service') return `${hours} hour${hours > 1 ? 's' : ''} or 1 civil-mil event`
  else if (reqType === 'Civil-Mil') return `1 civil-mil event`
  return ''
}

const translateStatus = (status: string) => {
  if (status === '') return 'Not yet evaluated'
  if (status === 'Late') return 'Late (accepted)'
  return status
}

const LoggedEngagement = ({engagementEvents, isLoading}: Props) => {

  const columns = [{
    id: 'Name',
    Header: 'Event name',
    accessor: event => event.name
  }, {
    id: 'Type',
    Header: 'Engagement type',
    accessor: event => event.type
  }, {
    id: 'Status',
    Header: 'Status',
    accessor: event => translateStatus(event.status)
  }, {
    id: 'Hours',
    Header: 'Engagement hours',
    accessor: event => translateHours(event.type, event.hours)
  }]

  return (
    <PanelWithLoading header={'Logged engagement'} isLoading={isLoading}>
      <ReactTable data={engagementEvents}
                  columns={columns}
                  showPagination={false}
                  showPageSizeOptions={false}
                  defaultPageSize={engagementEvents.length}
                  resizable={false} />
    </PanelWithLoading>
  )
}

export default LoggedEngagement
