// @flow
import React from 'react'
import NavButton from './NavButton'
import s from './NavButton.module.css'

const Nav = () => (
    <nav>
        <ul>
            <div className={s.shorten}>
            <NavButton link='./'>Home</NavButton>
            <NavButton link='./internships'>Internships</NavButton>
            <NavButton link='./calendar'>Calendar</NavButton>
            <NavButton link='./leadership'>Leadership</NavButton>
            </div>
        </ul>
    </nav>
)

export default Nav
