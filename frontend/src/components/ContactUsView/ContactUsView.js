// @flow
import React from 'react'
import {Bio, BioGroup} from 'components'

type Props = {}

const ContactUsView = () => (
        <BioGroup header={"Professional Staff"}>
            <Bio name={"Chris"} position={"member"} email={"ntran11@asu.edu"} pictureURL={"https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-9/26815372_1505477482841281_4162892782714660624_n.jpg?oh=1d246da8e20a909b20410066bdb65d4a&oe=5B10E643"}/>
            <Bio name={"Eric"} position={"Chief of Staff"} email={"eric@asu.edu"} pictureURL={"https://media.licdn.com/media/p/6/005/06f/10d/37f07f4.jpg"}/>
        </BioGroup>
    )

export default ContactUsView