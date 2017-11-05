// react
import React from 'react';
import ReactDOM from 'react-dom';
// styles
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/css/bootstrap-theme.css';
import './index.css';
// containers
import App from './containers/App/App';
import registerServiceWorker from './registerServiceWorker';


ReactDOM.render(<App />,
  document.getElementById('root'));

registerServiceWorker();
