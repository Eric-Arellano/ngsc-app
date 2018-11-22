import React from "react";
import ReactTable from "react-table"; // see https://react-table.js.org/#/story/readme
import type { EngagementEvent } from "types";
import { Entry, PanelWithLoading } from "components";
import "react-table/react-table.css";

type Props = {
  engagementEvents: Array<EngagementEvent>,
  isLoading: boolean
};

const translateHours = (reqType: string, hours: number): string => {
  if (reqType === "Service" || reqType === "NGSC Activity")
    return `${hours} hour${hours > 1 ? "s" : ""}`;
  else if (reqType === "Civil-Mil OR Service")
    return `${hours} hour${hours > 1 ? "s" : ""} or 1 civil-mil event`;
  else if (reqType === "Civil-Mil") return `1 civil-mil event`;
  return "";
};

const translateStatus = (status: string): string => {
  if (status === "") return "Not yet evaluated";
  if (status === "Late") return "Late (accepted)";
  return status;
};

const LoggedEngagement = ({ engagementEvents, isLoading }: Props) => {
  const columns = [
    {
      id: "Name",
      Header: "Event name",
      accessor: event => event.name
    },
    {
      id: "Type",
      Header: "Engagement type",
      accessor: event => event.type
    },
    {
      id: "Status",
      Header: "Status",
      accessor: event => translateStatus(event.status)
    },
    {
      id: "Hours",
      Header: "Engagement hours",
      accessor: event => translateHours(event.type, event.hours)
    }
  ];

  return (
    <PanelWithLoading header={"Logged engagement"} isLoading={isLoading}>
      <Entry>
        Log your engagement at{" "}
        <a href="https://goo.gl/forms/fEiCuxSW0p8djyJD2">
          https://goo.gl/forms/fEiCuxSW0p8djyJD2
        </a>
        .
      </Entry>
      <br />
      <ReactTable
        data={engagementEvents}
        columns={columns}
        showPagination={false}
        showPageSizeOptions={false}
        minRows={3}
        defaultPageSize={engagementEvents.length}
        resizable={false}
        noDataText={"No events logged yet"}
        className={"-striped"}
      />
    </PanelWithLoading>
  );
};

export default LoggedEngagement;
