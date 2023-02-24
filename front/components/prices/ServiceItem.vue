<template>
  <v-card hover color="blue-grey darken-4">
    <v-card-text class="d-flex justify-space-between">
      <div>
        {{ item.service }}
      </div>
      <div>
        {{ item.price }}
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  props: {
    item: {},
  },
};
</script>
