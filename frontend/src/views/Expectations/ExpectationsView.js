//@flow
import React from 'react'
import { Panel } from 'components'
// import s from './InternshipView.module.css'

const ExpectationsView = () => (
  <React.Fragment>
    <Panel header='Participation Expectations'>
      <p> These expectations are every semester. </p>
      {/*<ol className={s.list}>*/}
      <li>1 civil-mil event</li>
      <li>4 service hours</li>
      <li>4 NGSC Hours</li>
      <li>Attend On Leadership Seminars and Fall retreat</li>
      <li>Attend the majority of your mission team meetings</li>
      <li>Attend the majority of your committee meetings (first 1.5 years)</li>
      {/*</ol>*/}
    </Panel>
    <Panel header='Academic Expectations'>
    </Panel>
    <Panel header='Internship Expectations'>
    </Panel>
    <Panel header='Student leadership'>
    </Panel>
  </React.Fragment>

)

export default ExpectationsView