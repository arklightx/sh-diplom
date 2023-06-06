<template>
  <v-container>
    <v-row no-gutters>
      <v-col class="col col-1 d-none d-md-block"></v-col>
      <v-col class="col col-12 col-md-10">
        <v-card class="mt-2">
          <v-card-title>Ваш дом</v-card-title>
          <v-card-text>
            <v-card-title>Видеособрания жильцов</v-card-title>
            <Jitsy v-if="showJitsy" :homeId="home.id" />
            <div class="d-flex justify-center flex-column">
              <v-btn @click="showJitsy = false" v-if="showJitsy" primary>
                Отключиться</v-btn>
              <v-btn @click="showJitsy = true" v-else primary> Подключиться</v-btn>
            </div>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col class="d-none d-md-block"> </v-col>
    </v-row>
  </v-container>
</template>
<script>
import Swal from "sweetalert2";
import groupByKey from "~/helpers/groupByKey.js";
import Jitsy from "~/components/UI/Jitsi.vue";
export default {
  components: {
    Jitsy,
  },
  async created() {
    if (!this.user) {
      this.$router.push("/login");
    }
  },
  data() {
    return {
      showJitsy: false,
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
