<template>
  <v-card color="blue-grey darken-4">
    <v-card-title>Предложить голосование</v-card-title>
    <v-form v-model="valid" @submit.prevent="submit" ref="form">
      <v-card-text>
        <v-text-field
          v-model="vote.theme"
          :rules="requiredRules"
          label="Тема опроса"
          outlined
          filled
        ></v-text-field>
        <v-divider class="mb-3"></v-divider>
        <div :key="key" v-for="(item, key) in vote.variants" class="d-flex">
          <v-text-field
            :rules="requiredRules"
            clearable
            v-model="vote.variants[key]"
            :label="`Вариант ${key + 1}`"
            outlined
            filled
          ></v-text-field>
          <v-btn class="mt-2 ml-2" small @click="remove(key)" color="warning" fab>
            <v-icon>mdi-close</v-icon>
          </v-btn>
        </div>

        <v-card-actions>
          <v-spacer />
          <v-btn @click="add" color="cyan" fab>
            <v-icon>mdi-plus</v-icon>
          </v-btn>
          <v-spacer />
        </v-card-actions>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn type="submit" color="primary">Отправить</v-btn>
      </v-card-actions>
    </v-form>
  </v-card>
</template>

<script>
export default {
  name: "Test",
  created() {},
  data() {
    return {
      valid: false,
      vote: {
        theme: "",
        variants: ["", ""],
      },
      requiredRules: [(v) => !!v || "Заполните поле"],
    };
  },
  props: {},
  methods: {
    remove(key) {
      if (this.vote.variants.length < 3) return;
      this.vote.variants.splice(key, 1);
    },
    add() {
      if (this.vote.variants.length > 6) return;
      this.vote.variants.push("");
    },
    submit() {
      this.$refs.form.validate();
      if (this.valid) {
        this.emit("submit", this.vote);
      }
    },
  },
};
</script>

<style lang="scss" scoped></style>
