// @flow
import * as React from "react";
import { Route } from "react-router-dom";
import { LoginViewContainer } from "views";
import type { Student } from "types";

type Props = {
  path: string,
  isLoggedIn: boolean,
  login: Student => void,
  component: React.Component<any>
};

const PrivateRoute = ({
  component: Component,
  isLoggedIn,
  login,
  path,
  ...props
}: Props) => (
  <Route
    exact
    path={path}
    render={() =>
      isLoggedIn ? (
        // $FlowFixMe
        <Component {...props} />
      ) : (
        <LoginViewContainer login={login} />
      )
    }
  />
);

export default PrivateRoute;
