<template>
  <v-card height="600px" color="blue-grey darken-4">
    <div class="d-flex h-100 pa-2 justify-space-between">
      <events-calendar class="w-60" @getEvent="getEvent" :events="events"></events-calendar>
      <div class="ml-4 w-40">
        <event-item v-if="currentEvent" :event="currentEvent"></event-item>
        <v-alert v-else outlined type="info">
          Здесь отобразится информация о событии
        </v-alert>
      </div>
    </div>
  </v-card>
</template>

<script>
import EventsCalendar from "./EventsCalendar.vue";
import EventItem from "./EventItem.vue";
export default {
  components: {
    EventsCalendar,
    EventItem,
  },
  data() {
    return {
      currentEvent: false,
    };
  },
  props: {
    events: [],
  },
  methods: {
    getEvent(e) {
      this.currentEvent = e;
    },
  },
};
</script>

<style>
.w-60 {
  width: 60%;
}

.h-100 {
  height: 100%;
}

.w-40 {
  width: 40%;
}
</style>
