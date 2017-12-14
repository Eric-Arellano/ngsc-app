import React from 'react'
import { Button } from 'components'
import './Error.css'

type Props = {
  children: React.Element<string>,
  resetState: () => void,
}

const Error = (props: Props) => {
  const {children, resetState} = props
  return (
    <div className="error">
      <p>{children}</p>
      <Button handleClick={resetState}>Back</Button>
    </div>
  )
}

export default Error