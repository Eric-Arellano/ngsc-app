// @flow
import React from 'react'
import { AcceptedRequirements, Demographics, Error, Loading, LoggedRequirements } from 'components'
import type { Requirement, Student } from 'flow/types'

type Props = {
  isLoading: boolean,
  isError: boolean,
  student: Student,
  service: number,
  civilMil: number,
  requirements: Array<Requirement>,
  resetState: () => void
}

const EngagementView = (props: Props) => {
  const {isError, isLoading, student, civilMil, service, requirements, resetState} = props

  if (isLoading) {
    return <Loading />
  }
  else if (isError) {
    return <Error resetState={resetState}>There was an error. Please try again.</Error>
  }
  return [
    <Demographics student={student} key={0} />,
    <AcceptedRequirements service={service} civilMil={civilMil} key={1} />,
    <LoggedRequirements requirements={requirements} key={2} />
  ]
}

export default EngagementView
