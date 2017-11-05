import React from 'react';
import logo from '../../logo.png';
import './App.css';

import IDInput from './../../components/IDInput/IDInput';

const App = () => {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo"/>
        <h1 className="App-title">NGSC Engagement Requirements</h1>
      </header>
      <IDInput/>
    </div>
  );
};

export default App;
