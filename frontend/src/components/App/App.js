// @flow
import * as React from 'react'
import { Header, Confirmation } from 'components'
import { IDInputContainer, RequirementsContainer } from 'containers'
import { Button } from 'react-bootstrap'
import type { Name } from 'flow/types'
import './style.css';

type Props = {
  isLoading: boolean,
  isError: boolean,
  isValidated: boolean,
  isConfirmed: boolean,
  verifyStudentId: (number) => void,
  confirmCorrectStudent: (boolean) => void,
  resetState: () => void,
  id: ?number,
  missionTeam: ?number,
  committee: ?string,
  cohort: ?number,
  name: Name
}

const App = (props: Props) => {
  const {isLoading, isError, isValidated, isConfirmed, verifyStudentId, confirmCorrectStudent, resetState } = props

  let container: React.Element<'div'>
  if (isLoading) {
    container = <div className="container">
                  <p>Loading...</p>
                </div>
  } else if (isError) {
    container = <div className="container">
                  <h3 className="error">User not found. Please enter a valid ID.</h3>
                  <Button onClick={resetState}> Back </Button>
                </div>
  } else {
    container = <div className="container">
                  {!isValidated && <IDInputContainer onSubmit={verifyStudentId}/>}
                  {isValidated && !isConfirmed && <Confirmation confirmCorrectStudent={confirmCorrectStudent} {...props} />}
                  {isValidated && isConfirmed && <RequirementsContainer {...props}/>}
                </div>
  }

  return (
    <div className={"ngsc-container"}>
      <Header/>
      {container}
    </div>
  )
}

export default App