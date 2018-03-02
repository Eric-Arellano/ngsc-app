// @flow
import React from 'react'
import { Button, ButtonGroup } from 'components'
import type { Name } from 'types'

type Props = {
  name: Name,
  confirmCorrectStudent: (boolean) => void,
  resetState: () => void
}

const Confirmation = ({name, confirmCorrectStudent, resetState}: Props) => {
  return (
    <div>
      <h3>Are you {name.first} {name.last}?</h3>
      <ButtonGroup>
        <Button validationState={'valid'} handleClick={() => confirmCorrectStudent(true)}>Yes</Button>
        <Button validationState={'invalid'} handleClick={resetState}>No, wrong person!</Button>
      </ButtonGroup>
    </div>
  )
}

export default Confirmation