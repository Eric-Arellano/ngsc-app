// @flow
import React from "react";
import Confirmation from "./Confirmation";
import CredentialsContainer from "./CredentialsContainer";
import type { Student } from "types";
import s from "./LoginView.module.css";

type Props = {
  isValidated: boolean,
  isConfirmed: boolean,
  verifyAsurite: string => void,
  confirmCorrectStudent: boolean => void,
  resetState: () => void,
  student: ?Student
};

const LoginView = ({
  isValidated,
  isConfirmed,
  verifyAsurite,
  confirmCorrectStudent,
  resetState,
  student
}: Props) => (
  <div className={s.containerOffsetTop}>
    {!isValidated && <CredentialsContainer onSubmit={verifyAsurite} />}
    {isValidated &&
      !isConfirmed &&
      student != null && (
        <Confirmation
          confirmCorrectStudent={confirmCorrectStudent}
          name={student.name}
          resetState={resetState}
        />
      )}
  </div>
);

export default LoginView;
