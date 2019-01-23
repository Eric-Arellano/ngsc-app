import axios from "axios";
import type { EngagementEvent, Name } from "types";

type DemographicsResponse = {
  name: Name,
  cohort: string,
  missionTeam?: string,
  committee?: string,
  leadership?: string,
  email: string,
  phone: string,
  campus: string
};

export const getDemographics = (
  asurite: string
): Promise<DemographicsResponse> => {
  const api = `/api/app/demographics/${asurite}`;
  return getRequest(api);
};

type EngagementResponse = {
  acceptedTotal: number,
  acceptedCivilMil: number,
  loggedEvents: Array<EngagementEvent>
};

export const getEngagement = (asurite: string): Promise<EngagementResponse> => {
  const api = `/api/app/engagement/${asurite}`;
  return getRequest(api);
};

type AttendanceResponse = {
  noShows: number,
  committeeAttendance: string,
  olsAttendance: string
};

export const getAttendance = (asurite: string): Promise<AttendanceResponse> => {
  const api = `/api/app/attendance/${asurite}`;
  return getRequest(api);
};

export const getRequest = <T>(api: string): Promise<T> => {
  return axios
    .get(api)
    .then(info => info.data)
    .catch(error => error.status);
};
