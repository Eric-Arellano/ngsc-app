// @flow
import * as React from 'react'
import s from './Button.module.css'

type Props = {
  children: React.Node,
}

const ButtonGroup = ({children}: Props) => (
  <div className={s.group}>
    {children}
  </div>
)

export default ButtonGroup