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

export type FolderTarget = CheckboxOption

export const folderTargetOptions: Array<FolderTarget> = [
  {
    label: 'Committee chair folders',
    checked: true
  },
  {
    label: 'Committee lead folders',
    checked: true
  },
  {
    label: 'Mission team folders',
    checked: true
  },
  {
    label: 'Section lead folders',
    checked: true
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
  needsSource: boolean,
  needsTargets: boolean,
  api: string,
}

export const actionOptions: Array<Action> = [
  {
    label: 'Create empty file',
    isFile: true,
    needsSource: false,
    needsTargets: true,
    api: '/create/file',
  },
  {
    label: 'Create empty folder',
    isFile: false,
    needsSource: false,
    needsTargets: true,
    api: '/create/folder',
  },
  {
    label: 'Copy file',
    isFile: true,
    needsSource: true,
    needsTargets: true,
    api: '/copy/file',
  },
  {
    label: 'Move file',
    isFile: true,
    needsSource: true,
    needsTargets: true,
    api: '/move/file',
  },
  {
    label: 'Move folder',
    isFile: false,
    needsSource: true,
    needsTargets: true,
    api: '/move/folder',
  },
  {
    label: 'Remove file',
    isFile: true,
    needsSource: false,
    needsTargets: true,
    api: '/remove/file',
  },
  {
    label: 'Remove folder',
    isFile: false,
    needsSource: false,
    needsTargets: true,
    api: '/remove/folder',
  },
  {
    label: 'Rename file',
    isFile: true,
    needsSource: false,
    needsTargets: true,
    api: '/rename/file',
  },
  {
    label: 'Rename folder',
    isFile: false,
    needsSource: false,
    needsTargets: true,
    api: '/rename/folder',
  },
]
