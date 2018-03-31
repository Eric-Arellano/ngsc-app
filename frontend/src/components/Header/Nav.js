// @flow
import React from 'react'
import NavButton from './NavButton'

const Nav = () => (
    <nav>
        <ul>
            <NavButton link = './'>Home</NavButton>
            <NavButton link = './internships'>Internships</NavButton>
            <NavButton link = './calendar'>Calendar</NavButton>
            <NavButton link = './leadership'>Leadership</NavButton>
            {/*<li ><Link to={'/'}>Home</Link></li>*/}
            {/*<li><Link to={'/internships'}>Internships</Link></li>*/}
            {/*<li><Link to={'/calendar'}>Calendar</Link></li>*/}
            {/*<li><Link to={'/leadership'}>Leadership</Link></li>*/}
        </ul>
    </nav>
)

export default Nav
