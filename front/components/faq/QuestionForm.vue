<template>
  <v-card color="blue-grey darken-4" class="my-2">
    <v-form>
      <v-card-title> Ваш вопрос </v-card-title>
      <v-card-text>
        <v-text-field
          label="Ваша почта"
          placeholder="e-mail"
          solo
          clearable
          required
          :error-messages="emailErrors"
          v-model="email"
          @input="$v.email.$touch()"
          @blur="$v.email.$touch()"
        ></v-text-field>
        <v-textarea
          label="Задайте вопрос"
          placeholder="Ваш вопрос"
          solo
          clearable
          v-model="question"
          required
          :error-messages="questionErrors"
          @input="$v.question.$touch()"
          @blur="$v.question.$touch()"
          counter="100"
        ></v-textarea>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn @click="suggestQuestion" color="primary">
          <caption>
            Отправить
          </caption>
        </v-btn>
      </v-card-actions>
    </v-form>
  </v-card>
</template>

<script>
import { validationMixin } from "vuelidate";
import { required, maxLength, minLength, email } from "vuelidate/lib/validators";
import Swal from "sweetalert2";

export default {
  mixins: [validationMixin],
  validations: {
    email: { required, email },
    question: { required, maxLength: maxLength(100), minLength: minLength(10) },
  },
  data() {
    return {
      email: "",
      question: "",
    };
  },
  methods: {
    suggestQuestion() {
      this.$v.$touch();
      if (this.$v.$anyError) {
        Swal.fire({
          position: "center",
          icon: "error",
          title: "Проверьте данные",
          showConfirmButton: false,
          timer: 3000,
        });
        return;
      }

      let email = this.email;
      let question = this.question;
      this.$emit("suggestQuestion", { email, question });
      this.question = this.email = "";
      this.$v.$reset();
    },
  },
  computed: {
    questionErrors() {
      const errors = [];
      if (!this.$v.question.$dirty) return errors;
      !this.$v.question.maxLength && errors.push("Слишком длинный вопрос");
      !this.$v.question.minLength && errors.push("Вопрос должен быть содержателен");
      !this.$v.question.required && errors.push("Введите вопрос");
      return errors;
    },
    emailErrors() {
      const errors = [];
      if (!this.$v.email.$dirty) return errors;
      !this.$v.email.email && errors.push("Неверный формат почты");
      !this.$v.email.required && errors.push("Укажите электронную почту");
      return errors;
    },
  },
};
</script>
