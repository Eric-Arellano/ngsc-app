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
    type: 'Civil-Mil',
    status: 'Accepted',
    hours: 0
  }

  const req2: Requirement = {
    name: 'Day of Service',
    type: 'Service',
    status: 'Waiting for review',
    hours: 8
  }

  const req3: Requirement = {
    name: 'IT Awareness Day',
    type: 'Civil-Mil OR Service',
    status: 'Reclassified from "Civil Mil" to "Civil Mil OR Service"',
    hours: 4
  }

  return [req1, req2, req3]
}