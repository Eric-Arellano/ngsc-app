// @flow
import React from 'react'
import { Button } from 'components'
import type { Name } from 'flow/types'

type Props = {
  name: Name,
  confirmCorrectStudent: (boolean) => void
}

const Confirmation = ({name, confirmCorrectStudent}: Props) => {
  return (
    <div>
      <h3 className="confirm-header">Are you {name.first} {name.last}?</h3>
      <div className={'button-toolbar'}>
        <Button type={'success'} handleClick={() => confirmCorrectStudent(true)}>Yes</Button>
        <Button type={'danger'} handleClick={() => confirmCorrectStudent(false)}>No, wrong person!</Button>
      </div>
    </div>
  )
}

export default Confirmation