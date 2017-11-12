// @flow
import React from 'react'
import { Header, Confirmation } from 'components'
import { IDInputContainer, RequirementsContainer } from 'containers'
import type { Name } from 'flow/types'

type Props = {
  isLoading: boolean,
  isValidated: boolean,
  isConfirmed: boolean,
  verifyStudentId: (number) => void,
  confirmCorrectStudent: (boolean) => void,
  id: ?number,
  name: Name
}

const App = (props: Props) => {
  const {isLoading, isValidated, isConfirmed, verifyStudentId, confirmCorrectStudent, id, name} = props

  return (
    <div> { /* TODO: how to convert this to array since the conditional logic? */ }
      <Header/>
      {!isValidated && <IDInputContainer onSubmit={verifyStudentId}/>}
      {isValidated && !isConfirmed && <Confirmation confirmCorrectStudent={confirmCorrectStudent} name={name}/>}
      {isValidated && isConfirmed && <RequirementsContainer id={id} name={name}/>}
    </div>
  )
}

export default App