// @flow
import React from 'react'
import { Button } from 'components'
import { InputContainer } from 'containers'

type Props = {
  validationState: ValidationState,
  determineValidationState: (string) => ValidationState,
  handleEnterKey: SyntheticInputEvent<HTMLInputElement> => void,
  updateCurrentValue: string => void,
  updateValidationState: ValidationState => void,
  handleSubmit: () => void,
}

const IDInput = ({
                   validationState, determineValidationState, updateCurrentValue, updateValidationState,
                   handleEnterKey, handleSubmit
                 }: Props) => {
  const isSubmitDisabled = validationState !== 'valid'
  return (
    <form>
      <InputContainer placeholder={'Enter student ID'} determineValidationState={determineValidationState}
                      handleEnterKey={handleEnterKey} updateCurrentValue={updateCurrentValue}
                      updateValidationState={updateValidationState} />
      <Button disabled={isSubmitDisabled} handleClick={handleSubmit}>Submit</Button>
    </form>
  )
}

export default IDInput