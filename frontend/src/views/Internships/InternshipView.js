//@flow
import React from 'react'
import {Panel} from 'components'
import blackBoardHome from './photos/blackBoardHome.png'
import myOrgs from './photos/myOrgs.png'
import internshipsInfo from './photos/internshipsInfo.png'
import s from './InternshipView.module.css'

const InternshipView = () => (
  <Panel header='Internship Instructions'>
    <p> Check out the NGSC Blackboard Internship page for all of your internship-related questions.
      Here's how to get to the Internship Black Board Page: </p>
    <ol className={s.list}>
      <li>
        <p>Log in to your MyASU and navigate to the Blackboard Home page.</p>
        <img src={blackBoardHome} alt="Blackboard home screen shot" />
      </li>
      <li>
        <p>Scroll all the way to the bottom of the page to the box labeled 'My Organizations'.</p>
        <img src={myOrgs} alt="myOrgs screenshot" />
      </li>
      <li>
        <p>Click on 'Next Generation Service Corps'.</p>
      </li>
      <li>
        <p>Click on 'Internships Info'.</p>
        <img src={internshipsInfo} alt="internships info screen shot" />
      </li>
    </ol>
  </Panel>
)

export default InternshipView