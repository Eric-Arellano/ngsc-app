// @flow
import React from 'react'
import s from './Input.module.css'

type Props = {
  currentValue: string,
  validationState: ValidationState,
  placeholder: string,
  handleKeyInput: SyntheticInputEvent<HTMLInputElement> => void,
  handleEnterKey: SyntheticInputEvent<HTMLInputElement> => void
}

const Input = ({currentValue, validationState, placeholder, handleKeyInput, handleEnterKey}: Props) => (
  <input type={'number'} value={currentValue} placeholder={placeholder} onKeyDown={handleEnterKey}
         onChange={handleKeyInput} className={s[validationState]} />
)

Input.defaultProps = {
  currentValue: '',
  validationState: 'neutral'
}

export default Input
