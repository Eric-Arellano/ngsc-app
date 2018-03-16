// @flow
import React from 'react'
import {Link} from 'react-router-dom'

const Nav = () => (
    /*<Nav className={s.app}>*/
    <nav>
        <ul>
            <li><Link to={'/'}>Home</Link></li>
            <li><Link to={'/participation'}>Participation</Link></li>
            {/*<li><Link to={'/calendar'}>Calendar</Link></li>*/}
            {/*<li><Link to={'/leadership'}>Leadership</Link></li>*/}
            {/*<li><Link to={'/contact-us'}>Contact Us</Link></li>*/}
        </ul>

    </nav>
// </Nav>
)
export default Nav


