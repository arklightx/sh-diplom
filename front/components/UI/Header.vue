<template>
  <div>
    <v-navigation-drawer v-model="drawer" absolute left d-md-none width="300px" temporary>
      <List :menu="menu" />
    </v-navigation-drawer>
    <v-app-bar>
      <v-app-bar-nav-icon @click.stop="open" class="ml-2"></v-app-bar-nav-icon>
      <v-toolbar-title class="toolbar__title">
        <v-col class="d-flex curp justify-space-between align-center">
          <v-img @click="$router.push('/')" contain width="100px"> </v-img>
        </v-col>
      </v-toolbar-title>
      <!-- <Search :key="index" @search="rerender"/> -->
      <v-spacer />
      <!-- <DesktopMenu :menu="menu" class="d-none d-md-flex"/>  -->
      <v-spacer />
      <v-menu open-on-click left offset-y dense>
        <template v-slot:activator="{ on, attrs }">
          <v-btn v-bind="attrs" v-on="on" class="my-6 mr-lg-2 mr-0" icon rounded>
            <v-avatar color="primary">
              <v-img v-if="user.avatar" :src="base + user.avatar" alt="" />
              <span v-else-if="user.username" class="white--text text-h5">{{
                user.username.slice(0, 2)
              }}</span>
              <span v-else class="white--text text-h5">ЛК</span>
            </v-avatar>
          </v-btn>
        </template>
        <v-list>
          <v-list-item-group>
            <div v-if="user.username" class="text-h6 pa-4">{{ user.username }}</div>
            <template v-if="username">
              <v-list-item exact to="/lk" nuxt class="primary--text">
                <v-list-item-title color="primary"> Личный кабинет</v-list-item-title>
              </v-list-item>
              <v-list-item exact to="/lk/events" nuxt class="primary--text">
                <v-list-item-title color="primary"> Календарь событий</v-list-item-title>
              </v-list-item>
              <v-list-item exact to="/lk/jitsy" nuxt class="primary--text">
                <v-list-item-title color="primary"> Видеосвязь</v-list-item-title>
              </v-list-item>
              <v-list-item exact to="/lk/votes" nuxt class="primary--text">
                <v-list-item-title color="primary"> Голосования</v-list-item-title>
              </v-list-item>
            </template>


            <v-list-item to="/login" nuxt class="primary--text" v-if="!username">
              <v-list-item-title>Войти в аккаунт</v-list-item-title>
            </v-list-item>
            <v-list-item @click="logOut" color="red" v-if="username">
              <v-list-item-title class="red--text">Выйти</v-list-item-title>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-menu>
    </v-app-bar>
  </div>
</template>

<script>
import List from "@/components/UI/List";
// import DesktopMenu from './DesktopMenu.vue';
import { mapState } from "vuex";
// import Search from './Search.vue';
import { globalMenu } from "~/helpers/globalMenu";
export default {
  created() {
    this.menu = globalMenu;
  },
  components: {
    List, //МОбильная версия меню
    // DesktopMenu
  },
  data() {
    return {
      drawer: false,
      index: 0,
      menu: [],
    };
  },
  methods: {
    rerender() {
      this.index++;
    },

    logOut() {
      this.$store.dispatch("auth/logOut").then((res) => {
        this.$router.push("/");
      });
    },
    open() {
      this.drawer = true;
    },
    close() {
      this.drawer = false;
    },
  },
  computed: {
    username() {
      let user = this.$store.getters["auth/getUser"];
      if (user?.username) return user.username;

      // return this.$store.getters['auth/getUser'].username
    },
    user: {
      get() {
        return this.$store.getters["auth/getUser"];
      },
      set(newValue) {
        this.$store.commit("auth/setUser", newValue);
      },
    },
    ...mapState("auth", ["base"]),
  },
  name: "Header",
};
</script>

<style lang="scss">
.menu__item a {
  font-size: 1em;
  color: #506690 !important;
  text-decoration: none;

  &:hover {
    color: #335eea !important;
  }
}

.navigation {
  display: flex;
  justify-content: center;
  align-items: center;
}

.toolbar__title {
  padding-left: 0 !important;
}
</style>
