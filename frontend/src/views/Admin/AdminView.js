// @flow
import * as React from 'react'
import { Button, CheckboxGroup, Input, Label, RadioGroup } from 'components'
import { actionList, folderTargets, mimeType, semesterTarget } from './options.js'
import type { CheckboxOption, RadioOption } from 'types'

type Props = {}

type State = {
  semesterTarget: RadioOption,
  targetFolders: Array<CheckboxOption>,
  action: ?RadioOption,
  sourcePath: ?string,
  targetPaths: ?Array<string>,
  mimeType: ?RadioOption,
}

class AdminView extends React.Component<Props, State> {

  state = {
    semesterTarget: null,
    targetFolders: folderTargets,
    action: null,
    sourcePath: null,
    targetPaths: null,
    mimeType: null,
  }

  updateSemesterTarget = (semesterTarget: RadioOption): void => {
    this.setState({semesterTarget})
  }

  updateAction = (action: RadioOption): void => {
    this.setState({action})
  }

  updateFolderTargets = (targetFolders: Array<CheckboxOption>): void => {
    this.setState({targetFolders})
  }

  updateSourcePath = (sourcePath: string): void => {
    this.setState({sourcePath})
  }

  updateTargetPaths = (targetPaths: Array<string>): void => {
    this.setState({targetPaths})
  }

  updateMimeType = (mimeType: RadioOption): void => {
    this.setState({mimeType})
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
    return (
      <React.Fragment>
        <section>
          <p>Choose which semester you want to modify:</p>
          <RadioGroup options={semesterTarget}
                      default={semesterTarget[0]}
                      updateCurrentSelection={this.updateSemesterTarget} />
        </section>
        <br />
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
        {action && action.needsTargets && <section>
          <Label>Target {this.fileOrFolder(action)} name:</Label>
          <Input placeholder={this.targetPlaceholder(action)} />
        </section>}
        <br />
        {action && action.isFile && <section>
          <p>Choose which file type this is:</p>
          <RadioGroup options={mimeType}
                      updateCurrentSelection={this.updateMimeType} />
        </section>}
        <section>
          <Button handleClick={this.submit}>Submit</Button>
        </section>
      </React.Fragment>
    )
  }
}

export default AdminView