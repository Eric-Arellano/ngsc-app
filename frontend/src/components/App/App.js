// @flow
import React from 'react'
import { Header, Confirmation } from 'components'
import { IDInputContainer, RequirementsContainer } from 'containers'
import { Button } from 'react-bootstrap'
import type { Name } from 'flow/types'
import './style.css';

type Props = {
  isLoading: boolean,
  isValidated: boolean,
  isConfirmed: boolean,
  verifyStudentId: (number) => void,
  confirmCorrectStudent: (boolean) => void,
  resetState: () => void,
  id: ?number,
  name: Name
}

const App = (props: Props) => {
  const {isLoading, isValidated, isConfirmed, verifyStudentId, confirmCorrectStudent, resetState, id, name} = props
  if (isLoading) {
    return (
      <div className="ngsc-container">
        <Header/>
        <div className="container">
          <p>Loading...</p>
        </div>
      </div>
    )
  }

  if (id === 0) {
      return (
        <div className="ngsc-container">
          <Header />
          <div className="container">
            <h3 className="error">User Not Found. Please enter a valid ID.</h3>
            <Button onClick={resetState}> Back </Button>
          </div>
        </div>
      )
  }
  return (
    <div className={"ngsc-container"}> { /* TODO: how to convert this to array since the conditional logic? */ }
      <Header/>
      <div className="container">
        {!isValidated && <IDInputContainer onSubmit={verifyStudentId}/>}
        {isValidated && !isConfirmed && <Confirmation confirmCorrectStudent={confirmCorrectStudent} name={name}/>}
        {isValidated && isConfirmed && <RequirementsContainer id={id} name={name}/>}
      </div>
    </div>
  )
}

export default App