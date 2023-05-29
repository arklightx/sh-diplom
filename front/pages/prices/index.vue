<template>
  <v-container>
    <v-row no-gutters>
      <v-col class="col col-1 d-none d-md-block"></v-col>
      <v-col class="col col-12 col-md-10">
        <v-img class="d-flex text-center main_img align-center justify-center"
          gradient="to top right, rgba(0,0,0,.1), rgba(25,32,72,.8)" @click="$router.push('/')" max-height="600px"
          :src="require('@/assets/images/price_main.png')">
          <h1 class="text-h4 text-md-h2 mb-2 font-weight-medium">
            Прайс-лист платных услуг
          </h1>
        </v-img>
        <v-card>
          <v-card-title>Мы оказываем услуги</v-card-title>
          <v-text-field class="mx-4" v-model="query" placeholder="Поиск услуги..." persistent-hint
            append-icon="mdi-magnify" filled></v-text-field>
          <v-card-text>
            <div v-if="Object.keys(groupedServices).length > 0" v-for="(value, name) in groupedServices" class="pt-2"
              :key="name">
              <div v-if="value.length != 0" class="py-4">
                <v-chip>
                  {{ name }}
                </v-chip>
              </div>
              <div v-for="(item, index) in value" :key="index">
                <div class="blue-grey darken-4 mb-2">
                  <service-item :item="item"></service-item>
                </div>
              </div>
            </div>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col class="d-none d-md-block"> </v-col>
    </v-row>
  </v-container>
</template>

<script>
import groupByKey from "~/helpers/groupByKey";
import ServiceItem from "~/components/prices/ServiceItem.vue";
export default {
  name: "Test",
  components: {
    ServiceItem,
  },
  created() {
    this.$axios
      .get(`api/v1/company`, {
        withCredentials: true,
        headers: { Authorization: `Bearer ${this.token}` },
      })
      .then((res) => {
        this.services = res.data[0].services
        console.log()
      });
  },
  data() {
    return {
      query: "",
      toShow: 2,
      services: [],
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
    filteredServices() {
      return this.services.filter(
        (item) =>
          item.service_name.trim().toLowerCase().indexOf(this.query.trim().toLowerCase()) != -1)
    },
    groupedServices() {
      return groupByKey("group", this.filteredServices);
    },
  },
};
</script>

<style lang="scss" scoped>
.main_img {
  margin-top: -25px;
}
</style>
