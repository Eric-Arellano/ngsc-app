// @flow
import React from 'react'
import { Entry, Panel } from 'components'

type Props = {
  service: number,
  civilMil: number
}

const AcceptedEngagement = ({service, civilMil}: Props) => (
  <Panel header='Accepted Engagement'>
    <Entry>Accepted # of service hours: {service}</Entry>
    <Entry>Accepted # of Civil Mil: {civilMil}</Entry>
  </Panel>
)

export default AcceptedEngagement