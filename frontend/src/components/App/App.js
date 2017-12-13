// @flow
import * as React from 'react'
import { Button, Confirmation, Header, Loading } from 'components'
import { EngagementViewContainer, IDInputContainer } from 'containers'
import type { Student } from 'flow/types'
import './App.css'

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

const App = (props: Props) => {
  const {isLoading, isError, isValidated, isConfirmed, verifyStudentId, confirmCorrectStudent, resetState, student} = props

  let container: React.Element<'div'>
  if (isLoading) {
    container = <div className="container"><Loading /></div>
  } else if (isError) {
    container = <div className="container">
      <h3 className="error">User not found. Please enter a valid ID.</h3>
      <Button handleClick={resetState}>Back</Button>
    </div>
  } else {
    container = <div className="container">
      {!isValidated && <IDInputContainer onSubmit={verifyStudentId} />}
      {isValidated && !isConfirmed && <Confirmation confirmCorrectStudent={confirmCorrectStudent} name={student.name} />}
      {isValidated && isConfirmed && <EngagementViewContainer student={student} />}
    </div>
  }

  return (
    <div className={'ngsc-container'}>
      <Header />
      {container}
    </div>
  )
}

export default App