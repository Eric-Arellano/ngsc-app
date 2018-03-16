// @flow
import React from 'react'
import { Link } from 'react-router-dom'
import logo from './logo.png'
import s from './Header.module.css'
import Nav from './Header'

const Header = () => (
  <header className={s.container}>
    <Link to="/">
      <img src={logo} className={s.logo} alt="logo" />
    </a>
      <Nav />
      {/*<nav>*/}
          {/*<ul>*/}

              {/*<li><Link to={'/'}>Home</Link></li>*/}
              {/*<li><Link to={'/participation'}>Participation</Link></li>*/}
              {/*/!*<li><Link to={'/calendar'}>Calendar</Link></li>*!/*/}
              {/*/!*<li><Link to={'/leadership'}>Leadership</Link></li>*!/*/}
              {/*/!*<li><Link to={'/contact-us'}>Contact Us</Link></li>*!/*/}
              {/*</ul>*/}
      {/*</nav>*/}
    <h1 className={s.title}>NGSC App</h1>
  </header>
)

export default Header