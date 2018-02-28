// @flow
import React from 'react'
import {Route} from 'react-router-dom'
import {LoginViewContainer, ParticipationView} from 'views'
import type {Student} from 'types'

type Props = {
    isLoggedIn: boolean,
    login: (Student) => void,
    student: Student,
    resetState: () => void,
    path: string,
}

const PrivateRoute = ({isLoggedIn, login, student, resetState, path}: Props) => (
    <Route exact path={path} render={() => (
        isLoggedIn ? <ParticipationView student={student} resetState={resetState}/> :
            <LoginViewContainer login={login}/>
    )}/>
)

export default PrivateRoute
