// @flow
import React, { Component } from 'react';
import type { Requirement } from 'models';
import { DemographicSummary, RequirementsSummary, SubmittedRequirementsTable } from 'components'
import { getRequirements } from 'utils/api'

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
    const { name, id } = this.props
    const { isError, isLoading, civilMil, service, requirements } = this.state
    if (isError) {
      return <p>Error</p>
    }
    if (isLoading) {
      return <p>Loading</p>
    }
    return [
      <DemographicSummary firstName={name.first} lastName={name.last} id={id} key={0} />,
      <RequirementsSummary service={service} civilMil={civilMil} key={1} />,
      <SubmittedRequirementsTable requirements={requirements} key={2} />
    ]
  }
}

export default RequirementsContainer;
