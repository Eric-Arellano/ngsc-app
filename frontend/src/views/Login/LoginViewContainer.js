// @flow
import React, { Component } from "react";
import LoginView from "./LoginView";
import { withLoadingAndError } from "components";
import { getDemographics } from "api";
import type { Student } from "types";

type Props = {
  login: Student => void
};

type State = {
  isLoading: boolean,
  isError: boolean,
  isValidated: boolean,
  isConfirmed: boolean,
  student: ?Student
};

class LoginViewContainer extends Component<Props, State> {
  state = {
    isLoading: false,
    isError: false,
    isValidated: false,
    isConfirmed: false,
    student: null
  };

  verifyStudentId = (asurite: string) => {
    this.setState({
      isLoading: true
    });
    getDemographics(asurite)
      .then(data => {
        this.setState({
          isLoading: false,
          isValidated: true,
          student: {
            asurite,
            name: {
              first: data.name.first,
              last: data.name.last
            },
            missionTeam: data.missionTeam,
            committee: data.committee,
            cohort: data.cohort,
            leadership: data.leadership,
            email: data.email,
            phone: data.phone,
            campus: data.campus
          }
        });
      })
      .catch(err => {
        this.setState({
          isLoading: false,
          isError: true
        });
      });
  };

  resetState = () => {
    this.setState({
      isLoading: false,
      isError: false,
      isValidated: false,
      isConfirmed: false,
      student: null
    });
  };

  confirmCorrectStudent = (isConfirmed: boolean) => {
    const { student } = this.state;
    this.setState({ isConfirmed }, () => {
      if (isConfirmed && student != null) {
        this.props.login(student);
      }
    });
  };

  render() {
    const LoginViewWithLoadingAndError = withLoadingAndError(
      LoginView,
      this.resetState,
      "User not found. Please enter a valid ASUrite."
    );
    return (
      <LoginViewWithLoadingAndError
        {...this.state}
        verifyAsurite={this.verifyStudentId}
        confirmCorrectStudent={this.confirmCorrectStudent}
        resetState={this.resetState}
      />
    );
  }
}

export default LoginViewContainer;
