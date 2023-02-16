<template>
  <v-card class="pos-r" color="blue-grey darken-4">
    <v-chip class="status">{{ item.status }}</v-chip>
    <v-card-title class="text--primary">{{ item.text }}</v-card-title>
    <v-card-subtitle>Дата обращения: {{ item.create_dt }} <br>Тема: {{ item.theme }}</v-card-subtitle>
    <v-card-subtitle></v-card-subtitle>
    <v-card-text>
      Ответ:
      <template v-if="item.response">
        {{ item.response }}
      </template>
      <template v-else> Здесь будет отображён ответ после обработки запроса </template>
    </v-card-text>
    <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn disabled>Завершено {{ item.done_dt }}</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: {
    item: {},
  },
};
</script>

<style>
    .pos-r{
        position: relative !important;
    }
    .status{
        position: absolute !important;
        top: -16px;
        right: 0;
    }
</style>
