// @flow
import * as React from 'react'
import { Footer, Header } from 'components'
import { LoginViewContainer, ParticipationView, EventsView } from 'views'
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
    <div className={s.body}>
      {isLoggedIn ? <ParticipationView student={student} resetState={resetState} /> :
        <LoginViewContainer login={login} />}
    </div>
      <EventsView />
    <Footer />
  </div>
)

export default AppView