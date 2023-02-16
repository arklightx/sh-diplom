<template>
  <v-container>
    <v-row no-gutters>
      <v-col class="col col-1 d-none d-md-block"></v-col>
      <v-col class="col col-12 col-md-10">
        <v-img
          class="d-flex text-center main_img align-center justify-center"
          gradient="to top right, rgba(0,0,0,.1), rgba(25,32,72,.8)"
          @click="$router.push('/')"
          max-height="600px"
          :src="require('@/assets/images/news_main.png')"
        >
          <h1 class="text-h4 text-md-h2 mb-2 font-weight-medium">Новости</h1>
        </v-img>
        <v-card>
          <v-card-title>Последние новости</v-card-title>
          <v-text-field
            class="mx-4"
            v-model="query"
            placeholder="Поиск новости..."
            persistent-hint
            append-icon="mdi-magnify"
            filled
          ></v-text-field>
          <v-card-text>
            <news-item :item="item" :key="key" v-for="(item, key) in filteredNews" />
            <div class="d-flex justify-center">
              <v-btn
                v-if="news.length > filteredNews.length"
                @click="showMore"
                color="primary"
              >
                Больше
              </v-btn>
              <v-btn
                v-else-if="news.length == filteredNews.length && toShow > 2"
                @click="toShow = 2"
                color="primary"
              >
                Скрыть
              </v-btn>
            </div>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col class="d-none d-md-block"> </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "Test",
  data() {
    return {
      query: "",
      toShow: 2,
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
    };
  },
  methods: {
    showMore() {
      this.toShow += 5;
    },
    showLess() {
      this.toShow = 5;
    },
  },
  computed: {
    filteredNews() {
      return this.news.slice(0, this.toShow).filter((item) => {
        return (
          item.title.indexOf(this.query) != -1 ||
          item.description.indexOf(this.query) != -1
        );
      });
    },
  },
};
</script>

<style lang="scss" scoped>
.main_img {
  margin-top: -25px;
}
</style>
