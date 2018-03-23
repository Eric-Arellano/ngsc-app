// @flow
import React from 'react'
import { Link } from 'react-router-dom'
import logo from './logo.png'
import s from './Header.module.css'
import Nav from './Nav'

const Header = () => (
  <header className={s.container}>
    <Link to="/">
      <img src={logo} className={s.logo} alt="logo" />
    </Link>
    {/*<Nav />*/}
    <h1 className={s.title}>NGSC App</h1>
  </header>
)

export default Header