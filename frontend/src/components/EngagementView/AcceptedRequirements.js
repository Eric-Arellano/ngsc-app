// @flow
import React from 'react'
import { Entry, Panel } from 'components'

type Props = {
  service: number,
  civilMil: number
}

const AcceptedRequirements = (props: Props) => (
  <Panel header='Accepted Requirements'>
    <Entry>Accepted # of service hours: {props.service}</Entry>
    <Entry>Accepted # of Civil Mil: {props.civilMil}</Entry>
  </Panel>
)

export default AcceptedRequirements