// @flow
import React from 'react';
import './App.css';

import Header from './../../components/Header/Header'
import IDInput from './../../components/IDInput/IDInput';
import DemographicSummary from './../../components/DemographicSummary/DemographicSummary';
import RequirementsSummary from "../../components/RequirementsSummary/RequirementsSummary";
import type { Requirement } from "../../components/SubmittedRequirementsTable/EventTable";
import { SubmittedRequirementsTable } from "../../components/SubmittedRequirementsTable/EventTable";

// -----------------
// Fake data
// -----------------

const req1: Requirement = {
  name: 'PT',
  reqType: 'Civil-Mil',
  status: 'Accepted',
  hours: '1 civil-mil event'
};

const req2: Requirement = {
  name: 'Day of Service',
  reqType: 'Service',
  status: 'Waiting for review',
  hours: '8 hours'
};

const req3: Requirement = {
  name: 'IT Awareness Day',
  reqType: 'Civil Mil OR Service',
  status: 'Reclassified from "Civil Mil" to "Civil Mil OR Service"',
  hours: '4 hours or 1 civil-mil event'
};

const requirements: Array<Requirement> = [
  req1,
  req2,
  req3
];

// -----------------
// Actual code
// -----------------

const App = () => {
  return (
    <div className="App">
      <Header />
      <IDInput/>
      <DemographicSummary firstName="Eric" lastName='Arellano' id={1208487250} />
      <RequirementsSummary service={8} civilMil={2} />
      <SubmittedRequirementsTable requirements={requirements}/>
    </div>
  );
};

export default App;
