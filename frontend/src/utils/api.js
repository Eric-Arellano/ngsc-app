// @flow
import axios from 'axios';

export const getDemographics = (id: number) => {
  const api = `/api/demographics/${id}`;
  return axios.get(api)
    .then(info => info.data)
    .catch(error => error.status)
};

export const getRequirements = (id: number) => {
  const api = `/api/engagement/${id}`;
  return axios.get(api)
    .then(info => info.data)
    .catch(error => error.status)
};