// @flow
import React from 'react'
import { ButtonToolbar, Button } from 'react-bootstrap'
import type { Name } from 'flow/types'
import '../App/style.css'

type Props = {
  name: Name,
  confirmCorrectStudent: (boolean) => void
}

const Confirmation = (props: Props) => {
  const {name, confirmCorrectStudent} = props
  return (
    <div>
      <h3 className="confirm-header">Are you {name.first} {name.last}?</h3>
      <ButtonToolbar>
        <Button bsStyle={'success'} onClick={() => confirmCorrectStudent(true)}>Yes</Button>
        <Button bsStyle={'danger'} onClick={() => confirmCorrectStudent(false)}>No, wrong person!</Button>
      </ButtonToolbar>
    </div>
  )
}

export default Confirmation