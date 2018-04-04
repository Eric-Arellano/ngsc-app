// @flow
import React from 'react'
import s from './Bio.module.css'

type Props = {
  pictureURL: string,
  position: string,
  name: string,
  email: string
}

const Bio = ({pictureURL, position, name, email}: Props) => (
  <div className={s.container}>
    <img src={pictureURL} className={s.image}/>
    <p>{position}</p>
    <p>{name}</p>
    <p>{email}</p>
  </div>
)

export default Bio