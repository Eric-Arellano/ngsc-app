// @flow
import * as React from 'react'
import './Panel.css'

type Props = {
  children: React.Node,  // can be any valid react element, e.g. array of Entry
  header: string
}

const Panel = (props: Props) => {
  const {children, header} = props
  return (
    <div className="panel">
      <h3 className="panel-heading">{header}</h3>
      <div className="panel-body">{children}</div>
    </div>
  )
}

export default Panel