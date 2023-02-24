<template>
  <v-container class="pa-2">
    <v-row no-gutters>
      <v-col class="col col-2 d-none d-flex"> </v-col>
      <v-col class="col col-md-8 col-12">
        <div class="mb-8">
          <Nuxt-link class="text-caption" to="/news">Ко всем новостям</Nuxt-link>
        </div>
        <v-card>
          <v-img
            class="d-flex text-center main_img align-center justify-center"
            gradient="to top right, rgba(0,0,0,.1), rgba(25,32,72,.8)"
            :src="newsItem.image"
            height="400"
          >
            <h1 class="text-h4 text-md-h2 mb-2 font-weight-medium">
              {{ newsItem.title }}
            </h1>
          </v-img>
          <v-card-text class="">
            <div class="d-flex justify-space-between align-center mt-4">
              <div>{{ newsItem.create_dt }}</div>
            </div>
            <div v-html="newsItem.description" class="news-paragraph-image mt-4" />
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn disabled>{{ moment(newsItem.create_at).format('MM-DD-YYYY HH:mm') }}</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
      <v-col class="col d-none d-flex"></v-col>
    </v-row>
  </v-container>
</template>
<script>
import { mapState } from "vuex";
import moment from "moment"
export default {
  created() {
    this.moment = moment
    this.id = this.$route.params.id;
    console.log(moment)

    this.$axios
      .get(`api/v1/news/${this.id}`)
      .then((res) => {
        this.newsItem = res.data;
        console.log(this.newsItem)
      })
      .catch((err) => {
        this.error = err;
      });
  },
  data() {
    return {
      to: false,
      id: -1,
      newsItem: {
        id: 1,
        title: "asdasd",
        create_dt: 123123,
        description: "lorem	insdsd adsjasdan cncjoa weqweqw xmzxoos qweqwe",
        image: "",
      },
    };
  },
  methods: {},
  computed: {
    ...mapState("auth", ["accessToken", "base"]),
    user: {
      get() {
        return this.$store.getters["auth/getUser"];
      },
      set(newValue) {
        this.$store.commit("auth/setUser", newValue);
      },
    },
  },
};
</script>
<style scoped>
.w-70 {
  width: 70% !important;
}

.w-100 {
  width: 100% !important;
}
.comments {
  margin: 0 auto;
}
</style>

<style>
.news-paragraph-image img {
  max-width: 100% !important;
}
</style>
