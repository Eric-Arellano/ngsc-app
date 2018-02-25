// @flow
import React from 'react'
import { Button, Input, Label } from 'components'
import type { ValidationState } from 'types'

type Props = {
  validationState: ValidationState,
  handleEnterKey: SyntheticInputEvent<HTMLInputElement> => void,
  updateCurrentValue: string => void,
  handleSubmit: () => void,
}

const Credentials = ({
  validationState,
  updateCurrentValue,
  handleEnterKey,
  handleSubmit
}: Props) => {
  const isSubmitDisabled = validationState !== 'valid'
  return (
    <form>
      <Label>{'Student ID:'}</Label>
      <Input
        placeholder={'Enter student ID'}
        validationState={validationState}
        handleEnterKey={handleEnterKey}
        updateCurrentValue={updateCurrentValue}
      />
      <Button disabled={isSubmitDisabled} handleClick={handleSubmit}>
        {'Submit'}
      </Button>
    </form>
  )
}

export default Credentials
