// @flow
import type { CheckboxOption, RadioOption } from 'types'

// -------------------------------------------
// Semester Target
// -------------------------------------------

export type SemesterTarget = RadioOption

export const semesterTargetOptions: Array<SemesterTarget> = [
  {
    label: 'Current semester',
  },
  {
    label: 'Next semester'
  }
]

// -------------------------------------------
// Folder Target
// -------------------------------------------

export type FolderTarget = CheckboxOption & {
  sourcePath: ?string,
  targetPath: ?string,
}

export const folderTargetOptions: Array<FolderTarget> = [
  {
    label: 'Committee chair folders',
    checked: true,
    sourcePath: null,
    targetPath: null,
  },
  {
    label: 'Committee lead folders',
    checked: true,
    sourcePath: null,
    targetPath: null,
  },
  {
    label: 'Mission team folders',
    checked: true,
    sourcePath: null,
    targetPath: null,
  },
  {
    label: 'Section lead folders',
    checked: true,
    sourcePath: null,
    targetPath: null,
  },
]

// -------------------------------------------
// Semester Target
// -------------------------------------------

export type MimeType = RadioOption & {
  needsExtension: boolean,
}

export const mimeTypeOptions: Array<MimeType> = [
  {
    label: 'Google Doc',
    needsExtension: false,
  },
  {
    label: 'Google Sheet',
    needsExtension: false,
  },
  {
    label: 'Google Slides',
    needsExtension: false,
  },
  {
    label: 'Google Form',
    needsExtension: false,
  },
  {
    label: 'Other',
    needsExtension: true,
  }
]

// -------------------------------------------
// Action
// -------------------------------------------

export type Action = RadioOption & {
  isFile: boolean,
  needsGlobalSource: boolean,  // i.e. source can come from anywhere
  needsFolderSource: boolean,  // i.e. source comes from within FolderTarget
  api: string,
}

export const actionOptions: Array<Action> = [
  {
    label: 'Create empty file',
    isFile: true,
    needsGlobalSource: false,
    needsFolderSource: false,
    api: '/create/file',
  },
  {
    label: 'Create empty folder',
    isFile: false,
    needsGlobalSource: false,
    needsFolderSource: false,
    api: '/create/folder',
  },
  {
    label: 'Copy file',
    isFile: true,
    needsGlobalSource: true,
    needsFolderSource: false,
    api: '/copy/file',
  },
  {
    label: 'Move file',
    isFile: true,
    needsGlobalSource: false,
    needsFolderSource: true,
    api: '/move/file',
  },
  {
    label: 'Move folder',
    isFile: false,
    needsGlobalSource: false,
    needsFolderSource: true,
    api: '/move/folder',
  },
  {
    label: 'Remove file',
    isFile: true,
    needsGlobalSource: false,
    needsFolderSource: false,
    api: '/remove/file',
  },
  {
    label: 'Remove folder',
    isFile: false,
    needsGlobalSource: false,
    needsFolderSource: false,
    api: '/remove/folder',
  },
  {
    label: 'Rename file',
    isFile: true,
    needsGlobalSource: false,
    needsFolderSource: true,
    api: '/rename/file',
  },
  {
    label: 'Rename folder',
    isFile: false,
    needsGlobalSource: false,
    needsFolderSource: true,
    api: '/rename/folder',
  },
]
