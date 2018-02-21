// @flow
import * as React from 'react'
import {Bio} from 'components'

type Props = {
    header: string,
    children: React.ChildrenArray<React.Element<typeof Bio>>
}

const BioGroup = ({header, children}: Props) => (
    <div>
        <h3>{header}</h3>
        <div>{children}</div>
    </div>
)

export default BioGroup
