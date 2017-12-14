// @flow
import React from 'react'
import logo from './logo.png'
import './Header.css'

const Header = () => (
  <header className="header">
    <a href="/">
      <img src={logo} className="logo" alt="logo" />
    </a>
    <h1 className="title">NGSC Engagement Requirements</h1>
  </header>
)

export default Header