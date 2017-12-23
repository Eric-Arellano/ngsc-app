import React from 'react'
import { Loading } from 'components'

function withLoading (WrappedComponent) {
  return function withLoadingComponent ({isLoading, ...props}) {
    if (isLoading) return <Loading />
    return <WrappedComponent {...props} />
  }
}

export default withLoading