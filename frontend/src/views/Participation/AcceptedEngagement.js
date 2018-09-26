// @flow
import React from "react";
import { Entry, PanelWithLoading } from "components";

type Props = {
  totalHours: number,
  civilMil: number,
  isLoading: boolean
};

const AcceptedEngagement = ({ totalHours, civilMil, isLoading }: Props) => (
  <PanelWithLoading header="Accepted Engagement" isLoading={isLoading}>
    <Entry>Accepted # of hours: {totalHours}</Entry>
    <Entry>Accepted # of civil mil: {civilMil}</Entry>
  </PanelWithLoading>
);

export default AcceptedEngagement;
