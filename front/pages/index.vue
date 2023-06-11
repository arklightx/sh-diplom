<template>
  <v-container>
    <v-row no-gutters>
      <v-col class="col col-1 d-none d-md-block"></v-col>
      <v-col class="col col-12 col-md-10">
        <v-img class="d-flex text-center main_img align-center justify-center"
          gradient="to top right, rgba(0,0,0,.1), rgba(25,32,72,.8)" max-height="600px"
          :src="require('@/assets/images/main.jpg')">
          <div class="body-1">ООО "Управляющая компания"</div>
          <h1 class="text-h4 text-md-h2 mb-2 font-weight-medium">
            На страже вашего дома
          </h1>
        </v-img>
        <v-card>
          <v-card-title>Последние новости</v-card-title>
          <v-card-text>
            <news-item :item="item" :key="key" v-for="(item, key) in computedNews">
            </news-item>
            <div class="d-flex align-center justify-center">
              <v-btn @click="$router.push('/news')" color="primary">Смотреть все</v-btn>
            </div>
          </v-card-text>
        </v-card>
        <v-card class="mt-2">
          <v-card-title>Наши дома</v-card-title>
          <v-card-text>
            <div class="d-flex flex-wrap w-100 justify-space-between">
              <home-item class="w-50" :item="item" :key="key" v-for="(item, key) in computedHomes"></home-item>
            </div>
            <div class="d-flex align-center justify-center">
              <v-btn @click="$router.push('/homes')" color="primary">Смотреть все</v-btn>
            </div>
          </v-card-text>
        </v-card>
        <v-card class="mt-2">
          <v-card-title>Хотите задать вопрос?</v-card-title>
          <v-card-text>
            <div v-if="Object.keys(groupedQuestions).length > 0" v-for="(value, name) in groupedQuestions" class="pt-2"
              :key="name">
              <div v-if="value.length != 0" class="py-4">
                <v-chip>
                  {{ name }}
                </v-chip>
              </div>
              <v-expansion-panels v-for="(item, index) in value" :key="index">
                <v-expansion-panel class="blue-grey darken-4 mb-2">
                  <v-expansion-panel-header>
                    {{ item.question }}
                  </v-expansion-panel-header>
                  <v-expansion-panel-content>
                    {{ item.answer }}
                  </v-expansion-panel-content>
                </v-expansion-panel>
              </v-expansion-panels>
            </div>
            <div class="d-flex align-center justify-center">
              <v-btn @click="$router.push('/faq')" color="primary">Смотреть все</v-btn>
            </div>
            <!-- <h1 class="text-h5 mt-6 my-4">Не нашли вопрос? Задайте свой!</h1> -->
            <!-- <question-form @suggestQuestion="suggestQuestion"></question-form> -->
          </v-card-text>
        </v-card>
      </v-col>
      <v-col class="d-none d-md-block"> </v-col>
    </v-row>
  </v-container>
</template>

<script>
import NewsItem from "@/components/news/NewsItem.vue";
import HomeItem from "@/components/homes/HomeItem.vue";
import QuestionForm from "~/components/faq/QuestionForm.vue";
import groupByKey from "~/helpers/groupByKey.js";
export default {
  components: {
    NewsItem,
    HomeItem,
    QuestionForm,
  },
  created() {
    this.$axios.get("/api/v1/homes").then(
      res => {
        this.homes = res.data
        console.log(this.homes)
      }
    )
    this.$axios.get("/api/v1/news").then(
      res => {
        this.news = res.data
      }
    )
    this.$axios.get("api/v1/questions").then((res) => {
      this.questions = res.data;
    });

  },
  data() {
    return {
      news: [
        {
          id: 1,
          title: "asdasd",
          create_at: 123123,
          description: "lorem	insdsd adsjasdan cncjoa weqweqw xmzxoos qweqwe",
          image: "",
        },
        {
          id: 1,
          title: "asdasd",
          create_at: 123123,
          description: "lorem	insdsd adsjasdan cncjoa weqweqw xmzxoos qweqwe",
          image: "",
        },
        {
          id: 1,
          title: "asdasd",
          create_at: 123123,
          description: "lorem	insdsd adsjasdan cncjoa weqweqw xmzxoos qweqwe",
          image: "",
        },
        {
          id: 1,
          title: "asdasd",
          create_at: 123123,
          description: "lorem	insdsd adsjasdan cncjoa weqweqw xmzxoos qweqwe",
          image: "",
        },
        {
          id: 1,
          title: "asdasd",
          create_at: 123123,
          description: "lorem	insdsd adsjasdan cncjoa weqweqw xmzxoos qweqwe",
          image: "",
        },
      ],
      homes: [
        {
          id: 1,
          street: "asdasd",
          home_number: 1233,
          area: "123123.23",
          create_dt: 20,
        },
        {
          id: 1,
          street: "asdasd",
          home_number: 1233,
          area: "123123.23",
          create_dt: 20,
        },
      ],
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
    suggestQuestion(question) {
      this.$axios
        .post("api/v1/questions/", {
          author_email: question.email,
          question: question.question,
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
    computedNews() {
      return this.news.slice(0, 4);
    },
    computedHomes() {
      return this.homes.slice(0, 4);
    },
    groupedQuestions() {
      return groupByKey("theme", this.questions);
    },
  },
};
</script>

<style>
.w-50 {
  width: 49% !important;
  position: relative;

}

.main_img {
  margin-top: -25px;
}

.w-100 {
  width: 100%;
}
</style>
