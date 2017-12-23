// @flow
import React from 'react'
import { Button, ButtonGroup } from 'components'
import type { Name } from 'flow/types'

type Props = {
  name: Name,
  confirmCorrectStudent: (boolean) => void
}

const Confirmation = ({name, confirmCorrectStudent}: Props) => {
  return (
    <div>
      <h3>Are you {name.first} {name.last}?</h3>
      <ButtonGroup>
        <Button type={'success'} handleClick={() => confirmCorrectStudent(true)}>Yes</Button>
        <Button type={'danger'} handleClick={() => confirmCorrectStudent(false)}>No, wrong person!</Button>
      </ButtonGroup>
    </div>
  )
}

export default Confirmation