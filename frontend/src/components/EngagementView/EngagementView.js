// @flow
import React from 'react'
import { AcceptedRequirements, Demographics, Loading, LoggedRequirements } from 'components'
import type { Requirement, Student } from 'flow/types'

type Props = {
  isLoading: boolean,
  isError: boolean,
  student: Student,
  service: number,
  civilMil: number,
  requirements: Array<Requirement>,
}

const EngagementView = (props: Props) => {
  const {isError, isLoading, student, civilMil, service, requirements} = props
  if (isError) {
    return <p>Error</p>
  }
  if (isLoading) {
    return <Loading />
  }
  return [
    <Demographics student={student} key={0} />,
    <AcceptedRequirements service={service} civilMil={civilMil} key={1} />,
    <LoggedRequirements requirements={requirements} key={2} />
  ]
}

export default EngagementView
