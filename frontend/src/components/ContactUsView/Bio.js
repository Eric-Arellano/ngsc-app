// @flow
import React from 'react'

type Props = {
    pictureURL: string,
    position: ?string,
    name: string,
    email: string
}

const Bio = ({pictureURL, position, name, email}: Props) => (
        <div>
            <img src={pictureURL}/>
            <p>{position}</p>
            <p>{name}</p>
            <p>{email}</p>
        </div>
    )

export default Bio