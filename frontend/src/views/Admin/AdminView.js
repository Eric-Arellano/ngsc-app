// @flow
import * as React from 'react'
import { Button, CheckboxGroup, Input, Label, RadioGroup } from 'components'
import type { Action, FolderTarget, MimeType, SemesterTarget } from './options'
import { actionOptions, mimeTypeOptions, semesterTargetOptions } from './options'

type Props = {
  targetFolders: Array<FolderTarget>,
  action: ?Action,
  defaultSemesterTarget: SemesterTarget,
  updateSemesterTarget: SemesterTarget => void,
  updateAction: Action => void,
  updateFolderTargets: Array<FolderTarget> => void,
  updateMimeType: MimeType => void,
  submit: () => void
}

const fileOrFolder = (action: Action): string => (
  action.isFile ? 'file' : 'folder'
)

const sourcePlaceholder = (action: Action): string => (
  action.isFile ? 'Leadership/Example.gslides' : 'Leadership/Retreat 1'
)

const targetPlaceholder = (action: Action): string => (
  action.isFile ? 'Example.gslides' : 'Retreat 1'
)

const AdminView = ({targetFolders, action, defaultSemesterTarget, updateSemesterTarget, updateAction, updateFolderTargets, updateMimeType, submit}: Props) => (
  <React.Fragment>
    <div>
      <p>Choose which semester you want to modify:</p>
      <RadioGroup options={semesterTargetOptions}
                  default={defaultSemesterTarget}
                  updateCurrentSelection={updateSemesterTarget} />
    </div>
    <div>
      <p>Choose which action you'd like to take:</p>
      <RadioGroup options={actionOptions}
                  updateCurrentSelection={updateAction} />
    </div>
    <div>
      <p>Choose which groups you would like to apply the action to:</p>
      <CheckboxGroup options={targetFolders}
                     updateCurrentChecked={updateFolderTargets} />
    </div>
    {action && action.needsSource && <div>
      <Label>Source {fileOrFolder(action)} name:</Label>
      <Input placeholder={sourcePlaceholder(action)} />
    </div>}
    {action && action.needsTargets && <div>
      <Label>Target {fileOrFolder(action)} name:</Label>
      <Input placeholder={targetPlaceholder(action)} />
    </div>}
    {action && action.isFile && <div>
      <p>Choose which file type this is:</p>
      <RadioGroup options={mimeTypeOptions}
                  updateCurrentSelection={updateMimeType} />
    </div>}
    <div>
      <Button handleClick={submit}>Submit</Button>
    </div>
  </React.Fragment>
)

export default AdminView