<template>
  <v-card>
    <v-card-title class="primary--text">{{ event.name }}</v-card-title>
    <v-card-text>
      {{ event.description }}
    </v-card-text>
    <v-card-actions>
      <v-spacer />
      <v-btn disabled>
        <v-icon>mdi-calendar</v-icon>
        {{ $moment(event.start).format("MM-DD-YYYY") }}
        <template> по {{ $moment(event.end).format("MM-DD-YYYY") }} </template>
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  data() {
    return {};
  },
  props: {
    event: {},
  },
  mounted() {},
  methods: {
    moment(date) {
      return moment(date);
    },
  },
};
</script>

<style></style>
