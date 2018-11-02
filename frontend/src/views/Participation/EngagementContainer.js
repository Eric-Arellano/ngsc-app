// @flow
import * as React from "react";
import AcceptedEngagement from "./AcceptedEngagement";
import LoggedEngagement from "./LoggedEngagement";
import { getEngagement } from "api";
import type { EngagementEvent, Student } from "types";

type Props = {
  student: Student,
  resetState: () => void
};

type State = {
  isLoading: boolean,
  isError: boolean,
  totalHours: number,
  civilMil: number,
  engagementEvents: Array<EngagementEvent>
};

class EngagementContainer extends React.Component<Props, State> {
  state = {
    isLoading: true,
    isError: false,
    totalHours: 0,
    civilMil: 0,
    engagementEvents: []
  };

  componentDidMount() {
    getEngagement(this.props.student.asurite)
      .then(data => {
        this.setState({
          totalHours: data.acceptedTotal,
          civilMil: data.acceptedCivilMil,
          engagementEvents: data.loggedEvents,
          isLoading: false
        });
      })
      .catch(error => {
        this.setState({
          totalHours: 0,
          civilMil: 0,
          engagementEvents: [],
          isLoading: false,
          isError: true
        });
      });
  }

  resetState = () => this.props.resetState();

  render() {
    // TODO: no error handling because of weirdness with React.Fragment
    return (
      <React.Fragment>
        <AcceptedEngagement {...this.state} key={0} />
        <LoggedEngagement {...this.state} key={1} />
      </React.Fragment>
    );
  }
}

export default EngagementContainer;
