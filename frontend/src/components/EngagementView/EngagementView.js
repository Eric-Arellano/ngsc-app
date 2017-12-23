// @flow
import React from 'react'
import { AcceptedRequirements, Attendance, Demographics, Error, Loading, LoggedRequirements } from 'components'
import type { Requirement, Student } from 'flow/types'

type Props = {
  isLoading: boolean,
  isError: boolean,
  student: Student,
  service: number,
  civilMil: number,
  noShows: number,
  requirements: Array<Requirement>,
  resetState: () => void
}

const EngagementView = ({isError, isLoading, student, civilMil, service, noShows, requirements, resetState}: Props) => {

  if (isLoading) {
    return <Loading />
  }
  else if (isError) {
    return <Error resetState={resetState}>There was an error. Please try again.</Error>
  }
  return [
    <Demographics {...student} key={0} />,
    <Attendance noShows={noShows} key={1} />,
    <AcceptedRequirements service={service} civilMil={civilMil} key={2} />,
    <LoggedRequirements requirements={requirements} key={3} />
  ]
}

export default EngagementView
