// @flow
import React from 'react';
import { Panel, Table } from 'react-bootstrap';

export type Requirement = {
  name: string,
  reqType: string,
  status: string,
  hours: string
}

type Props = {
  requirements: Array<Requirement>
}

export const SubmittedRequirementsTable = (props: Props) => (
  <Panel header={"Logged Requirements"} bsStyle={"info"}>
    <Table striped bordered responsive>
      <thead>
        <tr>
          <th>Event name</th>
          <th>Requirement type</th>
          <th>Status</th>
          <th>Requested hours</th>
        </tr>
      </thead>
      <tbody>
        {props.requirements.map((requirement) => (
          <tr>
            <td>{requirement.name}</td>
            <td>{requirement.reqType}</td>
            <td>{requirement.status}</td>
            <td>{requirement.hours}</td>
          </tr>
        ))}
      </tbody>
    </Table>
  </Panel>
);

// export default SubmittedRequirementsTable;
