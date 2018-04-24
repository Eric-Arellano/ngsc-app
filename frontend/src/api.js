// @flow
import axios from 'axios'

export const getDemographics = (id: number): Promise<any> => {
  const api = `/api/app/demographics/${id}`
  return getRequest(api)
}

export const getEngagement = (id: number): Promise<any> => {
  const api = `/api/app/engagement/${id}`
  return getRequest(api)
}

export const getAttendance = (id: number): Promise<any> => {
  const api = `/api/app/attendance/${id}`
  return getRequest(api)
}

export const getRequest = (api: string): Promise<any> => {
  return axios.get(api)
    .then(info => info.data)
    .catch(error => error.status)
}

export const postRequest = (api: string, payload: {}): Promise<any> => {
  return axios.post(api, payload)
    .then(result => result.data)
    .catch(error => error.status)
}
