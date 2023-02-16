<template>
  <v-card color="blue-grey darken-4">
    <v-form v-model="valid" @submit.prevent="submit">
      <v-card-title>Создать обращение</v-card-title>
      <v-card-text>
        <v-form @submit.prevent="submit" ref="form" v-model="valid">
          <v-text-field
            v-model="request.theme"
            required
            :rules="requiredRules"
            clearable
            outlined
            filled
            label="Тема обращения"
          />
          <v-textarea
            v-model="request.text"
            :rules="requiredRules"
            outlined
            filled
            label="Текст обращения"
          />
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-spacer />
        <v-btn type="submit" color="primary">Отправить</v-btn>
      </v-card-actions>
    </v-form>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      valid: false,
      requiredRules: [(v) => !!v || "Поле обязательно"],
      request: {
        theme: "",
        text: "",
      },
    };
  },
  methods: {
    submit() {
      this.$refs.form.validate();
      if (this.valid) {
        this.$emit("submit", this.request);
      }
    },
  },
};
</script>
