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
          :src="require('@/assets/images/homes_main.png')"
        >
          <h1 class="text-h4 text-md-h2 mb-2 font-weight-medium">Наши дома</h1>
        </v-img>
        <v-card>
          <v-card-title>Нашими услугами пользуются</v-card-title>
          <v-text-field
            class="mx-4"
            v-model="query"
            placeholder="Поиск домов..."
            persistent-hint
            append-icon="mdi-magnify"
            filled
          ></v-text-field>
          <v-card-text>
            <div class="d-flex flex-wrap justify-space-between">
              <home-item
                class="w-50"
                :item="item"
                :key="key"
                v-for="(item, key) in filteredHomes"
              />
            </div>

            <div class="d-flex justify-center">
              <v-btn
                v-if="homes.length > filteredHomes.length"
                @click="showMore"
                color="primary"
              >
                Больше
              </v-btn>
              <v-btn
                v-else-if="homes.length == filteredHomes.length && toShow > 2"
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
import HomeItem from "~/components/homes/HomeItem.vue";
export default {
  name: "Homes",
  components: {
    HomeItem,
  },
  created(){
    this.$axios.get("/api/v1/homes").then(
      res=>{
        this.homes = res.data
        console.log(this.homes)
      }
    )

  },
  data() {
    return {
      query: "",
      toShow: 2,
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
    filteredHomes() {
      return this.homes.slice(0, this.toShow).filter((item) => {
        return (
          (item.street + item.home_number)
            .replaceAll(" ", "")
            .indexOf(this.query.replaceAll(" ", "")) != -1
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
.w-50 {
  width: 49%;
}
</style>
