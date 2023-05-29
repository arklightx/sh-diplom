<template>
  <v-container>
    <v-row no-gutters>
      <v-col class="col col-1 d-none d-md-block"></v-col>
      <v-col class="col col-12 col-md-10">
        <v-card>
          <v-card-title>Голосования</v-card-title>
          <v-card-subtitle>Активные</v-card-subtitle>
          <v-card-text>
            <vote-item @onVoteSend="sendVote" class="mb-3" :key="key" :item="vote"
              v-for="(vote, key) in activeVotings"></vote-item>
            <div class="d-flex justify-center flex-column">
              <vote-form @submit="submitVote" v-if="suggestStatus"></vote-form>
              <v-btn @click="suggestStatus = !suggestStatus" class="align-self-center mt-2">
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
            <vote-item class="mb-3" :key="key" :item="vote" v-for="(vote, key) in unactiveVotings"></vote-item>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col class="d-none d-md-block"> </v-col>
    </v-row>
  </v-container>
</template>
<script>
import Swal from "sweetalert2";
import VoteForm from "~/components/LK/VoteForm.vue";
import NewsItem from "@/components/news/NewsItem.vue";
import HomeItem from "@/components/homes/HomeItem.vue";
import QuestionForm from "~/components/faq/QuestionForm.vue";
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

      this.$axios
        .get(`api/v1/votes/${this.home.id}`, {
          withCredentials: true,
          headers: { Authorization: `Bearer ${this.token}` },
        })
        .then((res) => {
          this.votings = res.data;
        });
    }, 200);
  },
  data() {
    return {
      showJitsy: false,
      suggestStatus: false,
      votings: [],
    };
  },
  methods: {
    submitVote(data) {
      this.$axios
        .post(
          `api/v1/createvote/`,
          {
            user: this.user.id,
            home: this.home.id,
            theme: data.theme,
            variant: data.variants,
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
            title: "Голосование отправлено!",
            showConfirmButton: false,
            timer: 3000,
          });
        });
    },
    sendVote(item) {
      const selectedId = item.variants.find((i) => i.label === item.userVariant).id;
      this.$axios
        .post(
          `api/v1/vote-user/`,
          { id: selectedId },
          {
            withCredentials: true,
            headers: { Authorization: `Bearer ${this.token}` },
          }
        )
        .then((res) => {
          Swal.fire({
            position: "center",
            icon: "success",
            title: "Голос отправлен!",
            showConfirmButton: false,
            timer: 3000,
          });
        });
    },
  },
  computed: {
    user() {
      return { ...this.$store.getters["auth/getUser"] };
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
  },
};
</script>

<style>
.main_img {
  margin-top: -25px;
}
</style>
