// @flow
import * as React from 'react'
import {Footer, Header, ParticipationView} from 'components'
import {LoginViewContainer} from 'containers'
import type {Student} from 'flow/types'
import s from './AppView.module.css'

type Props = {
  isLoggedIn: boolean,
  student: ?Student,
  resetState: () => void,
  login: (Student) => void
}

const App = ({isLoggedIn, student, login, resetState}: Props) => (
  <div className={s.app}>
    <Header />
    <div className={s.body}>
      {isLoggedIn ? <ParticipationView student={student} resetState={resetState} /> :
        <LoginViewContainer login={login} />}
    </div>
    <Footer />
  </div>
);

export default App