<template>
  <v-container>
    <v-row no-gutters>
      <v-col class="col col-1 d-none d-md-block"></v-col>
      <v-col class="col col-12 col-md-10">
        <v-card class="mt-2">
          <v-card-title>Ваш дом</v-card-title>
          <v-card-text>
            <home-item v-if="home" :item="home"></home-item>
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
import HomeItem from "@/components/homes/HomeItem.vue";
export default {
  components: {
    HomeItem,
  },
  async created() {
    if (!this.user) {
      this.$router.push("/login");
    }
  },

  methods: {

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
