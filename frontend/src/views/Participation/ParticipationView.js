// @flow
import React from 'react'
import AttendanceContainer from './AttendanceContainer'
import Demographics from './Demographics'
import EngagementContainer from './EngagementContainer'
import type { Student } from 'types'

type Props = {
  student: Student,
  resetState: () => void
}

const ParticipationView = ({student, resetState}: Props) => [
  <Demographics student={student} key={0} />,
  <AttendanceContainer student={student} resetState={resetState} key={1} />,
  <EngagementContainer student={student} resetState={resetState} key={2} />
]

export default ParticipationView
