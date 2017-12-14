// @flow
import React from 'react'
import s from './Footer.module.css'

const Footer = () => (
  <footer className={s.container}>
    <p>Check out upcoming NGSC events at the&nbsp;
      <a href="https://psa.asu.edu/next-generation-service-corps/student-portal">student portal.</a>
    </p>
    <p>Made with love by the Admin Committee. {`🤓💪`}</p>
  </footer>
)

export default Footer