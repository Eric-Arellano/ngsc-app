// @flow
import * as React from 'react'
import { Header } from 'components'
import { EngagementViewContainer, LoginViewContainer } from 'containers'
import type { Student } from 'flow/types'
import './App.css'

type Props = {
  isLoggedIn: boolean,
  student: ?Student,
  resetState: () => void,
  login: (Student) => void
}

const App = (props: Props) => {
  const {isLoggedIn, student, login, resetState} = props

  return (
    <div className='ngsc-container'>
      <Header />
      <div className='container'>
        {isLoggedIn ? <EngagementViewContainer student={student} /> :
          <LoginViewContainer login={login} resetState={resetState} />}
      </div>
    </div>
  )
}

export default App