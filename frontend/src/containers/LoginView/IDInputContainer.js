// @flow
import React, { Component } from 'react'
import { IDInput } from 'components'

type Props = {
  onSubmit: (number) => void
}

type State = {
  currentValue: string,
  validationState: ?string,
  submitDisabled: boolean,
}

class IDInputContainer extends Component<Props, State> {

  state = {
    currentValue: '',
    validationState: null,
    submitDisabled: true,
  }

  determineValidationState (input: string) {
    const {currentValue} = this.state
    if (!currentValue) {
      return null
    } else {
      return this.isValidId(currentValue) ? 'success' : 'error'
    }
  }

  isValidId = (input: string) => {
    const num = Number(input)  // parse to number non-numeric answers will parse to NaN
    const isNumber = !isNaN(num)
    const length = num.toString().length
    return length === 10 && isNumber
  }

  handleKeyInput = (e: SyntheticInputEvent<HTMLInputElement>) => {
    const input = e.currentTarget.value
    this.setState({currentValue: input}, () => {
      const {currentValue} = this.state
      this.setState({validationState: this.determineValidationState(currentValue)})
    })

    if (input === '') {
      this.setState({submitDisabled: true})
    } else if (!this.isValidId(input)) {
      this.setState({submitDisabled: true})
    } else {
      this.setState({submitDisabled: false})
    }
  }

  handleEnterKey = (e: SyntheticInputEvent<HTMLInputElement>) => {
    if (e.key === 'Enter') {
      e.preventDefault()
      this.handleSubmit()
    }
  }

  handleSubmit = () => {
    const {currentValue} = this.state
    if (this.isValidId(currentValue)) {
      this.props.onSubmit(Number(currentValue))
    }
  }

  render () {
    return <IDInput {...this.state}
                    handleSubmit={this.handleSubmit}
                    handleKeyInput={this.handleKeyInput}
                    handleEnterKey={this.handleEnterKey} />
  }
}

export default IDInputContainer