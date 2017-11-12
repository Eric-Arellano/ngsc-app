// @flow
import type { Requirement } from 'flow/types'

export const mockStudent = (id: number) => {
  return {
    name: {
      first: 'Eric',
      last: 'Arellano'
    },
    id
  }
}

export const mockRequirements = () => {
  const req1: Requirement = {
    name: 'PT',
    reqType: 'Civil-Mil',
    status: 'Accepted',
    hours: '1 civil-mil event'
  }

  const req2: Requirement = {
    name: 'Day of Service',
    reqType: 'Service',
    status: 'Waiting for review',
    hours: '8 hours'
  }

  const req3: Requirement = {
    name: 'IT Awareness Day',
    reqType: 'Civil Mil OR Service',
    status: 'Reclassified from "Civil Mil" to "Civil Mil OR Service"',
    hours: '4 hours or 1 civil-mil event'
  }

  return [req1, req2, req3]
}