// @flow
import React, { Component } from 'react'
import Credentials from './Credentials'
import type { ValidationState } from 'types'

type Props = {
  onSubmit: (number) => void
}

type State = {
  currentValue: string,
  validationState: ValidationState
}

class CredentialsContainer extends Component<Props, State> {

  state = {
    currentValue: '',
    validationState: 'neutral'
  }

  // TODO: add debounce to validation, using Lodash's debounce function.
  // componentDidMount() {
  //   this.determineValidationState = debounce(this.determineValidationState, 400)
  // }

  determineValidationState = (input: string) => {
    if (!input) {
      return 'neutral'
    } else {
      return this.checkIsValidId(input) ? 'valid' : 'invalid'
    }
  }

  checkIsValidId = (input: string) => {
    const num = Number(input)  // parse to number non-numeric answers will parse to NaN
    const isNumber = !isNaN(num)
    const length = num.toString().length
    return isNumber && length === 10
  }

  updateCurrentValue = (currentValue: string) => {
    const validationState = this.determineValidationState(currentValue)
    this.setState({
      currentValue,
      validationState
    })
  }

  handleEnterKey = (e: SyntheticInputEvent<HTMLInputElement>) => {
    if (e.key === 'Enter') {
      this.handleSubmit()
    }
  }

  handleSubmit = () => {
    const {onSubmit} = this.props
    const {currentValue, validationState} = this.state
    if (validationState === 'valid') {
      onSubmit(Number(currentValue))
    }
  }

  render () {
    return <Credentials {...this.state}
                        handleSubmit={this.handleSubmit}
                        handleEnterKey={this.handleEnterKey}
                        updateCurrentValue={this.updateCurrentValue} />
  }
}

export default CredentialsContainer