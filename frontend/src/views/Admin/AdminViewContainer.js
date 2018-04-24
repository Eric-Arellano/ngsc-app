// @flow
import React from 'react'
import AdminView from './AdminView'
import type { Action, FolderTarget, MimeType, SemesterTarget } from './options'
import { folderTargetOptions, semesterTargetOptions } from './options'

type Props = {}

type State = {
  semesterTarget: SemesterTarget,
  targetFolders: Array<FolderTarget>,
  action: ?Action,
  globalSourcePath: ?string,
  mimeType: ?MimeType,
}

class AdminViewContainer extends React.Component<Props, State> {

  state = {
    semesterTarget: semesterTargetOptions[0],
    targetFolders: folderTargetOptions,
    action: null,
    globalSourcePath: null,
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

  updateGlobalSourcePath = (globalSourcePath: string): void => {
    this.setState({globalSourcePath})
  }

  updateFolderSourcePath = (targetFolder: FolderTarget, path: string): void => {
    const {targetFolders} = this.state
    const index = targetFolders.indexOf(targetFolder)
    const updatedTarget = {...targetFolder, targetPath: path}
    const updatedTargetFolders = [...targetFolders]
    updatedTargetFolders[index] = updatedTarget
    this.setState({targetFolders: updatedTargetFolders})
  }

  updateFolderTargetPath = (targetFolder: FolderTarget, path: string): void => {
    const {targetFolders} = this.state
    const index = targetFolders.indexOf(targetFolder)
    const updatedTarget = {...targetFolder, targetPath: path}
    const updatedTargetFolders = [...targetFolders]
    updatedTargetFolders[index] = updatedTarget
    this.setState({targetFolders: updatedTargetFolders})
  }

  updateMimeType = (mimeType: MimeType): void => {
    this.setState({mimeType})
  }

  submit = () => {

  }

  render () {
    const {action, targetFolders, semesterTarget} = this.state
    return <AdminView action={action}
                      targetFolders={targetFolders}
                      defaultSemesterTarget={semesterTarget}
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