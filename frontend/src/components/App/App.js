// @flow
import * as React from 'react'
import {Switch, Route} from 'react-router-dom'
import {Footer, Header, ParticipationView} from 'components'
import {LoginViewContainer} from 'containers'
import type {Student} from 'flow/types'
import s from './App.module.css'

type Props = {
    isLoggedIn: boolean,
    student: ?Student,
    resetState: () => void,
    login: (Student) => void
}

const App = ({isLoggedIn, student, login, resetState}: Props) => (
    <div className={s.app}>
        <Header/>
        <Switch>
            <Route exact path='/' render={() => (
                <LoginViewContainer login={login}/>)}/>
            <Route exact path='/participation' render={() => (
                <ParticipationView student={student} resetState={resetState}/>)}/>
        </Switch>
        {/*<div className={s.body}>*/}
        {/*{isLoggedIn ? <ParticipationView student={student} resetState={resetState} /> :*/}
        {/*<LoginViewContainer login={login} />}*/}
        {/*</div>*/}
        <Footer/>
    </div>
)

export default App