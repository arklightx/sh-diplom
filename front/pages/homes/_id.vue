<template>
  <v-container class="pa-2">
    <v-row no-gutters>
      <v-col class="col col-2 d-none d-flex"> </v-col>
      <v-col class="col col-md-8 col-12">
        <div class="mb-2">
          <Nuxt-link class="text-caption" to="/homes">Ко всем домам</Nuxt-link>
        </div>
        <v-card v-if="home">
          <v-card-text class="d-flex">
            <v-img
              height="250px"
              max-width="300px"
              :src="require('@/assets/images/home_illustration.png')"
            >
            </v-img>
            <div>
              <v-card-title class="primary--text">
                {{ home.street }}
                {{ home.home_number }}
              </v-card-title>
              <div class="mb-4">Краткая информация о доме</div>
              <div class="d-flex align-center mb-2">
                <v-icon class="mr-2">mdi-vector-square-plus</v-icon>
                {{ home.area }} м ²
              </div>
              <div class="d-flex align-center mb-2">
                <v-icon class="mr-2">mdi-home-city</v-icon>
                {{ appartments }} кв
              </div>
              <div class="d-flex align-center mb-2">
                <v-icon class="mr-2">mdi-calendar-clock</v-icon>
                Построен в
                {{ moment(home.create_dt).format("YYYY") }} году
              </div>
              <div class="d-flex align-center mb-2">
                <v-icon class="mr-2">mdi-home-floor-l</v-icon>
                количество этажей
                {{ home.levels.length }}
              </div>
            </div>
          </v-card-text>

          <v-card-text class="">
            <v-expansion-panels>
              <v-expansion-panel class="mb-1 blue-grey darken-4">
                <v-expansion-panel-header>
                  Просмотреть отключения
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                  <v-data-table
                    :headers="headers"
                    :items="disablings"
                    :items-per-page="5"
                    class="elevation-1"
                  ></v-data-table>
                </v-expansion-panel-content>
              </v-expansion-panel>
              <v-expansion-panel class="mb-1 blue-grey darken-4">
                <v-expansion-panel-header>
                  Просмотреть документы
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                  <div
                    v-if="Object.keys(groupedDocuments).length > 0"
                    v-for="(value, name) in groupedDocuments"
                    class="pt-2"
                    :key="name"
                  >
                    <div v-if="value.length != 0" class="py-4">
                      <v-chip>
                        {{ name }}
                      </v-chip>
                    </div>
                    <div v-for="(item, index) in value" :key="index">
                      <div class="blue-grey darken-4 mb-2">
                        <a :href="item.file">
                          {{ item.title }}
                        </a>
                      </div>
                    </div>
                  </div>
                </v-expansion-panel-content>
              </v-expansion-panel>
            </v-expansion-panels>
            <v-card class="mt-4 blue-grey darken-4">
              <v-card-title> Дом обслуживают</v-card-title>
              <div class="pa-4">
                <person-item class="mb-2"
                  v-for="(item, key) in home.staffs"
                  :key="key"
                  :item="item"
                ></person-item>
              </div>
            </v-card>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-col>
      <v-col class="col d-none d-flex"></v-col>
    </v-row>
  </v-container>
</template>
<script>
import { mapState } from "vuex";
import moment from "moment";
import groupByKey from "~/helpers/groupByKey";
import PersonItem from "~/components/homes/PersonItem.vue";
export default {
  components: {
    PersonItem,
  },
  created() {
    this.id = this.$route.params.id;
    this.moment = moment;
    this.$axios
      .get(`api/v1/homes/${this.id}`)
      .then((res) => {
        this.home = res.data;
        this.documents = this.home.documents;
        console.log(this.home)
      })
      .catch((err) => {
        this.error = err;
      });
  },
  data() {
    return {
      to: false,
      headers: [
        { text: "Статус", value: "status" },
        { text: "Вид ресурса", value: "resource" },
        { text: "Причина", value: "reason" },
        { text: "План. дата отключения", value: "disable_dt" },
        { text: "План. дата включения", value: "enable_dt" },
        { text: "Факт. дата включения", value: "fact_dt" },
        { text: "Квартира", value: "aparment" },
      ],
      id: -1,
      home: false,
      
      documents: [
        {
          type: "Годовые отчёты",
          title: "АЛЕКСАНДРА НЕВСКОГО УЛИЦА д.2а корп 1_2021_ООО__АМЕТИСТ_.pdf",
          src: "/aaaa.pdf",
        },
        {
          type: "Годовые отчёты",
          title: "АЛЕКСАНДРА НЕВСКОГО УЛИЦА д.2а корп 1_2022_ООО__АМЕТИСТ_.pdf",
          src: "/aaaa.pdf",
        },
        {
          type: "Протоколы ОСС",
          title: "Протокол.pdf",
          src: "/aaaa.pdf",
        },
      ],
      personal: [
        {
          first_name: "Антон",
          last_name: "Круглов",
          middle_name: "Алексеевич",
          role: "Электрик",
        },
      ],
    };
  },
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
    groupedDocuments() {
      return groupByKey("type", this.documents);
    },
    appartments() {
      let count = 0;
      if (this.home?.levels) {
        for (let level of this.home.levels) {
          count += level.apartments.length;
        }
      }
      return count;
    },
    disablings() {
      let res = [];
      if (this.home) {
        for (let level of [...this.home.levels]) {
          for (let apartment of level.apartments) {
            res.push(...apartment.disablings)
          }
        }
      }
      return res
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
.news-paragraph-image img {
  max-width: 100% !important;
}
a {
  text-decoration: none;
}
a:hover {
  text-decoration: underline;
}
</style>
