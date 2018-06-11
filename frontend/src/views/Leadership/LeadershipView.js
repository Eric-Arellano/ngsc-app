// @flow
import * as React from 'react'
import Bio from './Bio'
import BioGroup from './BioGroup'
import type { BioGroupType, BioType } from './data'
import { bioGroupsData } from './data'

const LeadershipView = () => (
  <React.Fragment>
    {bioGroupsData.map((bioGroup: BioGroupType, index: number) => (
      <BioGroup header={bioGroup.group} key={index}>
        {bioGroup.bios.map((bio: BioType, bioIndex: number) => (
          <Bio name={bio.name}
               position={bio.position}
               email={bio.email}
               pictureURL={bio.pictureURL}
               key={bioIndex}
          />
        ))}
      </BioGroup>
    ))}
  </React.Fragment>
)

export default LeadershipView