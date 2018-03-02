// @flow
import * as React from 'react'
import { Route, Switch } from 'react-router-dom'
import { Footer, Header, PrivateRoute } from 'components'
import { AdminView, LoginViewContainer, ParticipationView } from 'views'
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
      <PrivateRoute exact path='/' isLoggedIn={isLoggedIn} component={ParticipationView} student={student}
                    resetState={resetState} login={login} />
      <Route exact path='/admin' component={AdminView} />
      <Route exact path='/events' component={AdminView} />
      <Route exact path='/leadership' component={AdminView} />
    </Switch>
    <Footer />
  </div>
)

export default AppView