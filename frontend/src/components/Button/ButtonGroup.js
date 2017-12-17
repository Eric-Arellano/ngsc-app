// @flow
import * as React from 'react'
import s from './ButtonGroup.module.css'

type Props = {
  children: React.Node,
}

const ButtonGroup = (props: Props) => {
  return (
    <div className={s.container}>
      {props.children}
    </div>
  )
}

export default ButtonGroup