// @flow
import React, { Component } from "react";
import { withError } from "components";
import { getAttendance } from "api";
import type { Student } from "types";
import Attendance from "./Attendance";

type Props = {
  student: Student,
  resetState: () => void
};

type State = {
  isLoading: boolean,
  isError: boolean,
  noShows: number,
  committeeAttendance: string,
  olsAttendance: string
};

class AttendanceContainer extends Component<Props, State> {
  state = {
    isLoading: true,
    isError: false,
    noShows: 0,
    committeeAttendance: "",
    olsAttendance: ""
  };

  componentDidMount() {
    getAttendance(this.props.student.asurite)
      .then(data => {
        this.setState({
          noShows: data.noShows,
          committeeAttendance: data.committeeAttendance,
          olsAttendance: data.olsAttendance,
          isLoading: false
        });
      })
      .catch(error => {
        this.setState({
          noShows: 0,
          committeeAttendance: "",
          olsAttendance: "",
          isLoading: false,
          isError: true
        });
      });
  }

  resetState = () => this.props.resetState();

  render() {
    const AttendanceWithError = withError(
      Attendance,
      this.resetState,
      "There was an error. Please try again."
    );
    return <AttendanceWithError {...this.props} {...this.state} />;
  }
}

export default AttendanceContainer;
