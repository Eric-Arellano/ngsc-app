// @flow
import React from 'react'
import { Entry, Loading, Panel } from 'components'

type Props = {
  service: number,
  civilMil: number,
  isLoading: boolean
}

const AcceptedEngagement = ({service, civilMil, isLoading}: Props) => {
  if (isLoading) {
    return (<Panel header={'Accepted Engagement'}>
      <Loading />
    </Panel>)
  }
  return (
    <Panel header='Accepted Engagement'>
      <Entry>Accepted # of service hours: {service}</Entry>
      <Entry>Accepted # of Civil Mil: {civilMil}</Entry>
    </Panel>
  )
}

export default AcceptedEngagement