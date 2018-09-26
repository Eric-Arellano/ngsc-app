// @flow
import axios from "axios";

export const getDemographics = (asurite: string): Promise<any> => {
  const api = `/api/app/demographics/${asurite}`;
  return getRequest(api);
};

export const getEngagement = (asurite: string): Promise<any> => {
  const api = `/api/app/engagement/${asurite}`;
  return getRequest(api);
};

export const getAttendance = (asurite: string): Promise<any> => {
  const api = `/api/app/attendance/${asurite}`;
  return getRequest(api);
};

export const getRequest = (api: string): Promise<any> => {
  return axios
    .get(api)
    .then(info => info.data)
    .catch(error => error.status);
};
