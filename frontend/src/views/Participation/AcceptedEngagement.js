// @flow
import React from 'react'
import { Entry, PanelWithLoading } from 'components'

type Props = {
  service: number,
  civilMil: number,
  isLoading: boolean
}

const AcceptedEngagement = ({service, civilMil, isLoading}: Props) => (
  <PanelWithLoading header='Accepted Engagement' isLoading={isLoading}>
    <Entry>Accepted # of service hours: {service}</Entry>
    <Entry>Accepted # of Civil Mil: {civilMil}</Entry>
  </PanelWithLoading>
)

export default AcceptedEngagement