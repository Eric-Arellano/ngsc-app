// @flow
import React from 'react'
import { ButtonToolbar, Button } from 'react-bootstrap'
import type { Name } from 'flow/types'

type Props = {
  name: Name,
  confirmCorrectStudent: (boolean) => void
}

const Confirmation = (props: Props) => {
  const {name, confirmCorrectStudent} = props
  return (
    <div>
      <p>Are you {name.first} {name.last}?</p>
      <ButtonToolbar>
        <Button bsStyle={'success'} onClick={() => confirmCorrectStudent(true)}>Yes</Button>
        <Button bsStyle={'danger'} onClick={() => confirmCorrectStudent(false)}>No, wrong person!</Button>
      </ButtonToolbar>
    </div>
  )
}

export default Confirmation