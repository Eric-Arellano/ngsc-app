// @flow
import React from 'react'
import s from './Footer.module.css'
import {Social} from 'components'

const Footer = () => (
  <footer className={s.container}>
    <p>Check out upcoming NGSC events at the&nbsp;
      <a href="https://psa.asu.edu/next-generation-service-corps/student-portal" target="_blank">student
        portal</a>.
    </p>
    <Social />
  </footer>
)

export default Footer
