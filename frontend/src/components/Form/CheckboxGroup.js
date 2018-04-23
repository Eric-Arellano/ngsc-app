// @flow
import React, { Component } from 'react'
import { Label } from 'components'
import type { CheckboxOption } from 'types'
import s from './CheckboxGroup.module.css'

type Props = {
  options: Array<CheckboxOption>,
  updateCurrentChecked: (Array<CheckboxOption>) => void,
}

type State = {}

class CheckboxGroup extends Component<Props, State> {

  handleToggle = (e: SyntheticInputEvent<HTMLInputElement>) => {
    const {options, updateCurrentChecked} = this.props
    const input = e.currentTarget.value
    const updatedOptions = options.map(option => {
        if (option.label === input) {
          option.checked = !option.checked
        }
        return option
      }
    )
    updateCurrentChecked(updatedOptions)
  }

  render () {
    const {options} = this.props
    return <ul>
      {options.map((option: CheckboxOption, index: number) => (
        <li key={index}>
          <Label>
            <input type='checkbox'
                   value={option.label}
                   checked={option.checked}
                   onChange={this.handleToggle}
                   className={s.checkbox}
            />
            {option.label}
          </Label>
        </li>
      ))
      }
    </ul>
  }
}

export default CheckboxGroup
