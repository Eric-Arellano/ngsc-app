// @flow

import type { Name } from 'types'

export type BioType = {
  name: Name,
  position: string,
  email: string,
  photoUrl: string,
}

export type BioGroupType = {
  group: string,
  bios: Array<Bio>,
}