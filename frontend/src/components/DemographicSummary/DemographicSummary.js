// @flow
import React from 'react';
import { Panel } from 'react-bootstrap';

type Props = {
  firstName: string,
  lastName: string,
  id: number
}

const DemographicSummary = (props: Props) => (
  <Panel header={"Student info"} bsStyle={"info"}>
    <span>Name: {props.firstName + " " + props.lastName}</span>
    <br/>
    <span>ID number: {props.id}</span>
  </Panel>
);

export default DemographicSummary;