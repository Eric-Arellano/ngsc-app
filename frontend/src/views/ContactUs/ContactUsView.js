// @flow
import * as React from 'react'
import Bio from './Bio'
import BioGroup from './BioGroup'
import type { BioGroupType, BioType } from './data'
import { bioGroupsData } from './data'

const ContactUsView = () => (
  <React.Fragment>
    {bioGroupsData.map((bioGroup: BioGroupType) => (
      <BioGroup header={bioGroup.group}>
        {bioGroup.bios.map((bio: BioType) => (
          <Bio name={bio.name}
               position={bio.position}
               email={bio.email}
               pictureURL={bio.pictureURL}
          />
        ))}
      </BioGroup>
    ))}
  </React.Fragment>
)

export default ContactUsView