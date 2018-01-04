// @flow
import * as React from 'react'
import { Loading } from 'components'
import s from './Panel.module.css'

type Props = {
  children: React.Node,  // can be any valid react element, e.g. array of Entry
  header: string,
  isLoading: boolean
}

const PanelWithLoading = ({children, header, isLoading}: Props) => (
  <div className={s.container}>
    <h3 className={s.header}>{header}</h3>
    {isLoading ? <Loading /> : <div className={s.body}>{children}</div>}
  </div>
)

export default PanelWithLoading