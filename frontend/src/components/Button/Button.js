// @flow
import * as React from 'react'
import s from './Button.module.css'
import type { ValidationState } from 'types'

type Props = {
  children: React.Element<string>,
  handleClick: () => mixed,
  validationState?: ValidationState,
  disabled?: boolean
}

const Button = ({children, handleClick, validationState = 'neutral', disabled = false}: Props) => (
  <button
    onClick={handleClick}
    className={s[validationState]}
    disabled={disabled}
    type={'button'}
  >
    { children ? children : null }
  </button>
)

export default Button
