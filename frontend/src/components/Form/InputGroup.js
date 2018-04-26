// @flow
import * as React from 'react'
import s from './InputGroup.module.css'

type Props = {
  children: React.Node,  // can be any valid react element, e.g. array of Entry
  label: ?string,
}

const InputGroup = ({children, label}: Props) => (
  <div className={s.container}>
    {label && <p className={s.label}>{label}</p>}
    {children}
  </div>
)

export default InputGroup