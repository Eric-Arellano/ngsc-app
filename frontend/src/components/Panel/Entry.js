// @flow
import React from 'react'

type Props = {
  children: React.Element<string>
}

const Entry = (props: Props) => {
  return (
    <p>{props.children}</p>
  )
}

export default Entry