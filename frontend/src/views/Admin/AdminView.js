// @flow
import * as React from 'react'
import { Button, CheckboxGroup, Input, InputGroup, RadioGroup } from 'components'
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
  updateSourcePath: string => void,
  submit: () => void,
}

const fileOrFolder = (action: Action): string => (
  action.isFile ? 'file' : 'folder'
)

const sourcePlaceholder = (action: Action): string => (
  action.isFile ? 'Templates/RSVP Template' : 'Leadership/Retreat 1'
)

const targetPlaceholder = (action: Action): string => (
  action.isFile ? 'RSVP Template' : 'Training'
)

const AdminView = ({
                     targetFolders,
                     action,
                     defaultSemesterTarget,
                     updateSemesterTarget,
                     updateAction,
                     updateFolderTargets,
                     updateMimeType,
                     submit,
                     updateSourcePath,
                   }: Props) => (
  <React.Fragment>
    <RadioGroup options={semesterTargetOptions}
                default={defaultSemesterTarget}
                label='Choose which semester you want to modify:'
                updateCurrentSelection={updateSemesterTarget} />
    <RadioGroup options={actionOptions}
                label={'Choose which action you\'d like to take:'}
                updateCurrentSelection={updateAction} />
    <CheckboxGroup options={targetFolders}
                   label='Choose which groups you would like to apply the action to:'
                   updateCurrentChecked={updateFolderTargets} />
    {action && action.needsGlobalSource && <InputGroup label={'Paths begin from the semesters\'s root folder.'}>
      <Input placeholder={sourcePlaceholder(action)}
             label={`Source ${fileOrFolder(action)} name:`}
             updateCurrentValue={updateSourcePath} />
    </InputGroup>
    }
    {action && action.needsFolderSource && <InputGroup label={'Paths begin from the group\'s own folder.'}>
      {targetFolders
        .filter((targetFolder: FolderTarget) => targetFolder.checked)
        .map((targetFolder: FolderTarget, index: number) => (
          <Input key={index}
                 placeholder={targetPlaceholder(action)}
                 label={`Source ${fileOrFolder(action)} name - ${targetFolder.label}: `} />
        ))}
    </InputGroup>}
    {action && <InputGroup label={'Paths begin from the group\'s own folder.'}>
      {targetFolders
        .filter((targetFolder: FolderTarget) => targetFolder.checked)
        .map((targetFolder: FolderTarget, index: number) => (
          <Input key={index}
                 placeholder={targetPlaceholder(action)}
                 label={`Target ${fileOrFolder(action)} name - ${targetFolder.label}:`} />
        ))}
    </InputGroup>}
    {action && action.isFile && <RadioGroup options={mimeTypeOptions}
                                            label='Choose which file type this is:'
                                            updateCurrentSelection={updateMimeType} />}
    <Button handleClick={submit}>Submit</Button>
  </React.Fragment>
)

export default AdminView