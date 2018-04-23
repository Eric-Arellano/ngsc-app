// @flow
import * as React from 'react'
import { Button, CheckboxGroup, Input, Label, RadioGroup } from 'components'
import type { Action, FolderTarget, MimeType, SemesterTarget } from './options'
import { actionOptions, folderTargetOptions, mimeTypeOptions, semesterTargetOptions } from './options'

type Props = {}

type State = {
  semesterTarget: SemesterTarget,
  targetFolders: Array<FolderTarget>,
  action: ?Action,
  sourcePath: ?string,
  targetPaths: ?Array<string>,
  mimeType: ?MimeType,
}

class AdminView extends React.Component<Props, State> {

  state = {
    semesterTarget: semesterTargetOptions[0],
    targetFolders: folderTargetOptions,
    action: null,
    sourcePath: null,
    targetPaths: null,
    mimeType: null,
  }

  updateSemesterTarget = (semesterTarget: SemesterTarget): void => {
    this.setState({semesterTarget})
  }

  updateAction = (action: Action): void => {
    this.setState({action})
  }

  updateFolderTargets = (targetFolders: Array<FolderTarget>): void => {
    this.setState({targetFolders})
  }

  updateSourcePath = (sourcePath: string): void => {
    this.setState({sourcePath})
  }

  updateTargetPaths = (targetPaths: Array<string>): void => {
    this.setState({targetPaths})
  }

  updateMimeType = (mimeType: MimeType): void => {
    this.setState({mimeType})
  }

  submit = () => {

  }

  fileOrFolder = (action: Action): string => (
    action.isFile ? 'file' : 'folder'
  )

  sourcePlaceholder = (action: Action): string => (
    action.isFile ? 'Leadership/Example.gslides' : 'Leadership/Retreat 1'
  )

  targetPlaceholder = (action: Action): string => (
    action.isFile ? 'Example.gslides' : 'Retreat 1'
  )

  render () {
    const {action, targetFolders, semesterTarget} = this.state
    return (
      <React.Fragment>
        <section>
          <p>Choose which semester you want to modify:</p>
          <RadioGroup options={semesterTargetOptions}
                      default={semesterTarget}
                      updateCurrentSelection={this.updateSemesterTarget} />
        </section>
        <br />
        <section>
          <p>Choose which action you'd like to take:</p>
          <RadioGroup options={actionOptions}
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
          <RadioGroup options={mimeTypeOptions}
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