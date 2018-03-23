// @flow
import React from 'react'
import { Link } from 'react-router-dom'

const Nav = () => (
  <nav>
    <ul>
      <li><Link to={'/'}>Home</Link></li>
      <li><Link to={'/internships'}>Internships</Link></li>
      <li><Link to={'/calendar'}>Calendar</Link></li>
      <li><Link to={'/leadership'}>Leadership</Link></li>
    </ul>
  </nav>
)

export default Nav
