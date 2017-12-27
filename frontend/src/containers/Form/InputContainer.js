// @flow
import React, { Component } from 'react'
import { Input } from 'components'

type ValidationState = 'neutral' | 'invalid' | 'valid'

type Props = {
  placeholder: string,
  determineValidationState: (string) => ValidationState,
  handleEnterKey: SyntheticInputEvent<HTMLInputElement> => void,
  updateCurrentValue: (string) => void,
  updateValidationState: (ValidationState) => void
}

type State = {
  currentValue: string,
  validationState: ValidationState
}

class InputContainer extends Component<Props, State> {

  state = {
    currentValue: '',
    validationState: 'neutral'
  }

  handleKeyInput = (e: SyntheticInputEvent<HTMLInputElement>) => {
    const {determineValidationState, updateCurrentValue, updateValidationState} = this.props
    const input = e.currentTarget.value
    this.setState({currentValue: input}, () => {
      const {currentValue} = this.state
      const state = determineValidationState(currentValue)
      this.setState({validationState: state})
      updateCurrentValue(currentValue)
      updateValidationState(state)
    })
  }

  render () {
    return <Input {...this.state} {...this.props} handleKeyInput={this.handleKeyInput} />
  }
}

export default InputContainer