// @flow
import * as React from 'react'
import s from './Button.module.css'

type ButtonType = 'success' | 'danger' | 'ngsc'

type Props = {
  children: React.Element<string>,
  handleClick: () => mixed,
  btnType?: ButtonType,
  disabled?: boolean
}

const Button = ({children, handleClick, btnType = 'ngsc', disabled = false}: Props) => (
  <button
    onClick={handleClick}
    className={s[btnType]}
    disabled={disabled}
  >
    { children ? children : null }
  </button>
)

export default Button
