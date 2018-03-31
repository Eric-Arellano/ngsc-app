// @flow
import React, { Component } from 'react'
import { Button, CheckboxGroup, Input, Label, RadioGroup } from 'components'
import { actionList, folderTargets } from './options.js'
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

  fileOrFolder = (action: RadioOption): string => (
    action.isFile ? 'file' : 'folder'
  )

  sourcePlaceholder = (action: RadioOption): string => (
    action.isFile ? 'Leadership/Example.gslides' : 'Leadership/Retreat 1'
  )

  targetPlaceholder = (action: RadioOption): string => (
    action.isFile ? 'Example.gslides' : 'Retreat 1'
  )

  render () {
    const {action, targetFolders} = this.state
    return <div>
      <section>
        <p>Choose which action you'd like to take:</p>
        <RadioGroup options={actionList}
                    updateCurrentSelection={this.updateAction} />
      </section>
      <br />
      <section>
        <p>Choose which groups you would like to apply the action to:</p>
        <CheckboxGroup options={targetFolders}
                       updateCurrentChecked={this.updateFolderTargets} />
      </section>
      <br />
      {action && action.needsSource && <section>
        <Label>Source {this.fileOrFolder(action)} name:</Label>
        <Input placeholder={this.sourcePlaceholder(action)} />
      </section>}
      {action && action.needsTarget && <section>
        <Label>Target {this.fileOrFolder(action)} name:</Label>
        <Input placeholder={this.targetPlaceholder(action)} />
      </section>}
      <section>
        <Button handleClick={this.submit}>Submit</Button>
      </section>
    </div>
  }
}

export default AdminView