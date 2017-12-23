// @flow
import React from 'react'
import { Confirmation } from 'components'
import { IDInputContainer } from 'containers'
import type { Student } from 'flow/types'

type Props = {
  isValidated: boolean,
  isConfirmed: boolean,
  verifyStudentId: (number) => void,
  confirmCorrectStudent: (boolean) => void,
  student: ?Student
}

const LoginView = ({isValidated, isConfirmed, verifyStudentId, confirmCorrectStudent, student}: Props) => (
  <div>
    {!isValidated && <IDInputContainer onSubmit={verifyStudentId} />}
    {isValidated && !isConfirmed && <Confirmation confirmCorrectStudent={confirmCorrectStudent} name={student.name} />}
  </div>
)

export default LoginView