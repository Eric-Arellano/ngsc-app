// @flow
import React, { Component } from 'react'
import { IDInput } from 'components'

type Props = {
  onSubmit: (number) => void
}

type State = {
  currentValue: string,
  validationState: ?string,
  submissionFailed: boolean,
}

class IDInputContainer extends Component<Props, State> {

  state = {
    currentValue: '',
    validationState: null,
    submissionFailed: false
  }

  determineValidationState(input: string) {
    if (this.state.currentValue.length <= 0) return null
    else return this.isValidId(input) ? 'success' :  'error'
  }

  isValidId = (input: string) => {
    const num = Number(input)  // parse to number non-numeric answers will parse to NaN
    const isNumber = !isNaN(num)
    const length = num.toString().length
    return length === 10 && isNumber
  }

  handleKeyInput = (e: SyntheticInputEvent<HTMLInputElement>) => {
    const input = e.currentTarget.value
    this.setState({
      currentValue: input,
      validationState: this.determineValidationState(input),
    })
  }

  handleSubmit = () => {
    const { currentValue } = this.state
    if (this.isValidId(currentValue)) {
      this.props.onSubmit(Number(currentValue))
    } else {
      this.setState({ submissionFailed: false })
    }
  }

  render() {
    return <IDInput {...this.state} handleSubmit={this.handleSubmit} handleKeyInput={this.handleKeyInput} />
  }
}

export default IDInputContainer