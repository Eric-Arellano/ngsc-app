// @flow
import * as React from 'react'
import { Link } from 'react-router-dom'
import s from './NavButton.module.css'

type Props = {
    children: React.Node,  // can be any valid react element, e.g. array of Entry
    link: string
}
const NavButton = ({children, link}: Props) => (
    <li className={s.container}>
        <Link to= {link}>{children}</Link>
    </li>
)

export default NavButton

/*// children is between tags, input children to be type on button*/



