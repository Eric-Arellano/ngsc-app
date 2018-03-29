// @flow
import * as React from 'react'
import {Bio} from 'components'
import s from './Bio.module.css'

type Props = {
    header: string,
    children: React.ChildrenArray<React.Element<typeof Bio>>
}

const BioGroup = ({header, children}: Props) => (
    <div>
        <h3>{header}</h3>
        <div className={s.row}>{children}</div>
    </div>
)

export default BioGroup
