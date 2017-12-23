import React from 'react'
import { Error } from 'components'

function withError (WrappedComponent, resetState: () => void, errorMessage: string) {
  return function withErrorComponent ({isError, ...props}) {
    if (isError) {
      return <Error resetState={resetState}>{errorMessage}</Error>
    }
    return <WrappedComponent {...props} />
  }
}

export default withError