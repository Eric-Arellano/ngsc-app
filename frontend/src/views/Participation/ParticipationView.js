// @flow
import * as React from "react";
import AttendanceContainer from "./AttendanceContainer";
import Demographics from "./Demographics";
import EngagementContainer from "./EngagementContainer";
import type { Student } from "types";

type Props = {
  student: Student,
  resetState: () => void
};

const ParticipationView = ({ student, resetState }: Props) => (
  <React.Fragment>
    <Demographics student={student} />
    <AttendanceContainer student={student} resetState={resetState} />
    <EngagementContainer student={student} resetState={resetState} />
  </React.Fragment>
);

export default ParticipationView;
