// @flow
import React from 'react'
import logo from './logo.png'
import s from './Header.module.css'

const Header = () => (
  <header className={s.container}>
    <a href="/">
      <img src={logo} className={s.logo} alt="logo" />
    </a>
    <h1 className={s.title}>NGSC Engagement Requirements</h1>
  </header>
)

export default Header