// @flow

import type {Name} from 'types'

export type BioType = {
  name: Name,
  position: string,
  email: string,
  pictureURL: string,
}

export type BioGroupType = {
  group: string,
  bios: Array<BioType>,
}

export const bioGroupsData: Array<BioGroupType> = [
  {
    group: 'Professional Staff',
    bios: [
      {
        name: {
          first: 'Brett',
          last: 'Hunt'
        },
        position: 'Executive Director',
        email: 'brett.hunt@asu.edu',
        pictureURL: 'https://media.licdn.com/media/p/6/005/06f/10d/37f07f4.jpg'
      },
      {
        name: {
          first: 'Jessica',
          last: 'Eldridge'
        },
        position: 'Assistant Director',
        email: 'jessica.eldridge@asu.edu',
        pictureURL: 'https://media.licdn.com/media/p/2/000/2b4/161/38a250d.jpg'
      }
    ]
  },
  {
    group: 'Chief of staff and leads',
    bios: []
  }
]