// @flow
import React, { Component } from 'react'
import { Label } from 'components'
import type { RadioOption } from 'types'
import s from './RadioGroup.module.css'

type Props = {
  options: Array<RadioOption>,
  default: ?RadioOption,
  updateCurrentSelection: (RadioOption) => void,
}

type State = {
  currentSelection: RadioOption,
}

class RadioGroup extends Component<Props, State> {

  state = {
    currentSelection: this.props.default
  }

  handleSelection = (e: SyntheticInputEvent<HTMLInputElement>) => {
    const {options, updateCurrentSelection} = this.props
    const input = e.currentTarget.value
    const newSelection: RadioOption = options.find(option => option.label === input)
    this.setState({currentSelection: newSelection}, () => {
      updateCurrentSelection(newSelection)
    })
  }

  render () {
    const {currentSelection} = this.state
    const {options} = this.props
    return <ul>
      {options.map((option: RadioOption) => (
        <li>
          <Label>
            <input type='radio'
                   value={option.label}
                   checked={currentSelection === option}
                   onChange={this.handleSelection}
                   className={s.radio} />
            {option.label}
          </Label>
        </li>
      ))
      }
    </ul>
  }
}

export default RadioGroup
