import React from 'react'
import TwitterOutline from 'react-icons/lib/io/social-twitter-outline'
import TwitterFull from 'react-icons/lib/io/social-twitter'
import FacebookOutline from 'react-icons/lib/io/social-facebook-outline'
import FacebookFull from 'react-icons/lib/io/social-facebook'
import InstagramOutline from 'react-icons/lib/io/social-instagram-outline'
import InstagramFull from 'react-icons/lib/io/social-instagram'

import s from './Social.module.css'

const Social = () => (
  <section className={s.container}>
    <a className={s.link} href='https://twitter.com/ASU_PSAJobs' title='ASU_PSAJobs | twitter'>
      <span className={s.iconFull}><TwitterFull size={40} /></span>
      <span className={s.iconOutline}><TwitterOutline size={40} /></span>
    </a>
    <a className={s.link} href='https://www.instagram.com/ngscsocial/' title='ngscsocial | instagram'>
      <span className={s.iconFull}><InstagramFull size={40} /></span>
      <span className={s.iconOutline}><InstagramOutline size={40} /></span>
    </a>
    <a className={s.link} href='https://www.facebook.com/groups/NGSC2015' title='NGSC2015 | facebook'>
      <span className={s.iconFull}><FacebookFull size={40} /></span>
      <span className={s.iconOutline}><FacebookOutline size={40} /></span>
    </a>
  </section>
)

export default Social