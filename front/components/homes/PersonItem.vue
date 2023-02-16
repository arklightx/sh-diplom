<template>
  <v-card color="blue-grey darken-3">
    <v-card-text class="d-flex">
      <v-avatar width="150px" height="150px">
        <v-img
          gradient="to top right, rgba(0,0,0,.1), rgba(25,32,72,.8)"
          :src="require('~/assets/images/avatar.jpg')"
        >
        </v-img>
      </v-avatar>

      <div class="d-flex flex-column">
        <v-card-title>
          {{ item.last_name }} {{ item.first_name }} {{ item.middle_name }}
        </v-card-title>
        <v-card-subtitle class="mt-2">
          {{ item.role }}
        </v-card-subtitle>
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "Test",
  created() {},
  data() {
    return {};
  },
  props: {
    item: {},
  },
  methods: {},
};
</script>

<style lang="scss" scoped></style>
