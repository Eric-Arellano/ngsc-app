// @flow
import React from 'react'
import logo from './logo.png'
import Nav from './Nav'
import s from './Header.module.css'

const Header = () => (
  <header className={s.container}>
    <img src={logo} className={s.logo} alt="logo" />
    <Nav />
  </header>
)

export default Header