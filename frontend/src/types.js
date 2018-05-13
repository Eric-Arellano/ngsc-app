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
  missionTeam?: string,
  committee?: string,
  leadership?: string,
  email: string,
  phone: string,
  campus: string
}

export type Name = {
  first: string,
  last: string
}

export type CalendarEvent = {
  title: string,
  start: Date,
  end: Date,
  description?: string,
  location?: string,
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
