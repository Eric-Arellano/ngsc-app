// @flow
import * as React from 'react'
import { Confirmation, Error, Loading } from 'components'
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
  }
  else if (isError) {
    return <Error resetState={resetState}>User not found. Please enter a valid ID.</Error>
  }
  else {
    return <div>
      {!isValidated && <IDInputContainer onSubmit={verifyStudentId} />}
      {isValidated && !isConfirmed &&
      <Confirmation confirmCorrectStudent={confirmCorrectStudent} name={student.name} />}
    </div>
  }
}

export default LoginView