// @flow
import * as React from 'react'
import './Button.css'

type ButtonType = 'success' | 'danger' | 'ngsc'

type Props = {
  children: React.Element<any>,
  handleClick: () => mixed,
  type?: ButtonType,
  disabled?: boolean
}

const Button = (props: Props) => {
  const {children, handleClick, type, disabled} = props
  const style = `button-${type}`
  return (
    <button onClick={handleClick}
            className={`button ${style}`}
            disabled={disabled}>
      {children}
    </button>
  )
}

Button.defaultProps = {
  children: '',
  type: 'ngsc',
  disabled: false
}

export default Button