// @flow
import * as React from 'react'
import { Button, CheckboxGroup, Input, InputGroup, RadioGroup } from 'components'
import type { Action, FolderTarget, MimeType, SemesterTarget } from './options'
import { actionOptions, mimeTypeOptions, semesterTargetOptions } from './options'
import type { ValidationState } from 'types'
import s from './AdminView.module.css'

type Props = {
  targetFolders: Array<FolderTarget>,
  action: ?Action,
  defaultSemesterTarget: SemesterTarget,
  updateSemesterTarget: SemesterTarget => void,
  updateAction: Action => void,
  updateCheckedFolderTargets: Array<FolderTarget> => void,
  updateMimeType: MimeType => void,
  updateGlobalSourcePath: string => void,
  updateFolderSourcePath: (FolderTarget, string) => void,
  updateFolderTargetPath: (FolderTarget, string) => void,
  submit: () => void,
  validationState: ValidationState,
  isLoading: boolean,
  isError: boolean
}

// ----------------------------------------------------------------------------
// Utils
// ----------------------------------------------------------------------------

const fileOrFolder = (action: Action): string => (
  action.isFile ? 'file' : 'folder'
)

const sourcePlaceholder = (action: Action): string => (
  action.isFile ? 'Templates/RSVP Template' : 'Leadership/Retreat 1'
)

const targetPlaceholder = (action: Action): string => (
  action.isFile ? 'RSVP Template' : 'Training'
)

// ----------------------------------------------------------------------------
// Form components
// ----------------------------------------------------------------------------

const instructions = () => (
  <div className={s.instructions}>
    <p>This tool allows you to perform bulk operations on the Google Drive, e.g. copying a file into every mission team
      leader's folder.</p>
    <p>Follow the below prompts. After you select an option, the form will update to ask you the questions it needs to
      know to work.</p>
    <p>When inputting the name of a file or folder, input the name exactly as it appears in Google Drive, and do not
      include the file extension.
      For example, the Google Form "RSVP Template" should be entered as "RSVP Template".</p>
    <p>Every file and folder has a <em>parent folder</em>.
      You can only input files and folders that belong to that parent. For example, you cannot reference a file from
      last semester, because the tool won't be able to find that file.</p>
    <p>The parent folder depends on which command you choose.
      If the prompt says "the semester root", this means the parent is that semester's folder, e.g. 'Fall 2019',
      and you can access anything within that semester's folder.
      Otherwise, the parent will be the folder for the group you are targeting. For example, if you performing an action
      on Mission Team Folders, then the parent folder will be each individual mission team's folder, e.g. "Mission Team
      1" and "Mission Team 28".</p>
    <p>If you want to specify a file or folder that is nested within the parent, specify the file path by using a '/'
      to indicate folders. For example, if you want to specify the presentation 'Attendance Training' saved in the
      'Leadership' folder, input 'Leadership/Attendance Training'.</p>
  </div>
)

const semesterTargetQuestion = (updateSemesterTarget: (SemesterTarget => void),
                                defaultSemesterTarget: SemesterTarget) => (
  <RadioGroup options={semesterTargetOptions}
              default={defaultSemesterTarget}
              label='Choose which semester you want to modify:'
              updateCurrentSelection={updateSemesterTarget} />
)

const actionQuestion = (updateAction) => (
  <RadioGroup options={actionOptions}
              label={'Choose which action you\'d like to take:'}
              updateCurrentSelection={updateAction} />
)

const targetFoldersQuestion = (targetFolders, updateCheckedFolderTargets) => (
  <CheckboxGroup options={targetFolders}
                 label='Choose which groups you would like to apply the action to:'
                 updateCurrentChecked={updateCheckedFolderTargets} />
)

const globalSourceQuestion = (action, updateGlobalSourcePath) => (
  <React.Fragment>
    {action && action.needsGlobalSource && <InputGroup label={'Paths begin from the semesters\'s root folder.'}>
      <Input placeholder={sourcePlaceholder(action)}
             label={`Source ${fileOrFolder(action)} name:`}
             updateCurrentValue={updateGlobalSourcePath} />
    </InputGroup>
    }
  </React.Fragment>
)

const folderSourceQuestion = (action, targetFolders, updateFolderSourcePath) => (
  <React.Fragment>
    {action && action.needsFolderSource && <InputGroup label={'Paths begin from the group\'s own folder.'}>
      {targetFolders
        .filter((folder: FolderTarget) => folder.checked)
        .map((folder: FolderTarget) => {
          const updateFolderPath = (path: string) => updateFolderSourcePath(folder, path)
          return <Input key={targetFolders.indexOf(folder)}
                        placeholder={targetPlaceholder(action)}
                        label={`Source ${fileOrFolder(action)} name - ${folder.label}: `}
                        updateCurrentValue={updateFolderPath} />
          }
        )}
    </InputGroup>}
  </React.Fragment>
)

const folderTargetQuestion = (action, targetFolders, updateFolderTargetPath) => (
  <React.Fragment>
    {action && <InputGroup label={'Paths begin from the group\'s own folder.'}>
      {targetFolders
        .filter((folder: FolderTarget) => folder.checked)
        .map((folder: FolderTarget) => {
          const updateFolderPath = (path: string) => updateFolderTargetPath(folder, path)
          return <Input key={targetFolders.indexOf(folder)}
                        placeholder={targetPlaceholder(action)}
                        label={`Target ${fileOrFolder(action)} name - ${folder.label}:`}
                        updateCurrentValue={updateFolderPath} />
          }
        )}
    </InputGroup>}
  </React.Fragment>
)

const mimeTypeQuestion = (action, updateMimeType) => (
  <React.Fragment>
    {action && action.isFile && <RadioGroup options={mimeTypeOptions}
                                            label='Choose which file type this is:'
                                            updateCurrentSelection={updateMimeType} />}
  </React.Fragment>
)

const submitButton = (submit, validationState) => {
  const isSubmitDisabled = validationState !== 'valid'
  return (
    <Button disabled={isSubmitDisabled} handleClick={submit}>
      {'Submit'}
    </Button>
  )
}

// ----------------------------------------------------------------------------
// Form
// ----------------------------------------------------------------------------

const AdminView = ({
                     targetFolders,
                     action,
                     defaultSemesterTarget,
                     updateSemesterTarget,
                     updateAction,
                     updateCheckedFolderTargets,
                     updateMimeType,
                     submit,
                     updateGlobalSourcePath,
                     updateFolderSourcePath,
                     updateFolderTargetPath,
                     validationState,
                   }: Props) => (
  <React.Fragment>
    <h2>Admin Google Drive tool</h2>
    {instructions()}
    {semesterTargetQuestion(updateSemesterTarget, defaultSemesterTarget)}
    {actionQuestion(updateAction)}
    {targetFoldersQuestion(targetFolders, updateCheckedFolderTargets)}
    {globalSourceQuestion(action, updateGlobalSourcePath)}
    {folderSourceQuestion(action, targetFolders, updateFolderSourcePath)}
    {folderTargetQuestion(action, targetFolders, updateFolderTargetPath)}
    {mimeTypeQuestion(action, updateMimeType)}
    {submitButton(submit, validationState)}
  </React.Fragment>
)

export default AdminView