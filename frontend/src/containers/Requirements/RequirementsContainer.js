// @flow
import React, { Component } from 'react';

import DemographicSummary from './../../components/DemographicSummary/DemographicSummary';
import RequirementsSummary from "../../components/RequirementsSummary/RequirementsSummary";
import type { Requirement } from "../../models";
import { SubmittedRequirementsTable } from "../../components/SubmittedRequirementsTable/EventTable";
import { getRequirements } from "../../api";

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
  isLoading: boolean,
  isError: boolean,
  service: number,
  civilMil: number,
  requirements: Array<Requirement>,
}

class RequirementsContainer extends Component<Props, State> {

  state = {
    isLoading: true,
    isError: false,
    service: 8,
    civilMil: 2,
    requirements: [req1, req2, req3]
  };

  componentDidMount() {
    getRequirements(this.props.id)
      .then((data) => {
        this.setState({
          service: data.service,
          civilMil: data.civilMil,
          requirements: data.events
        })
      })
      .catch((error) => {
        this.setState({
          isLoading: false,
          isError: true
        })
      })
  }

  render() {
    if (this.state.isError) return <p>Error</p>;
    if (this.state.isLoading) return <p>Loading</p>;
    if (!this.state.isLoading) return (
      <div>
        <DemographicSummary firstName={this.props.firstName} lastName={this.props.lastName} id={this.props.id} />
        <RequirementsSummary service={this.state.service} civilMil={this.state.civilMil} />
        <SubmittedRequirementsTable requirements={this.state.requirements}/>
      </div>
    )
  }

}

export default RequirementsContainer;
