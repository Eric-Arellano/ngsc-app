// @flow

import type { Name } from 'types'

export type Bio = {
  name: Name,
  position: string,
  email: string,
  photoUrl: string,
}

export type BioGroup = {
  group: string,
  bios: Array<Bio>,
}