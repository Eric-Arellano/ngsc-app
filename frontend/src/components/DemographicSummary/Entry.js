// @flow
import React from 'react'

type Props = {
  header: string,
  value: string
}

const Entry = (props: Props) => {
  const {header, value} = props
  return (
    <p>{header}: {value}</p>
  )
}

export default Entry