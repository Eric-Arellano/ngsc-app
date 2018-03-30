// @flow
import * as React from 'react'
import {Bio} from 'components'
import s from './BioGroup.module.css'

type Props = {
    header: string,
    children: React.ChildrenArray<React.Element<typeof Bio>>
}

const BioGroup = ({header, children}: Props) => (
    <div>
        <h3 className={s.bold}>{header}</h3>
        <div className={s.wrapper}>{children}</div>
    </div>
)

export default BioGroup
