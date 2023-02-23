<template>
  <v-container>
    <v-row no-gutters>
      <v-col class="col col-1" />
      <v-col class="col col-md-10 col-12 pa-2 pt-0">
        <v-img
          class="d-flex text-center main_img align-center justify-center"
          gradient="to top right, rgba(0,0,0,.1), rgba(25,32,72,.8)"
          max-height="400px"
          :src="require('@/assets/images/faq_main.png')"
        >
          <h1 class="text-h4 text-md-h2 mb-2 font-weight-medium">FAQ</h1>
        </v-img>
        <v-text-field
          class="courses__input_search mt-2"
          placeholder="Поиск вопросов..."
          persistent-hint
          append-icon="mdi-magnify"
          filled
          v-model="query"
        >
        </v-text-field>

        <h1 class="text-h5 mb-0">Самые волнующие вопросы</h1>
        <div
          v-if="Object.keys(filteredQuestions).length > 0"
          v-for="(value, name) in filteredQuestions"
          class="pt-2"
          :key="name"
        >
          <div v-if="value.length != 0" class="py-4">
            <v-chip>
              {{ name }}
            </v-chip>
          </div>
          <v-expansion-panels v-for="(item, index) in value" :key="index">
            <v-expansion-panel class="mb-1 blue-grey darken-4">
              <v-expansion-panel-header>
                {{ item.question }}
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                {{ item.answer }}
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>
        </div>
        <h1 class="text-h5 mt-6 my-4">Не нашли вопрос? Задайте свой!</h1>
        <QuestionForm @suggestQuestion="suggestQuestion" id="ask" />
      </v-col>
      <v-col class="col d-none d-md-block"> </v-col>
    </v-row>
  </v-container>
</template>

<script>
import QuestionForm from "@/components/faq/QuestionForm";
import Swal from "sweetalert2";
export default {
  components: {
    QuestionForm,
  },
  created() {
    // await this.$store.dispatch("faq/setQuestions").then((res) => {});
    // this.questions = this.$store.getters["faq/getQuestions"];
    this.$axios.get("api/v1/questions").then((res) => {
      this.questions = res.data;
      this.groupQuestions();
    });
    this.groupQuestions();
  },
  data() {
    return {
      filters: {
        reverse: false,
        selectedTag: "",
      },

      query: "",
      questions: [
        {
          theme: "Смерть всему живому",
          question: "АААА?",
          answer: "aaaa",
        },
        {
          theme: "Смерть всему живому",
          question: "АААА?",
          answer: "aaaa",
        },
      ],
    };
  },

  methods: {
    applyFilters(filters) {
      this.filters = filters;
    },
    groupQuestions() {
      let themes = [];
      let groupedQuestions = {};
      for (let quest of this.questions) {
        let currentTheme = quest.theme;
        if (themes.includes(currentTheme)) {
          groupedQuestions[currentTheme].push({
            question: quest.question,
            answer: quest.answer,
            tags: quest.tags,
          });
        } else {
          groupedQuestions[currentTheme] = [
            {
              question: quest.question,
              answer: quest.answer,
              tags: quest.tags,
            },
          ];
        }
        themes.push(currentTheme);
      }
      this.questions = groupedQuestions;

    },
    suggestQuestion(question) {
      this.$axios
        .post("api/v1/questions/", {
          ...question
        })
        .then((res) => {
          Swal.fire({
            position: "center",
            icon: "success",
            title: "Вопрос отправлен!",
            showConfirmButton: false,
            timer: 3000,
          });
        })
        .catch((res) => {
          Swal.fire({
            position: "center",
            icon: "error",
            title: "Что-то пошло не так",
            showConfirmButton: false,
            timer: 3000,
          });
        });
    },
  },
  computed: {
    filteredQuestions() {
      let questions = { ...this.questions };
      console.log(questions)
      let keys = Object.keys(questions);
      for (let key of keys) {
        console.log(questions[key])
        let filteredQuestion = questions[key].filter((item) => {
          if (
            item.question
              .toLowerCase()
              .trim()
              .includes(this.query.toLowerCase().trim()) ||
            item.answer.toLowerCase().trim().includes(this.query.toLowerCase().trim())
          ) {
            return item;
          }
        });
        if (filteredQuestion) {
          questions[key] = filteredQuestion;
        } else {
          questions[key] = questions[key];
        }
      }
      return questions;
    },
  },
};
</script>

<style lang="scss" scoped>
.main_img {
  margin-top: -25px;
}
</style>
