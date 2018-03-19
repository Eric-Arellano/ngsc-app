// @flow
import React, { Component } from 'react'
import { Button, CheckboxGroup, Input, Label, RadioGroup } from 'components'
import { actionList, folderTargets } from './Options.js'
import type { CheckboxOption, RadioOption } from 'types'

type Props = {}

type State = {
  targetFolders: Array<CheckboxOption>,
  action: ?RadioOption,
  sourcePath: ?string,
  targetPaths: ?Array<string>
}

class AdminView extends Component<Props, State> {

  state = {
    targetFolders: folderTargets,
    action: null,
    sourcePath: null,
    targetPaths: null
  }

  updateAction = (action: RadioOption) => {
    this.setState({action})
  }

  updateFolderTargets = (targetFolders: Array<CheckboxOption>) => {
    this.setState({targetFolders})
  }

  updateSourcePath = (sourcePath: string) => {
    this.setState({sourcePath})
  }

  updateTargetPaths = (targetPaths: Array<string>) => {
    this.setState({targetPaths})
  }

  submit = () => {

  }

  render () {
    const {action, targetFolders} = this.state
    return <div>
      <section>
        <p>Choose which groups you would like to apply the action to:</p>
        <CheckboxGroup options={targetFolders}
                       updateCurrentChecked={this.updateFolderTargets} />
      </section>
      <br />
      <section>
        <p>Choose which action you'd like to take:</p>
        <RadioGroup options={actionList}
                    updateCurrentSelection={this.updateAction} />
      </section>
      <br />
      {action && action.needsSource && <section>
        <Label>Source file name:</Label>
        <Input placeholder='ex: Leadership/Retreat 1/Google Drive.gslides' />
      </section>}
      {action && action.needsTarget && <section>
        <Label>Target file name:</Label>
        <Input placeholder='ex: Leadership/Retreat 1/Google Drive.gslides' />
      </section>}
      <section>
        <Button handleClick={this.submit}>Submit</Button>
      </section>
    </div>
  }
}

export default AdminView