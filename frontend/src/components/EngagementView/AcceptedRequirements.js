// @flow
import React from 'react'
import { Entry, Panel } from 'components'

type Props = {
  service: number,
  civilMil: number
}

const AcceptedRequirements = ({service, civilMil}: Props) => (
  <Panel header='Accepted Requirements'>
    <Entry>Accepted # of service hours: {service}</Entry>
    <Entry>Accepted # of Civil Mil: {civilMil}</Entry>
  </Panel>
)

export default AcceptedRequirements