// @flow
import React, { Component } from 'react'
import { IDInput } from 'components'

type Props = {
  onSubmit: (number) => void
}

type State = {
  currentValue: string,
  validationState: ValidationState
}

class IDInputContainer extends Component<Props, State> {

  state = {
    currentValue: '',
    validationState: 'neutral'
  }

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

  updateValidationState = (validationState: ValidationState) => {
    this.setState({validationState})
  }

  updateCurrentValue = (currentValue: string) => {
    this.setState({currentValue})
  }

  handleEnterKey = (e: SyntheticInputEvent<HTMLInputElement>) => {
    if (e.key === 'Enter') {
      e.preventDefault()
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
    return <IDInput {...this.state}
                    determineValidationState={this.determineValidationState}
                    handleSubmit={this.handleSubmit}
                    handleEnterKey={this.handleEnterKey}
                    updateCurrentValue={this.updateCurrentValue}
                    updateValidationState={this.updateValidationState} />
  }
}

export default IDInputContainer