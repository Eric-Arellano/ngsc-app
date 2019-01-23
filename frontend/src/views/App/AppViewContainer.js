import * as React from "react";
import AppView from "./AppView";
import type { Student } from "types";

type Props = {};

type State = {
  isLoggedIn: boolean,
  student: ?Student
};

class AppViewContainer extends React.Component<Props, State> {
  state = {
    isLoggedIn: false,
    student: null
  };

  componentDidMount() {
    const fadeInPage = () => {
      if (document.body != null) document.body.style.opacity = "1";
    };
    requestAnimationFrame(fadeInPage);
  }

  login = (student: Student): void => {
    this.setState({
      student,
      isLoggedIn: true
    });
  };

  resetState = (): void => {
    this.setState({
      isLoggedIn: false,
      student: null
    });
  };

  render() {
    return (
      <AppView
        {...this.state}
        login={this.login}
        resetState={this.resetState}
      />
    );
  }
}

export default AppViewContainer;
