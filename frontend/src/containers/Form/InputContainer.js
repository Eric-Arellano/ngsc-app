// @flow
import React, { Component } from 'react'
import { Input } from 'components'
import debounce from 'lodash/debounce'

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
  static defaultProps = {
    debounceDelay: 800
  }
  state = {
    currentValue: '',
    validationState: 'neutral'
  }

  componentDidMount() {
    this.validateInput = debounce(this.validateInput, this.props.debounceDelay)
  }

  validateInput = str => {
    const newState = this.props.determineValidationState(str)
    this.setState({validationState: newState})
  }

  handleKeyInput = (e: SyntheticInputEvent<HTMLInputElement>) => {
    const {determineValidationState, updateCurrentValue, updateValidationState} = this.props
    const input = e.currentTarget.value
    this.setState({currentValue: input}, () => {
      const {currentValue} = this.state
      const state = determineValidationState(currentValue)
      // this.setState({validationState: state})
      this.validateInput(this.state.currentValue)
      updateCurrentValue(currentValue)
      updateValidationState(state)
    })
  }

  render () {
    return <Input {...this.state} {...this.props} handleKeyInput={this.handleKeyInput} />
  }
}

export default InputContainer
