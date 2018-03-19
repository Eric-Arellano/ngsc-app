// @flow
import type { CheckboxOption, RadioOption } from 'types'

export const folderTargets: Array<CheckboxOption> = [
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

export const actionList: Array<RadioOption> = [
  {
    label: 'Create empty file',
    needsSource: false,
    needsTarget: true,
    api: '/create/file',
  },
  {
    label: 'Create empty folder',
    needsSource: false,
    needsTarget: true,
    api: '/create/folder',
  },
  {
    label: 'Copy file',
    needsSource: true,
    needsTarget: true,
    api: '/copy/file',
  },
  {
    label: 'Copy folder',
    needsSource: true,
    needsTarget: true,
    api: '/copy/folder',
  },
  {
    label: 'Move file',
    needsSource: true,
    needsTarget: true,
    api: '/move/file',
  },
  {
    label: 'Move folder',
    needsSource: true,
    needsTarget: true,
    api: '/move/folder',
  },
  {
    label: 'Remove file',
    needsSource: false,
    needsTarget: true,
    api: '/remove/file',
  },
  {
    label: 'Remove folder',
    needsSource: false,
    needsTarget: true,
    api: '/remove/folder',
  },
  {
    label: 'Rename file',
    needsSource: false,
    needsTarget: true,
    api: '/rename/file',
  },
  {
    label: 'Rename folder',
    needsSource: false,
    needsTarget: true,
    api: '/rename/folder',
  },
]
