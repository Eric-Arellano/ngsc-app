import React from "react";
import type { Student } from "types";
import { Entry, Panel } from "components";

type Props = {
  student: Student
};

const Demographics = ({
  student: {
    name,
    missionTeam,
    committee,
    cohort,
    leadership,
    email,
    phone,
    campus
  }
}: Props) => (
  <Panel header="Student info">
    <Entry>
      Name: {name.first} {name.last}
    </Entry>
    <Entry>Cohort: {cohort}</Entry>
    {missionTeam !== undefined && <Entry>Mission team: {missionTeam}</Entry>}
    {committee !== undefined && <Entry>Committee: {committee}</Entry>}
    {leadership !== undefined && <Entry>Leadership: {leadership}</Entry>}
    <Entry>Email: {email}</Entry>
    <Entry>Phone: {phone}</Entry>
    <Entry>Campus: {campus}</Entry>
    <br />
    <p>
      <em>
        Use this form to submit changes to your contact info:
        <a href="https://tinyurl.com/yc48bo3d">https://tinyurl.com/yc48bo3d</a>
      </em>
    </p>
  </Panel>
);

export default Demographics;
