// react
import React from 'react'
import { render } from 'react-dom'
import { BrowserRouter } from 'react-router-dom'
import { AppViewContainer } from 'views'

render(
  <BrowserRouter>
    <AppViewContainer/>
  </BrowserRouter>,
  document.getElementById('root')
)
