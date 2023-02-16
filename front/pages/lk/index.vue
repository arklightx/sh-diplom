<template>
  <v-container>
    <v-row no-gutters>
      <v-col class="col col-1 d-none d-md-block"></v-col>
      <v-col class="col col-12 col-md-10">
        <v-img
          class="d-flex text-center main_img align-center justify-center"
          gradient="to top right, rgba(0,0,0,.1), rgba(25,32,72,.8)"
          max-height="400px"
          :src="require('@/assets/images/lk_main.jpg')"
        >
          <h1 class="text-h4 text-md-h2 mb-2 font-weight-medium">Личный кабинет</h1>
        </v-img>
        <v-card>
          <v-card-title>Личная информация</v-card-title>
          <v-card-text>
            <v-card color="blue-grey darken-4">
              <v-form
                @submit.prevent="submitInfo"
                ref="infoForm"
                v-model="infoValid"
                class="pa-3"
              >
                <v-text-field
                  v-model="user.second_name"
                  filled
                  required
                  outlined
                  :rules="requiredRules"
                  label="Фамилия"
                ></v-text-field>
                <v-text-field
                  v-model="user.first_name"
                  filled
                  outlined
                  required
                  :rules="requiredRules"
                  label="Имя"
                ></v-text-field>
                <v-text-field
                  v-model="user.middle_name"
                  filled
                  outlined
                  required
                  :rules="requiredRules"
                  label="Отчество"
                ></v-text-field>
                <v-text-field
                  v-model="user.login"
                  filled
                  outlined
                  required
                  :rules="requiredRules"
                  label="Логин"
                ></v-text-field>
                <v-text-field
                  v-model="user.email"
                  filled
                  required
                  :rules="emailRules"
                  outlined
                  label="Почта"
                ></v-text-field>
                <v-text-field
                  filled
                  outlined
                  v-model="user.password"
                  required
                  :rules="requiredRules"
                  type="password"
                  label="Пароль"
                ></v-text-field>
                <v-card-actions>
                  <v-spacer></v-spacer> <v-btn color="primary">Сохранить</v-btn>
                </v-card-actions>
              </v-form>
            </v-card>
          </v-card-text>
        </v-card>
        <v-card class="mt-2">
          <v-card-title>Ваш дом</v-card-title>
          <v-card-text>
            <home-item :item="home"></home-item>
            <v-card>
              <v-card-title class="mb-3">Голосования</v-card-title>
              <v-card-subtitle>Активные</v-card-subtitle>
              <v-card-text>
                <vote-item
                  class="mb-3"
                  :key="key"
                  :item="vote"
                  v-for="(vote, key) in activeVotings"
                ></vote-item>
                <div class="d-flex justify-center flex-column">
                  <vote-form v-if="suggestStatus"></vote-form>
                  <v-btn
                    @click="suggestStatus = !suggestStatus"
                    class="align-self-center mt-2"
                  >
                    <template v-if="!suggestStatus">
                      Предложить <v-icon right dark> mdi-plus </v-icon>
                    </template>
                    <template v-else>
                      Скрыть <v-icon right dark> mdi-minus </v-icon>
                    </template>
                  </v-btn>
                </div>
              </v-card-text>
              <v-card-subtitle>Завершённые</v-card-subtitle>
              <v-card-text>
                <vote-item
                  class="mb-3"
                  :key="key"
                  :item="vote"
                  v-for="(vote, key) in unactiveVotings"
                ></vote-item>
              </v-card-text>
            </v-card>
            <v-card class="mt-2">
              <v-card-title> Обращения </v-card-title>
              <v-card-text>
                <request-item
                  v-for="(item, key) in requests"
                  :key="key"
                  :item="item"
                ></request-item>
                <div class="d-flex justify-center flex-column">
                  <request-form class="mt-4" v-if="suggestRequestStatus"></request-form>
                  <v-btn
                    @click="suggestRequestStatus = !suggestRequestStatus"
                    class="align-self-center mt-2"
                  >
                    <template v-if="!suggestRequestStatus">
                      Создать <v-icon right dark> mdi-plus </v-icon>
                    </template>
                    <template v-else>
                      Скрыть <v-icon right dark> mdi-minus </v-icon>
                    </template>
                  </v-btn>
                </div>
                <events-block class="mt-4" :events="events" />
              </v-card-text>
            </v-card>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col class="d-none d-md-block"> </v-col>
    </v-row>
  </v-container>
</template>
<script>
import VoteForm from "~/components/LK/VoteForm.vue";
import NewsItem from "@/components/news/NewsItem.vue";
import HomeItem from "@/components/homes/HomeItem.vue";
import QuestionForm from "~/components/faq/QuestionForm.vue";
import groupByKey from "~/helpers/groupByKey.js";
import VoteItem from "~/components/LK/VoteItem.vue";
import RequestForm from "~/components/LK/RequestForm.vue";
import RequestItem from "~/components/LK/RequestItem.vue";
import EventsCalendar from "~/components/LK/EventsCalendar.vue";
import EventsBlock from "~/components/LK/EventsBlock.vue";
export default {
  components: {
    NewsItem,
    HomeItem,
    VoteItem,
    RequestItem,
    RequestForm,
    QuestionForm,
    VoteForm,
    EventsCalendar,
    EventsBlock,
  },
  data() {
    return {
      events: [
        {
          name: "Я ненавижу галкина",
          start:  new Date().setDate(new Date().getDate() + 3),
          end: new Date().setDate(new Date().getDate() + 6),
          timed: true,
          color: "blue",
          description: "asdasd"
        },
        {
          name: "Я ненавижу галкина и пугачёву",
          start: new Date(),
          end: new Date().setDate(new Date().getDate() + 4),
          timed: true,
        },
      ],
      infoValid: false,
      infoValid: false,
      emailRules: [
        (v) => !!v || "Почта обязательно",
        (v) => /.+@.+\..+/.test(v) || "Неверный формат почты",
      ],
      requiredRules: [(v) => !!v || "Поле обязательно"],
      user: {
        first_name: "",
        second_name: "",
        middle_name: "",
        login: "",
        email: "",
        password: "",
      },
      suggestStatus: false,
      home: {
        id: 1,
        street: "asdasd",
        home_number: 1233,
        area: "123123.23",
        create_dt: 20,
      },
      suggestRequestStatus: false,
      votings: [
        {
          theme: "Что с тобой делать?",
          isActive: true,
          variants: [
            { label: "Сломать колени", votes: 23 },
            { label: "Дать леща", votes: 13 },
          ],
          userVariant: "Сломать колени",
        },
        {
          theme: "Идут как-то к рельсам",
          isActive: false,
          variants: [
            { label: "Два муравья", votes: 23 },
            { label: "Два лося", votes: 3 },
            { label: "Дважды два = 4", votes: 3 },
          ],
          userVariant: "Два лося",
        },
      ],
      requests: [
        {
          status: "Выполняется",
          create_dt: "12.09.2022",
          theme: "Телефон!",
          text: "Провод сгрылзли гриззли",
          done_dt: "13.10.2022",
          response: "Провод вгрызли обратно",
        },
      ],
    };
  },
  methods: {
    submitInfo() {
      this.$refs.infoForm.validate();
      console.log(this.infoForm);
    },
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
    activeVotings() {
      return this.votings.filter((item) => item.isActive);
    },
    unactiveVotings() {
      return this.votings.filter((item) => !item.isActive);
    },
  },
};
</script>

<style>
.main_img {
  margin-top: -25px;
}
</style>
