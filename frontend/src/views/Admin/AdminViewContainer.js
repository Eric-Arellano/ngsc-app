// @flow
import React from 'react'
import AdminView from './AdminView'
import type { Action, FolderTarget, MimeType, SemesterTarget } from './options'
import { folderTargetOptions, semesterTargetOptions } from './options'
import type { ValidationState } from 'types'
import { postRequest } from 'api'

type Props = {}

type State = {
  semesterTarget: SemesterTarget,
  targetFolders: Array<FolderTarget>,
  action: ?Action,
  globalSourcePath: ?string,
  mimeType: ?MimeType,
  validationState: ValidationState,
}

class AdminViewContainer extends React.Component<Props, State> {

  state = {
    semesterTarget: semesterTargetOptions[0],
    targetFolders: folderTargetOptions,
    action: null,
    globalSourcePath: null,
    mimeType: null,
    validationState: 'neutral',
  }

  updateValidationState = () => {
    const {semesterTarget, targetFolders, action, globalSourcePath, mimeType} = this.state
    // predicates
    const semesterChosen = semesterTarget != null
    const actionChosen = action != null
    const targetChecked = targetFolders.some(folder => folder.checked)
    const globalSourceAdded = !(action && action.needsGlobalSource && (globalSourcePath == null || globalSourcePath === ''))
    const folderSourceAdded = !(action && action.needsFolderSource && targetFolders
      .filter(folder => folder.checked)
      .some(folder => folder.sourcePath == null || folder.sourcePath === ''))
    const folderTargetAdded = !(action && targetFolders
      .filter(folder => folder.checked)
      .some(folder => folder.targetPath == null || folder.targetPath === ''))
    const mimeChosen = !(action && action.isFile && mimeType == null)
    // update
    const validationState = semesterChosen && actionChosen && targetChecked && globalSourceAdded && folderSourceAdded && folderTargetAdded && mimeChosen
      ? 'valid' : 'invalid'
    this.setState({validationState})
  }

  updateSemesterTarget = (semesterTarget: SemesterTarget): void => {
    this.setState({semesterTarget}, () => this.updateValidationState())
  }

  updateAction = (action: Action): void => {
    const globalSourcePath = action.needsGlobalSource ? this.state.globalSourcePath : null
    const mimeType = action.isFile ? this.state.mimeType : null
    this.setState({action, globalSourcePath, mimeType}, () => this.updateValidationState())
  }

  updateFolderTargets = (targetFolders: Array<FolderTarget>): void => {
    const resetTargetFolders = targetFolders.map(folder => ({
      ...folder,
      sourcePath: folder.checked ? folder.sourcePath : null,
      targetPath: folder.checked ? folder.targetPath : null
    }))
    this.setState({targetFolders: resetTargetFolders}, () => this.updateValidationState())
  }

  updateGlobalSourcePath = (globalSourcePath: string): void => {
    this.setState({globalSourcePath}, () => this.updateValidationState())
  }

  updateFolderSourcePath = (targetFolder: FolderTarget, path: string): void => {
    const {targetFolders} = this.state
    const index = targetFolders.indexOf(targetFolder)
    const updatedTarget = {...targetFolder, sourcePath: path}
    const updatedTargetFolders = [...targetFolders]
    updatedTargetFolders[index] = updatedTarget
    this.setState({targetFolders: updatedTargetFolders}, () => this.updateValidationState())
  }

  updateFolderTargetPath = (targetFolder: FolderTarget, path: string): void => {
    const {targetFolders} = this.state
    const index = targetFolders.indexOf(targetFolder)
    const updatedTarget = {...targetFolder, targetPath: path}
    const updatedTargetFolders = [...targetFolders]
    updatedTargetFolders[index] = updatedTarget
    this.setState({targetFolders: updatedTargetFolders}, () => this.updateValidationState())
  }

  updateMimeType = (mimeType: MimeType): void => {
    this.setState({mimeType}, () => this.updateValidationState())
  }

  submit = () => {
    const {validationState, semesterTarget, targetFolders, action, globalSourcePath, mimeType} = this.state
    if (validationState === 'valid' && action != null) {
      const payload = this.generatePayload(semesterTarget, targetFolders, action, globalSourcePath, mimeType)
      postRequest(action.api, payload)
    }
  }

  generatePayload = (semesterTarget: SemesterTarget,
                     targetFolders: Array<FolderTarget>,
                     action: Action,
                     globalSourcePath: ?string,
                     mimeType: ?MimeType) => (
    {
      semester: semesterTarget.apiId,
      targetFolders: targetFolders
        .filter(folder => folder.checked)
        .map(folder => ({
          apiId: folder.apiId,
          targetPath: folder.targetPath,
          // $FlowFixMe
          ...(action.needsFolderSource && {sourcePath: folder.sourcePath})
        })),
      // $FlowFixMe
      ...(action.needsGlobalSource && {globalSourcePath: globalSourcePath}),
      // $FlowFixMe
      ...(action.isFile && mimeType && {mimeType: mimeType.apiId})
    })

  render () {
    return <AdminView {...this.state}
                      defaultSemesterTarget={this.state.semesterTarget}
                      updateSemesterTarget={this.updateSemesterTarget}
                      updateAction={this.updateAction}
                      updateCheckedFolderTargets={this.updateFolderTargets}
                      updateMimeType={this.updateMimeType}
                      updateGlobalSourcePath={this.updateGlobalSourcePath}
                      updateFolderSourcePath={this.updateFolderSourcePath}
                      updateFolderTargetPath={this.updateFolderTargetPath}
                      submit={this.submit}
    />
  }
}

export default AdminViewContainer