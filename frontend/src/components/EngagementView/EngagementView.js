// @flow
import React from 'react'
import { AcceptedRequirements, Attendance, Demographics, Error, Loading, LoggedRequirements } from 'components'
import type { Requirement, Student } from 'flow/types'

type Props = {
  student: Student,
  service: number,
  civilMil: number,
  noShows: number,
  requirements: Array<Requirement>,
}

const EngagementView = ({student, civilMil, service, noShows, requirements}: Props) => [
  <Demographics {...student} key={0} />,
  <Attendance noShows={noShows} key={1} />,
  <AcceptedRequirements service={service} civilMil={civilMil} key={2} />,
  <LoggedRequirements requirements={requirements} key={3} />
]

export default EngagementView
