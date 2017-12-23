// @flow
import React from 'react'
// import type { Student } from 'flow/types'
import { Entry, Panel } from 'components'

type Props = {
    noShows: number,
    mt_percent: str,
    com_percent: str
}

const Attendance = (props: Props) => {
    return (
        <Panel header='Attendance'>
            <Entry>No-shows: {props.noShows}</Entry>
            <Entry>Mission Team Percent: {props.mt_percent}</Entry>
            <Entry>Committee Percent: {props.com_percent}</Entry>
            <p><em>
                * No-shows indicate the number of times that you have RSVPed that you will be attending an event but did
                not sign in on our records. If you need to dispute this number, please let e-mail the Admin chair.
            </em></p>
        </Panel>
    )
}

export default Attendance
