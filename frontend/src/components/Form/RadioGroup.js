// @flow
import React, { Component } from 'react'
import { Label } from 'components'
import s from './RadioGroup.module.css'

type Props = {
  options: Array<string>,
  updateCurrentSelection: (string) => void,
}

type State = {
  currentSelection: string,
}

class RadioGroup extends Component<Props, State> {

  state = {
    currentSelection: ''
  }

  handleSelection = (e: SyntheticInputEvent<HTMLInputElement>) => {
    const {updateCurrentSelection} = this.props
    const input = e.currentTarget.value
    this.setState({currentSelection: input}, () => {
      const {currentSelection} = this.state
      updateCurrentSelection(currentSelection)
    })
  }

  render () {
    const {currentSelection} = this.state
    const {options} = this.props
    return <ul>
      {options.map((option: string) => (
        <li>
          <Label>
            <input type='radio'
                   value={option}
                   checked={currentSelection === option}
                   onChange={this.handleSelection}
                   className={s.radio} />
            {option}
          </Label>
        </li>
      ))
      }
    </ul>
  }
}

export default RadioGroup
