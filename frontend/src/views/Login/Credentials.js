// @flow
import React from 'react'
import { Button, Input } from 'components'
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
      <Input
        label='Student ID:'
        placeholder='Enter student ID'
        validationState={validationState}
        handleEnterKey={handleEnterKey}
        updateCurrentValue={updateCurrentValue}
        inputType='number'
      />
      <Button disabled={isSubmitDisabled} handleClick={handleSubmit}>
        {'Submit'}
      </Button>
    </form>
  )
}

export default Credentials
