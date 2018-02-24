// @flow
import axios from 'axios'

export const getDemographics = (id: number) => {
  const api = `/api/demographics/${id}`
  return getRequest(api)
}

export const getEngagement = (id: number) => {
  const api = `/api/engagement/${id}`
  return getRequest(api)
}

export const getAttendance = (id: number) => {
  const api = `/api/attendance/${id}`
    return getRequest(api)
}

const getRequest = (api: string) => {
  return axios.get(api)
    .then(info => info.data)
    .catch(error => error.status)
}