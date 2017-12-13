// @flow
import * as React from 'react'
import './Panel.css'

type Props = {
  children: React.Element<string>,
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