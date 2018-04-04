//@flow
import React from 'react'
import { Panel } from 'components'
//import s from './InternshipView.module.css'

const InternshipView = () => (
  <div>
    <Panel> //look at how to use this
      <h1> Internship Information </h1>
      <h2> Check out the NGSC Blackboard Internship page for all of your internship related questions.
        How to get to the Internship Black Board Page: </h2>
      <h3>
        1. Log in to your MyASU and navigate to the Blackboard Home page.
        //insert BB home page pi
        2. Scroll all the way to the bottom of the page to the box labeled 'My Organizations'.
        3. Click on 'Next Generation Service Corps'.
        4. Click on 'Internships Info'.
        //insert picture 4 of NGSC BB page home
      </h3>
    </Panel>
  </div>
)

export default InternshipView