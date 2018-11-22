import * as React from "react";
import moment from "moment";
import { getRequest } from "api";
import EventsView from "./EventsView";
import { withError } from "components";
import type { CalendarEvent } from "types";

type Props = {};

type State = {
  isLoading: boolean,
  isError: boolean,
  events: Array<CalendarEvent>
};

type EventResponse = {
  id: string,
  status: string,
  htmlLink: string,
  created: string,
  updated: string,
  summary: string,
  description?: string,
  location?: string,
  creator: {
    email: string
  },
  start: {
    date?: string,
    dateTime?: string
  },
  end: {
    date?: string,
    dateTime?: string
  },
  iCalUID: string
};

class EventsViewContainer extends React.Component<Props, State> {
  state = {
    isLoading: true,
    isError: false,
    events: []
  };

  componentDidMount() {
    this.getEvents()
      .then(events =>
        this.setState({
          isLoading: false,
          events: this.parseEvents(events)
        })
      )
      .catch(error =>
        this.setState({
          isError: true,
          isLoading: false,
          events: []
        })
      );
  }

  getEvents = (): Promise<Array<EventResponse>> => {
    const calendar_id =
      "k1n6cusdrh0okgpp4okg8nhak4%40group.calendar.google.com";
    const api_key = "AIzaSyCGqIbNGpiy_pbpCEmAL7vja5hbbUGVGn0";
    const url = `https://www.googleapis.com/calendar/v3/calendars/${calendar_id}/events?key=${api_key}`;
    const response = getRequest(url);
    return response.then(data => data.items);
  };

  parseEvents = (googleEvents: Array<EventResponse>): Array<CalendarEvent> =>
    googleEvents
      .filter(
        event =>
          event.start.date !== undefined || event.start.dateTime !== undefined
      )
      .map(event => ({
        start: moment(
          event.start.date !== undefined
            ? event.start.date
            : event.start.dateTime
        ).toDate(),
        end: moment(
          event.end.date !== undefined ? event.end.date : event.end.dateTime
        ).toDate(),
        title: event.summary,
        description: event.description || "",
        location: event.location || ""
      }));

  resetState = (): void => {
    this.setState({
      events: [],
      isLoading: false,
      isError: false
    });
  };

  render() {
    const EventsViewWithError = withError(
      EventsView,
      this.resetState,
      "There was an error. Please try again."
    );
    return <EventsViewWithError {...this.state} />;
  }
}

export default EventsViewContainer;
