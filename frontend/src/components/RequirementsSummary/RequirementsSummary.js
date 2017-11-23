// @flow
import React from 'react';
import { Panel } from 'react-bootstrap';

type Props = {
  service: number,
  civilMil: number
}

const RequirementsSummary = (props: Props) => (
  <Panel header={"Accepted Requirements"} bsStyle={"info"} className="ngsc">
    <span>Accepted # of service hours: {props.service}</span>
    <br/>
    <span>Accepted # of Civil Mil: {props.civilMil}</span>
  </Panel>
);

export default RequirementsSummary;