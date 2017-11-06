// @flow
import React, { Component } from 'react';

import DemographicSummary from './../../components/DemographicSummary/DemographicSummary';
import RequirementsSummary from "../../components/RequirementsSummary/RequirementsSummary";
import type { Requirement } from "../../components/SubmittedRequirementsTable/EventTable";
import { SubmittedRequirementsTable } from "../../components/SubmittedRequirementsTable/EventTable";

// TODO: pull from requirements spreadsheet and render below

// -----------------
// Fake data
// -----------------

const req1: Requirement = {
  name: 'PT',
  reqType: 'Civil-Mil',
  status: 'Accepted',
  hours: '1 civil-mil event'
};

const req2: Requirement = {
  name: 'Day of Service',
  reqType: 'Service',
  status: 'Waiting for review',
  hours: '8 hours'
};

const req3: Requirement = {
  name: 'IT Awareness Day',
  reqType: 'Civil Mil OR Service',
  status: 'Reclassified from "Civil Mil" to "Civil Mil OR Service"',
  hours: '4 hours or 1 civil-mil event'
};

// -----------------
// Actual code
// -----------------

type Props = {
  id: number,
  firstName: string,
  lastName: string,
}

type State = {
  service: number,
  civilMil: number,
  requirements: Array<Requirement>,
}

class Summary extends Component<Props, State> {

  // real code
  // state = {
  //   service: 0,
  //   civilMil: 0,
  //   requirements: []
  // };

  // demo
  state = {
    service: 8,
    civilMil: 2,
    requirements: [req1, req2, req3]
  };

  render() {
    return (
      <div>
        <DemographicSummary firstName={this.props.firstName} lastName={this.props.lastName} id={this.props.id} />
        <RequirementsSummary service={this.state.service} civilMil={this.state.civilMil} />
        <SubmittedRequirementsTable requirements={this.state.requirements}/>
      </div>
    )
  }

}

export default Summary;
