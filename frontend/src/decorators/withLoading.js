// @flow

import React from 'react'
import { Loading } from 'components'

// Call this decorator on render() function.
// Class must have isLoading state value.
const withLoading = (target, key, descriptor) => {
  target.renderOnLoad = target.renderOnLoad || descriptor.value
  descriptor.value = function () {
    const render = target.renderOnLoad.bind(this)
    const {isLoading} = this.state
    if (isLoading) return <Loading />
    return render()
  }
}

export default withLoading