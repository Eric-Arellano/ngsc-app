// @flow
import * as React from 'react'
import s from './Button.module.css'

type Props = {
  children: React.Node,
}

const ButtonGroup = (props: Props) => {
  return (
    <div className={s.group}>
      {props.children}
    </div>
  )
}

export default ButtonGroup