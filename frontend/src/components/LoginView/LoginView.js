// @flow
import * as React from 'react'
import { Button, Confirmation, Loading } from 'components'
import { IDInputContainer } from 'containers'
import type { Student } from 'flow/types'

type Props = {
  isLoading: boolean,
  isError: boolean,
  isValidated: boolean,
  isConfirmed: boolean,
  verifyStudentId: (number) => void,
  confirmCorrectStudent: (boolean) => void,
  resetState: () => void,
  student: ?Student
}

const LoginView = (props: Props) => {
  const {isLoading, isError, isValidated, isConfirmed, verifyStudentId, confirmCorrectStudent, resetState, student} = props

  if (isLoading) {
    return <Loading />
  } else if (isError) {
    return <div>
      <h3 className="error">User not found. Please enter a valid ID.</h3>
      <Button handleClick={resetState}>Back</Button>
    </div>
  } else {
    return <div>
      {!isValidated && <IDInputContainer onSubmit={verifyStudentId} />}
      {isValidated && !isConfirmed &&
      <Confirmation confirmCorrectStudent={confirmCorrectStudent} name={student.name} />}
    </div>
  }
}

export default LoginView