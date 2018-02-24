// @flow

export type EngagementEvent = {
  name: string,
  type: string,
  status: string,
  hours: string
}

export type Student = {
  id: number,
  name: Name,
  cohort: number,
  missionTeam: number,
  committee: ?string,
  leadership: ?string
}

export type Name = {
  first: string,
  last: string
}