import React from 'react'
import { Error } from 'components'

// Call this decorator on render() function.
// Class must have isError state value and resetState as class property.
const withError = (errorMessage: string) => (target, key, descriptor) => {
  target.renderOnLoad = target.renderOnLoad || descriptor.value
  descriptor.value = function () {
    const render = target.renderOnLoad.bind(this)
    const {isError} = this.state
    const {resetState} = this
    if (isError) {
      return <Error resetState={resetState}>{errorMessage}</Error>
    }
    return render()
  }
}

export default withError