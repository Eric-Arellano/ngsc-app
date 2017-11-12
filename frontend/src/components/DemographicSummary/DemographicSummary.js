// @flow
import React from 'react';
import { Panel } from 'react-bootstrap';
import type { Name } from 'flow/types'

type Props = {
  name: Name,
  id: number
}

const DemographicSummary = (props: Props) => {
  const { name, id } = props
  return (
  <Panel header={"Student info"} bsStyle={"info"}>
    <span>Name: {`${name.first} ${name.last}`}</span>
    <br/>
    <span>ID number: {id}</span>
  </Panel>
  )
}

export default DemographicSummary;