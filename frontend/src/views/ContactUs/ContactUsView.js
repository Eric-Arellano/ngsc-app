// @flow
import React from 'react'
import Bio from './Bio'
import BioGroup from './BioGroup'
import {bioGroupsData} from './data'
import type {BioGroupType, BioType} from './data'


const ContactUsView = () => (
  <div>
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
  </div>)

export default ContactUsView