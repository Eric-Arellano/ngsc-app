// @flow
import React, { Component } from 'react'
import { AcceptedRequirements, Demographics, Loading, LoggedRequirements } from 'components'
import { getRequirements } from 'utils/api'
import type { Requirement, Student } from 'flow/types'

type Props = {
  student: Student
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
  }

  componentDidMount () {
    getRequirements(this.props.student.id)
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

  render () {
    const {isError, isLoading, civilMil, service, requirements} = this.state
    if (isError) {
      return <p>Error</p>
    }
    if (isLoading) {
      return <Loading />
    }
    return [
      <Demographics {...this.props} key={0} />,
      <AcceptedRequirements service={service} civilMil={civilMil} key={1} />,
      <LoggedRequirements requirements={requirements} key={2} />
    ]
  }
}

export default RequirementsContainer
