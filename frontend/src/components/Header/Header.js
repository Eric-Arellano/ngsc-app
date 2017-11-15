// @flow
import React from 'react';
import logo from 'logo.png';
import './style.css';

const Header = () => (
  <header className="App-header">
      <a href="/">
          <img src={logo} className="App-logo" alt="logo"/>
      </a>
    <h1 className="App-title">NGSC Engagement Requirements</h1>
  </header>
);

export default Header;