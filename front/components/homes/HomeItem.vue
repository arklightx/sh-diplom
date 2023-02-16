<template>
  <v-card color="blue-grey darken-4" elevation="5" class="mb-4">
    <div class="d-flex align-center flex-column">
      <v-img width="200" :src="require('@/assets/images/home_illustration.png')"> </v-img>
      <v-card-title> {{ item.street }} {{ item.home_number }} </v-card-title>
      <v-card-text class="d-flex align-center flex-column">
        <div class="d-flex align-center mb-2">
          <v-icon class="mr-2">mdi-vector-square-plus</v-icon>
          {{ item.area }} м ²
        </div>
        <div class="d-flex align-center mb-2">
          <v-icon class="mr-2">mdi-home-city</v-icon>
          {{ item.appartments }} кв
        </div>
        <div class="d-flex align-center mb-2">
          <v-icon class="mr-2">mdi-calendar-clock</v-icon>
          Построен в
          {{ item.create_dt.toString().split("-")[0] }} году
        </div>
      </v-card-text>
    </div>

    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn nuxt :to="`/homes/${item.id}`" color="primary lighten-2" text small>
        просмотреть
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "HomeItem",
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
