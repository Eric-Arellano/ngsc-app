// @flow
import React from 'react'
import Confirmation from './Confirmation'
import CredentialsContainer from './CredentialsContainer'
import type { Student } from 'types'

type Props = {
  isValidated: boolean,
  isConfirmed: boolean,
  verifyStudentId: (number) => void,
  confirmCorrectStudent: (boolean) => void,
  resetState: () => void,
  student: ?Student
}

const LoginView = ({isValidated, isConfirmed, verifyStudentId, confirmCorrectStudent, resetState, student}: Props) => (
  <div>
    {!isValidated && <CredentialsContainer onSubmit={verifyStudentId} />}
    {isValidated && !isConfirmed &&
    <Confirmation confirmCorrectStudent={confirmCorrectStudent} name={student.name} resetState={resetState} />}
  </div>
)

export default LoginView