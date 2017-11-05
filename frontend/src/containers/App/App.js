// @flow
import React from 'react';
import logo from '../../logo.png';
import './App.css';

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
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo"/>
        <h1 className="App-title">NGSC Engagement Requirements</h1>
      </header>
      <IDInput/>
      <DemographicSummary firstName="Eric" lastName='Arellano' id={1208487250} />
      <RequirementsSummary service={8} civilMil={2} />
      <SubmittedRequirementsTable requirements={requirements}/>
    </div>
  );
};

export default App;
