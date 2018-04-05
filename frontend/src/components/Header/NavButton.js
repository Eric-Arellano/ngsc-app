// @flow
import * as React from 'react'
import {Link} from 'react-router-dom'
import s from './NavButton.module.css'

type Props = {
  label: string,
  link: string
}

const NavButton = ({label, link}: Props) => (
  <Link to={link} className={s.container}>
    <p>{label}</p>
  </Link>
)

export default NavButton
