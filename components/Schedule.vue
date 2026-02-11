<!-- An events calendar that pulls events from DynamoDB -->

<template>
    <div class="whole-component">
        <div id="schedule-header">
            <h3 class="glow">Schedule</h3>
        </div>
        <div id="schedule" class="section" :style="styles">
        <!-- FULL SCHEDULE -->
        <div class="schedule-container">
            <div class="dates">
            <button
                v-for="date in Object.keys(schedule)"
                :key="date"
                :class="date === selectedDay.day ? 'active' : 'fff'"
                @click="setDaySelection(date)"
            >
                {{
                new Date(parseInt(date)).toLocaleDateString('en-US', {
                    weekday: 'short',
                    month: 'long',
                    day: 'numeric',
                })
                }}
            </button>
            </div>
            <!-- this event list is implemented with a css grid
            each row is a 15 minute increment. the start and end times are parsed
            to determine a proper starting rows and row spans for the event elements-->
            <!-- because of how the times are centered, they don't cover everything on scroll 
            and hence need an additional element to act as the background cover over the event elements -->
            <span class="left-cover"></span>
            <div class="event-list-container">
              <!-- Coming Soon Message (shows when no events) -->
              <div v-if="!dataLoaded || Object.keys(schedule).length === 0" class="coming-soon-inline">
                <h2>Coming Soon</h2>
              </div>
            <div class="event-list" :style="{}">
                <span
                v-for="(_, idx) in selectedDay.times"
                :key="idx"
                class="bar"
                :style="{
                    // add top padding (1rem) and 2.1rem for each 15 minute interval
                    // subtract 1px to align bar in middle of grid row
                    top: `calc(1rem + ${idx * (60 / INTERVAL_M) * 2.1}rem - 1px)`,
                }"
                ></span>
                <div
                v-for="(time, idx) in selectedDay.times"
                :key="time"
                class="time-container"
                :style="{
                    gridRow: `${idx * (60 / INTERVAL_M) + 1} / span ${
                    60 / INTERVAL_M
                    }`,
                }"
                >
                <p>{{ time }}</p>
                </div>
                <div
                v-for="event in selectedDay.events"
                :key="event.id"
                :style="{
                    gridRow: `${event.startRow} / span ${event.rowSpan}`,
                }"
                class="event-container"
                :class="event.type"
                @click="
                    () => {
                    selectedEvent = event;
                    showEventModal = true;
                    }
                "
                >
                <div>
                    <p class="name">{{ event.title }}</p>
                    <p>{{ event.location }}</p>
                </div>
                </div>
            </div>
            </div>
            <!-- Category Legend -->
            <div class="category-legend">
              <div class="legend-item">
                <span class="legend-color" style="background-color: #FFAF3F;"></span>
                <span class="legend-label">General</span>
              </div>
              <div class="legend-item">
                <span class="legend-color" style="background-color: #009051;"></span>
                <span class="legend-label">Events</span>
              </div>
              <div class="legend-item">
                <span class="legend-color" style="background-color: #EC5156;"></span>
                <span class="legend-label">Workshops</span>
              </div>
              <div class="legend-item">
                <span class="legend-color" style="background-color: #528CA5;"></span>
                <span class="legend-label">Sponsor Event</span>
              </div>
              <div class="legend-item">
                <span class="legend-color" style="background-color: #6A166F;"></span>
                <span class="legend-label">Food</span>
              </div>
            </div>
        </div>
        </div>
    </div>
    <ModalsContainer />
    <EventModal
      v-model="showEventModal"
      :selectedEvent="selectedEvent"
      @close="() => closeEventModal()"
    />
  </template>
  
  <script setup lang="ts">
  import { ref, onMounted } from 'vue';
  import { ModalsContainer } from 'vue-final-modal';
  import type { ParsedEvent, CalculatedEvent } from '../types/event';
  
  type DaySchedule = {
    events: CalculatedEvent[];
    concurrence: number;
  };
  
  type AllSchedules = {
    [key: string]: DaySchedule;
  };
  
  interface SelectionData extends DaySchedule {
    times: string[];
    day: string;
  }
  
  // conversion values
  const MINUTES_TO_MS = 60000;
  const INTERVAL_M = 15;
  const INTERVAL_MS = INTERVAL_M * MINUTES_TO_MS;
  
  const dataLoaded = ref(false);
  const schedule = ref<AllSchedules>({});
  const selectedDay = ref<SelectionData>({} as SelectionData);
  const selectedEvent = ref<CalculatedEvent>();
  const showEventModal = ref(false);
  
  onMounted(async () => {
    const rawEvents = await fetchRawEvents();
    const formattedEvents = mapEvents(rawEvents);
    schedule.value = formattedEvents;
    setDaySelection(Object.keys(formattedEvents)[0]);
    dataLoaded.value = true;
    console.log(
      schedule.value[Object.keys(schedule.value)[1]].events.map(
        (event) => event.title
      )
    );
  });
  
  /**
   *
   * @param day milliseconds since epoch as string
   */
  function setDaySelection(day: string) {
    const daySchedule = schedule.value[day];
  
    // get starting time of first event and ending time of last event
    const start = daySchedule.events[0].startTimeMs;
    const end = daySchedule.events[daySchedule.events.length - 1].endTimeMs;
    // find out how many 15 minute sections there are
    const elapsed = end - start;
    const sections = elapsed / (60 * MINUTES_TO_MS);
  
    // create array of times for those 15 minute sections
    const times = Array.from({ length: sections + 1 }, (_, i) => {
      const ms = start + i * (60 * MINUTES_TO_MS);
  
      const time = new Date(ms).toLocaleTimeString([], {
        hour: 'numeric',
        hour12: true,
      });
  
      return time;
    });
  
    console.log(day);
  
    selectedDay.value = { ...daySchedule, times, day };
  }
  
  /**
   * Fetch events from DynamoDB
   *
   * calculates a rounded start and end time for each event
   * formats category for display
   *
   * @returns list of events in sorted order by start time
   */
  async function fetchRawEvents(): Promise<ParsedEvent[]> {
    // CHANGE BACKEND URL WHEN DEPLOYING TO api.bit.camp/schedule!!!!!
    const eventsRes = await fetch('https://api.alpha.bit.camp/schedule');
    const events = await eventsRes.json();
  
    return events.map((event: any): ParsedEvent => ({
      id: event.id,
      title: event.event_name || event.title,
      description: event.description || '',
      startTime: event.start_time || event.startTime,
      endTime: event.end_time || event.endTime,
      location: event.location || 'TBD',
      type: event.category || event.type || 'General',
      speakers: event.speakers || [],
      links: event.links || []
    })).sort((a: ParsedEvent, b: ParsedEvent) => 
      new Date(a.startTime).getTime() - new Date(b.startTime).getTime()
    );
  }
  
  /** Split raw events into days and calculate concurrence
   * as well as startRow and span for each event for grid layout
   *
   * @param events list of events in sorted order
   * @returns object with events split by day
   */
  function mapEvents(events: ParsedEvent[]): AllSchedules {
    interface BareDaySchedule {
      events: CalculatedEvent[];
      concurrence?: number;
    }
    
    type BareAllSchedule = {
      [key: string]: BareDaySchedule;
    };
  
    console.log(events);
  
    // holds the number of events in each time window
    // map uses numbers instead of dates because of how JS handles Map keys (no hashing)
    const allTimeWindows = new Map<number, Map<number, number>>();
  
    const schedule = events.reduce((acc, event) => {
      const startTimeMs = new Date(event.startTime).getTime();
      const endTimeMs = new Date(event.endTime).getTime();
      
      // get day of event
      const date = new Date(startTimeMs);
      date.setHours(0, 0, 0, 0);
      const dayTime = date.getTime();
  
      // get time windows for the day
      let timeWindows = allTimeWindows.get(dayTime);
      if (!timeWindows) {
        timeWindows = new Map();
        allTimeWindows.set(dayTime, timeWindows);
      }
  
      // iterate through entire event time window with 15 minute increments
      for (
        let timeWindow = startTimeMs;
        timeWindow < endTimeMs;
        timeWindow += INTERVAL_MS
      ) {
        if (timeWindows.has(timeWindow)) {
          timeWindows.set(timeWindow, timeWindows.get(timeWindow)! + 1);
        } else {
          timeWindows.set(timeWindow, 1);
        }
      }
  
      const calculatedEvent: CalculatedEvent = {
        id: event.id,
        title: event.title,
        description: event.description,
        location: event.location,
        type: event.type,
        speakers: event.speakers,
        links: event.links,
        startTimeMs,
        endTimeMs,
        startRow: 0,
        rowSpan: 0,
        colSpan: 1
      };
  
      const existingDate = acc[dayTime];
      if (existingDate) {
        existingDate.events.push(calculatedEvent);
      } else {
        acc[dayTime] = { events: [calculatedEvent] };
      }
      return acc;
    }, {} as BareAllSchedule);
  
    // get max concurrence for each day and calculate sub-columns for overlapping events
    for (const [dateTime, data] of Object.entries(schedule)) {
      const timeWindows = allTimeWindows.get(parseInt(dateTime));
      if (timeWindows) {
        data.concurrence = Math.max(...Array.from(timeWindows.values()));
      }

      const firstEntry = timeWindows?.entries().next().value;
      if (firstEntry) {
        const [firstTime] = firstEntry;
        let dayStart = new Date(firstTime).getTime();
        dayStart = dayStart - (dayStart % (60 * MINUTES_TO_MS));

        data.events = data.events.map((event: CalculatedEvent): CalculatedEvent => {
          let rowSpan = (event.endTimeMs - event.startTimeMs) / INTERVAL_MS;
          if (rowSpan === 0) rowSpan = 2;
          if (rowSpan < 2) rowSpan = 2;

          return {
            ...event,
            startRow: (event.startTimeMs - dayStart) / INTERVAL_MS + 1,
            rowSpan
          };
        });
      }
    }
  
    return schedule as AllSchedules;
  }
  
  function formatAMPM(date: Date) {
    // Convert to AM/PM local time
    return date.toLocaleTimeString([], {
      hour: '2-digit',
      minute: '2-digit',
      hour12: true,
    });
  }
  
  function closeEventModal() {
    showEventModal.value = false;
  }
  </script>
  
  <script lang="ts">
  export default {
    name: 'SchedulePage',
    props: {
      styles: {
        type: String,
        required: false,
        default: '',
      },
    },
  };
  </script>
  
  <style scoped lang="scss">
  @import 'bootstrap/dist/css/bootstrap.css';
  @import '../assets/css/schedule.scss';

  .whole-component {
    // background: #010B18;
  }

  #schedule-header {
    display: flex;
    justify-content: right;
    align-items: right;
    width: 100%;
    max-width: 150rem;
    margin: 0 auto;
    padding-top: 5rem;
    padding-right: 5rem;
    padding-left: 2.5rem;

    h3 {
      font-family: 'Aleo', serif;
      font-weight: 600;
      font-size: 8rem;
      color: white;
      margin: 0;
      text-shadow: 0 0 20px #FFF7EB;
    }
}

  #schedule {
    position: relative;
    height: 100%;
    display: flex;
    flex-direction: column;
    width: 100%;
    max-width: 150rem;
    margin: 0 auto;
    padding: 2.5rem;

    * {
      padding: 0;
      margin: 0;
    }

    /* width */
    ::-webkit-scrollbar {
      width: 10px;
      height: 10px;
      opacity: 0.8;
    }

    /* Track */
    ::-webkit-scrollbar-track {
      background: rgba(241, 241, 241, 0.557);
    }

    /* Handle */
    ::-webkit-scrollbar-thumb {
      background: #ffffffb3;
      border-radius: 999px;
    }

    /* Handle on hover */
    ::-webkit-scrollbar-thumb:hover {
      background: #ffff;
    }

    .schedule-container {
      position: relative;
      border-radius: 10px;
      overflow: hidden;
      height: 100%;
      display: flex;
      flex-direction: column;
      backdrop-filter: blur(12.5px);
      background: rgba(255, 255, 255, 0.8);
      border: 1px solid #d5d8dc;
    }
  
    .schedule-icon {
      width: 30rem;
      margin: 0 auto -2rem auto;
      display: block;
      position: relative;
      z-index: 4;
  
      @media screen and (max-width: 767.8px) {
        width: 18rem;
        margin-bottom: 1rem;
      }
    }
  
    .event-list-container {
      background: rgba(179, 185, 192, 0.15);
      position: relative;
      overflow-x: auto;
      overflow-y: auto;
      height: 100%;
      padding-bottom: 3rem;
      flex: 1;
      @media screen and (max-width: 1024px) {
        flex: 0 1 auto;
        min-height: 300px;
        padding-bottom: 1rem;
      }
    }
  
    .left-cover {
      position: absolute;
      background: rgba(255, 255, 255, 0.8);
      border-right: 1px solid rgba(0, 0, 0, 0.2);
      width: 9rem;
      left: 0;
      top: 74px;
      bottom: 55px;
      z-index: 2;

      @media screen and (max-width: 1024px) {
        width: 9rem;
        top: 60px;
        bottom: 50px;
      }
    }
    .event-list {
      padding-top: 1rem;
      display: grid;
      grid-template-columns: [time] 10rem repeat(auto-fit, minmax(20rem, 1fr));
      column-gap: 0.5rem;
      position: relative;
      // change grid-row height with the white hour-line bar layout
      grid-auto-rows: 2.1rem;
      min-width: 100%;
      width: 100%;
      height: 100%;
  
      padding-right: 1rem;
  
      @media screen and (max-width: 767.8px) {
        grid-template-columns: [time] 10rem repeat(auto-fit, minmax(12rem, 1fr));
      }
  
      .bar {
        position: absolute;
        background: rgba(255, 255, 255, 0.3);
        height: 1px;
        width: calc(100% - 9rem);
        left: 9rem;
        z-index: 0;
      }
      .time-container {
        position: sticky;
        left: 0.5rem;
        grid-column: time;
        font-family: 'Avenir';
        z-index: 2;
        font-weight: 500;
        font-size: 20px;
        color: #000;
        text-align: center;

        p {
          color: #000;
          max-width: 8rem;
          width: 100%;
          padding: 0 1rem;
          position: absolute;
          top: 0;
          transform: translateY(-50%);
          text-align: center;
          margin: 0;

          @media screen and (max-width: 767.8px) {
            font-size: 14px;
          }
        }
      }
      .event-container {
        font-size: 1.1rem;
        min-width: 0;
        border-radius: 10px;
        padding: 0.5rem;
        margin: 0.15rem;
        overflow: hidden;
        z-index: 1;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: flex-start;
        cursor: pointer;
        transition: all 0.2s ease;
        border-width: 1px;
        border-style: solid;
        color: white;

        @media screen and (max-width: 767.8px) {
          padding: 0.5rem;
        }

        &:hover {
          transform: translateY(-2px);
          box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        }

        p {
          margin: 0;
          margin-bottom: 0.2rem;
        }

        .name {
          overflow: hidden;
          text-overflow: ellipsis;
          display: -webkit-box;
          -webkit-line-clamp: 2;
          line-clamp: 2;
          -webkit-box-orient: vertical;
          font-family: 'Avenir';
          font-weight: 700;
          font-size: 10px;
        }

        > p:last-child {
          font-weight: 400;
          font-size: 10px;
          opacity: 0.95;
        }

        &.main-event {
          background-color: $COLOR_MAIN_EVENT;
          border-color: $COLOR_MAIN_EVENT_BORDER;
        }

        &.workshop-event {
          background-color: $COLOR_WORKSHOP;
          border-color: $COLOR_WORKSHOP_BORDER;
        }

        &.mini-event {
          background-color: $COLOR_MINI_EVENT;
          border-color: $COLOR_MINI_EVENT_BORDER;
        }

        &.sponsor-event {
          background-color: $COLOR_SPONSOR;
          border-color: $COLOR_SPONSOR_BORDER;
        }

        &.food-event {
          background-color: $COLOR_FOOD;
          border-color: $COLOR_FOOD_BORDER;
        }
      }
    }

    .coming-soon-inline {
      display: flex;
      align-items: center;
      justify-content: center;
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      width: 100%;
      height: 100%;
      z-index: 3;
      
      h2 {
        font-size: 2.5rem;
        color: black;
        font-family: 'Aleo', serif;
        
        @media screen and (max-width: 768px) {
          font-size: 2rem;
        }
      }
    }
  
    .dates {
      background: rgba(255, 255, 255, 0.8);
      font-family: 'Aleo';
      display: flex;
      justify-content: center;
      align-items: center;
      position: relative;
      z-index: 3;
      gap: 60px;
      padding: 20px 60px;
      min-height: 74px;
      border-bottom: 1px solid #d5d8dc;
      flex-wrap: wrap;

      @media screen and (max-width: 767.8px) {
        background: rgba(255, 255, 255, 0.8);
        gap: 20px;
        padding: 15px 20px;
        min-height: 74px;
      }

      button {
        background: transparent;
        border: none;
        cursor: pointer;
        color: #010B18;
        font-weight: 600;
        padding: 5px 15px;
        height: auto;
        width: auto;
        transition: all 0.2s;
        border-radius: 10px;
        white-space: nowrap;
        font-family: 'Aleo', sans-serif;
        font-size: 20px;
        position: relative;

        &.active {
          background-color: #FF6F3F;
          color: #FFFFFF;

          @media screen and (max-width: 767.8px) {
            background: #FF6F3F;
            color: #FFFFFF;
          }
        }

        &:hover:not(.active) {
          background: rgba(255, 111, 63, 0.1);
        }

        // Separator between tabs
        &:not(:last-child)::after {
          content: '';
          position: absolute;
          right: -30px;
          top: 50%;
          transform: translateY(-50%);
          width: 1px;
          height: 34px;
          background: #d5d8dc;

          @media screen and (max-width: 767.8px) {
            right: -10px;
            height: 20px;
          }
        }

        @media screen and (max-width: 767.8px) {
          font-size: 14px;
          padding: 5px 10px;
        }
      }
    }

    .category-legend {
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 2rem;
      padding: 1.5rem 2rem;
      background: rgba(255, 255, 255, 0.8);
      font-family: 'Aleo';
      border-top: 1px solid #d5d8dc;
      z-index: 2;

      @media screen and (max-width: 767.8px) {
        display: grid;
        grid-template-columns: repeat(6, 1fr);
        gap: 1rem 0;
        padding: 1rem;
      }

      .legend-item {
        display: flex;
        align-items: center;
        gap: 0.5rem;

        @media screen and (max-width: 767.8px) {
          justify-content: center;
        }

        &:nth-child(1) {
          @media screen and (max-width: 767.8px) {
            grid-column: 1 / 3;
          }
        }

        &:nth-child(2) {
          @media screen and (max-width: 767.8px) {
            grid-column: 3 / 5;
          }
        }

        &:nth-child(3) {
          @media screen and (max-width: 767.8px) {
            grid-column: 5 / 7;
          }
        }

        &:nth-child(4) {
          @media screen and (max-width: 767.8px) {
            grid-column: 2 / 4;
          }
        }

        &:nth-child(5) {
          @media screen and (max-width: 767.8px) {
            grid-column: 4 / 6;
          }
        }

        .legend-color {
          width: 18px;
          height: 18px;
          border-radius: 50%;
          display: inline-block;
          flex-shrink: 0;
        }

        .legend-label {
          font-size: 18px;
          color: #010b18;
          font-weight: 500;
          white-space: nowrap;
          font-family: 'Avenir', sans-serif;

          @media screen and (max-width: 767.8px) {
            font-size: 2.25rem;
          }
        }
      }
    }
  }
  </style>