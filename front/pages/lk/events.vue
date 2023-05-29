<template>
  <v-container>
    <v-row no-gutters>
      <v-col class="col col-1 d-none d-md-block"></v-col>
      <v-col class="col col-12 col-md-10">
        <v-card class="mt-2">
          <v-card-title>
            События
          </v-card-title>
          <v-card-text>
            <events-block class="mt-4" :events="events" />
          </v-card-text>
        </v-card>
      </v-col>
      <v-col class="d-none d-md-block"> </v-col>
    </v-row>
  </v-container>
</template>
<script>
import EventsBlock from "~/components/LK/EventsBlock.vue";
export default {
  components: {
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

    }, 200);
  },
  data() {
    return {
      showJitsy: false,
      events: [],
    };
  },

  computed: {
    user() {
      return { ...this.$store.getters["auth/getUser"] };
    },

    token() {
      return this.$store.getters["auth/getAccessToken"];
    },
    home() {
      if (this.user?.homes) {
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
