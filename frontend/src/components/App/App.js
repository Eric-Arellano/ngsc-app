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
  const Aux = props => props.children
  return (
    <Aux>
      <Header/>
      {!isValidated && <IDInputContainer onSubmit={verifyStudentId}/>}
      {isValidated && !isConfirmed && <Confirmation confirmCorrectStudent={confirmCorrectStudent} name={name}/>}
      {isValidated && isConfirmed && <RequirementsContainer id={id} name={name}/>}
    </Aux>
  )
}

export default App