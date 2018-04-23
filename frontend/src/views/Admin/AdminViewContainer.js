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
  sourcePath: ?string,
  targetPaths: ?Array<string>,
  mimeType: ?MimeType,
}

class AdminViewContainer extends React.Component<Props, State> {

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

  render () {
    const {action, targetFolders, semesterTarget} = this.state
    const {updateSemesterTarget, updateAction, updateFolderTargets, updateMimeType, submit} = this
    return <AdminView action={action}
                      targetFolders={targetFolders}
                      defaultSemesterTarget={semesterTarget}
                      updateSemesterTarget={updateSemesterTarget}
                      updateAction={updateAction}
                      updateFolderTargets={updateFolderTargets}
                      updateMimeType={updateMimeType}
                      submit={submit}
    />
  }
}

export default AdminViewContainer