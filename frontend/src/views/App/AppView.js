// @flow
import * as React from 'react'
import {Switch, Route} from 'react-router-dom'
import { Footer, Header, PrivateRoute } from 'components'
import { LoginViewContainer, ParticipationView } from 'views'
import type { Student } from 'types'
import s from './AppView.module.css'

type Props = {
  isLoggedIn: boolean,
  student: ?Student,
  resetState: () => void,
  login: (Student) => void
}

const AppView = ({isLoggedIn, student, login, resetState}: Props) => (
    <div className={s.app}>
        <Header />
        <Switch>
            {/*<PrivateRoute path={'/'} isLoggedIn={isLoggedIn} student={student} resetState={resetState} login={login}/>*/}
            <PrivateRoute path={'/participation'} isLoggedIn={isLoggedIn} student={student} resetState={resetState} login={login}/>
        </Switch>
        <Footer/>
    </div>
)

export default AppView