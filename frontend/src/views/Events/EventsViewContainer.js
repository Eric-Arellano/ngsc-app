// @flow
import React, { Component } from "react";
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

class EventsViewContainer extends Component<Props, State> {
  state = {
    isLoading: true,
    isError: false,
    events: []
  };

  componentDidMount() {
    this.getEvents()
      .then(data =>
        this.setState({
          isLoading: false,
          events: this.parseEvents(data.items)
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

  getEvents = (): Promise<any> => {
    const calendar_id =
      "k1n6cusdrh0okgpp4okg8nhak4%40group.calendar.google.com";
    const api_key = "AIzaSyCGqIbNGpiy_pbpCEmAL7vja5hbbUGVGn0";
    const url = `https://www.googleapis.com/calendar/v3/calendars/${calendar_id}/events?key=${api_key}`;
    return getRequest(url);
  };

  parseEvents = (googleEvents: Array<any>): Array<CalendarEvent> =>
    googleEvents.map(event => ({
      start: moment(event.start.date || event.start.dateTime).toDate(),
      end: moment(event.start.date || event.end.dateTime).toDate(),
      title: event.summary,
      description: event.description || "",
      location: event.location || ""
    }));

  resetState = () => {
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
