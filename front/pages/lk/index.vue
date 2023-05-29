<template>
  <v-container>
    <v-row no-gutters>
      <v-col class="col col-1 d-none d-md-block"></v-col>
      <v-col class="col col-12 col-md-10">
        <v-img class="d-flex text-center main_img align-center justify-center"
          gradient="to top right, rgba(0,0,0,.1), rgba(25,32,72,.8)" max-height="400px"
          :src="require('@/assets/images/lk_main.jpg')">
          <h1 class="text-h4 text-md-h2 mb-2 font-weight-medium">Личный кабинет</h1>
        </v-img>
        <v-card>
          <v-card-title>Личная информация</v-card-title>
          <v-card-text>
            <v-card color="blue-grey darken-4">
              <v-form @submit.prevent="submitInfo" ref="infoForm" v-model="infoValid" class="pa-3">
                <v-text-field v-model="user.second_name" filled required disabled outlined :rules="requiredRules"
                  label="Фамилия"></v-text-field>
                <v-text-field v-model="user.first_name" filled outlined disabled required :rules="requiredRules"
                  label="Имя"></v-text-field>
                <v-text-field v-model="user.middle_name" filled outlined disabled required :rules="requiredRules"
                  label="Отчество"></v-text-field>
                <v-text-field v-model="user.login" filled outlined disabled required :rules="requiredRules"
                  label="Логин"></v-text-field>
                <v-text-field v-model="user.email" filled required disabled :rules="emailRules" outlined
                  label="Почта"></v-text-field>
                <v-text-field filled outlined disabled v-model="user.password" required :rules="requiredRules"
                  type="password" label="Пароль"></v-text-field>
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
            <home-item v-if="home" :item="home"></home-item>
            <v-card class="mt-2">
              <v-card-title> Обращения </v-card-title>
              <v-card-text>
                <request-item class="mb-6" v-for="(item, key) in requests" :key="key" :item="item"></request-item>
                <div class="d-flex justify-center flex-column">
                  <request-form @submit="submitRequest" class="mt-4" v-if="suggestRequestStatus"></request-form>
                  <v-btn @click="suggestRequestStatus = !suggestRequestStatus" class="align-self-center mt-2">
                    <template v-if="!suggestRequestStatus">
                      Создать <v-icon right dark> mdi-plus </v-icon>
                    </template>
                    <template v-else>
                      Скрыть <v-icon right dark> mdi-minus </v-icon>
                    </template>
                  </v-btn>
                </div>
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
import { mapState } from "vuex";
import Swal from "sweetalert2";
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
import Jitsy from "~/components/UI/Jitsi.vue";
export default {
  components: {
    Jitsy,
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
  async created() {
    if (!this.user) {
      this.$router.push("/login");
    }
    setTimeout(() => {
      this.$axios
        .get(`api/v1/events/${this.home.id}`, {
          withCredentials: true,
          headers: { Authorization: `Bearer ${this.token}` },
        })
        .then((res) => {
          this.events = res.data;
        });

      this.$axios
        .get(`api/v1/requests/${this.home.id}`, {
          withCredentials: true,
          headers: { Authorization: `Bearer ${this.token}` },
        })
        .then((res) => {
          this.requests = res.data;
        });

    }, 200);
  },
  data() {
    return {
      events: [],
      infoValid: false,
      infoValid: false,
      emailRules: [
        (v) => !!v || "Почта обязательно",
        (v) => /.+@.+\..+/.test(v) || "Неверный формат почты",
      ],
      requiredRules: [(v) => !!v || "Поле обязательно"],
      suggestStatus: false,
      suggestRequestStatus: false,

      requests: [],
    };
  },
  methods: {
    submitRequest(data) {
      this.$axios
        .post(
          `api/v1/requests/`,
          {
            user: this.user.id,
            home: this.home.id,
            theme: data.theme,
            text: data.text,
          },
          {
            withCredentials: true,
            headers: { Authorization: `Bearer ${this.token}` },
          }
        )
        .then((res) => {
          Swal.fire({
            position: "center",
            icon: "success",
            title: "Запрос отправлен!",
            showConfirmButton: false,
            timer: 3000,
          });
        });
    },
    submitInfo() {
      this.$refs.infoForm.validate();
    },
  },
  computed: {
    user() {
      return { ...this.$store.getters["auth/getUser"] };
    },
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
    token() {
      return this.$store.getters["auth/getAccessToken"];
    },
    home() {
      if (this.user?.homes) {
        console.log(this.user);
        return this.user?.homes[0];
      }
      return false;
    },
  },
};
</script>

<style>
.main_img {
  margin-top: -25px;
}
</style>
