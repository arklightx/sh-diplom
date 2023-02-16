<template>
  <v-calendar
    width="60%"
    ref="calendar"
    v-model="value"
    :weekdays="weekday"
    :type="'month'"
    readonly
    @click:date="day"
    @click:event="emitEvent"
    :events="events"
    :event-overlap-mode="'stack'"
    :event-overlap-threshold="30"
  ></v-calendar>
</template>

<script>
export default {
  data() {
    return {
      value: "",
      weekday: [0, 1, 2, 3, 4, 5, 6],
    };
  },
  props: {
    events: [],
  },
  mounted() {
    console.log();
  },
  methods: {
    day(e) {
      // console.log(e)
    },
    emitEvent(e) {
      this.$emit("getEvent", e.event);
    },
  },
  watch: {
    value(val) {
      console.log(val);
    },
  },
};
</script>
