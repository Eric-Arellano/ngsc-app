// @flow
import * as React from 'react'
import { Bio, BioGroup, Footer, Header, ParticipationView } from 'components'
import { LoginViewContainer } from 'containers'
import type { Student } from 'flow/types'
import s from './App.module.css'

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
        <BioGroup header={"Professional Staff"}>
            <Bio name={"Chris"} position={"member"} email={"ntran11@asu.edu"} pictureURL={"https://scontent.fphx1-1.fna.fbcdn.net/v/t1.0-9/26815372_1505477482841281_4162892782714660624_n.jpg?oh=1d246da8e20a909b20410066bdb65d4a&oe=5B10E643"}/>
            <Bio name={"Eric"} position={"Chief of Staff"} email={"eric@asu.edu"} pictureURL={"https://media.licdn.com/media/p/6/005/06f/10d/37f07f4.jpg"}/>
        </BioGroup>
    </div>
    <Footer />
  </div>
)

export default App