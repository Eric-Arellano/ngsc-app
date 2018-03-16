// react
import React from 'react'
import { render } from 'react-dom'
import {BrowserRouter} from 'react-router-dom'
import { AppViewContainer } from 'views'
import './resets.css'

render((
        <BrowserRouter>
            <AppViewContainer/>
        </BrowserRouter>),
    document.getElementById('root')
)
