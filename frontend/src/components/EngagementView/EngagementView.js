// @flow
import React from 'react'
import { AcceptedRequirements, Attendance, Demographics, LoggedRequirements } from 'components'
import type { Requirement, Student } from 'flow/types'

type Props = {
  student: Student,
  service: number,
  civilMil: number,
  noShows: number,
  mt_percent : string,
  com_percent: string,
  requirements: Array<Requirement>,
}

const EngagementView = ({student, civilMil, service, noShows, mt_percent, com_percent, requirements}: Props) => [
  <Demographics {...student} key={0} />,
  <Attendance noShows={noShows} mt_percent={mt_percent} com_percent={com_percent} key={1} />,
  <AcceptedRequirements service={service} civilMil={civilMil} key={2} />,
  <LoggedRequirements requirements={requirements} key={3} />
]

export default EngagementView
