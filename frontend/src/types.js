// @flow

// -------------------------------------------------------
// Data models
// -------------------------------------------------------

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

// -------------------------------------------------------
// UI Types
// -------------------------------------------------------

export type ValidationState = 'valid' | 'invalid' | 'neutral'

export type RadioOption = {
  label: string,
}

export type CheckboxOption = {
  label: string,
  checked: bool,
}
