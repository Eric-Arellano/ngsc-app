// @flow
import React, { Component } from 'react'
import type { ValidationState } from 'types'
import s from './Input.module.css'

type Props = {
  validationState: ValidationState,
  inputType: ?string,
  placeholder: ?string,
  updateCurrentValue: (string) => void,
  handleEnterKey: ?(SyntheticInputEvent<HTMLInputElement> => void),
}

type State = {
  currentValue: string,
}

class Input extends Component<Props, State> {

  static defaultProps = {
    validationState: 'neutral',
    inputType: 'text',
  }

  state = {
    currentValue: ''
  }

  handleKeyInput = (e: SyntheticInputEvent<HTMLInputElement>) => {
    const {updateCurrentValue} = this.props
    const input = e.currentTarget.value
    this.setState({currentValue: input}, () => {
      const {currentValue} = this.state
      updateCurrentValue(currentValue)
    })
  }

  render () {
    const {validationState, placeholder, handleEnterKey, inputType} = this.props
    const {currentValue} = this.state
    return <input type={inputType} value={currentValue} placeholder={placeholder} onKeyDown={handleEnterKey}
                  onChange={this.handleKeyInput} className={s[validationState]} />
  }
}

export default Input
