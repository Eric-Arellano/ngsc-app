// @flow
import React, { Component } from 'react';
import { DemographicSummary, RequirementsSummary, SubmittedRequirementsTable, Loading } from 'components'
import { getRequirements } from 'utils/api'
import type { Name, Requirement } from 'flow/types'

type Props = {
  id: number,
  missionTeam: number,
  name: Name
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
    service: 0,
    civilMil: 0,
    requirements: []
  };

  componentDidMount() {
    getRequirements(this.props.id)
      .then((data) => {
        this.setState({
          service: data.acceptedService,
          civilMil: data.acceptedCivilMil,
          requirements: data.requirements,
          isLoading: false,
        })
      })
      .catch((error) => {
        this.setState({
          service: 0,
          civilMil: 0,
          requirements: [],
          isLoading: false,
          isError: true,
        })
      })
  }

  render() {
    const { isError, isLoading, civilMil, service, requirements } = this.state
    if (isError) {
      return <p>Error</p>
    }
    if (isLoading) {
      return <Loading />
    }
    return [
      <DemographicSummary {...this.props} key={0} />,
      <RequirementsSummary service={service} civilMil={civilMil} key={1} />,
      <SubmittedRequirementsTable requirements={requirements} key={2} />
    ]
  }
}

export default RequirementsContainer;
