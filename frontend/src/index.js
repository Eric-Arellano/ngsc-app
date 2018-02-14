// react
import React from 'react'
import {render} from 'react-dom'
import {BrowserRouter} from 'react-router-dom'
import {AppContainer} from 'containers'
import './resets.css'

render((
        <BrowserRouter>
            <AppContainer/>
        </BrowserRouter>),
    document.getElementById('root')
)
