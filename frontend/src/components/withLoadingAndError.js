import React from "react";
import { Error, Loading } from "components";

function withLoadingAndError(
  WrappedComponent,
  resetState: () => void,
  errorMessage: string
) {
  return function withLoadingComponent({ isLoading, isError, ...props }) {
    if (isLoading) return <Loading />;
    if (isError) return <Error resetState={resetState}>{errorMessage}</Error>;
    return <WrappedComponent {...props} />;
  };
}

export default withLoadingAndError;
