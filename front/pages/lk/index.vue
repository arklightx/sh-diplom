<template>
  <v-container>
    <v-row no-gutters>
      <v-col class="col col-1 d-none d-md-block"></v-col>
      <v-col class="col col-12 col-md-10">
        <v-img class="d-flex text-center main_img align-center justify-center"
          gradient="to top right, rgba(0,0,0,.1), rgba(25,32,72,.8)" max-height="400px"
          :src="require('@/assets/images/lk_main.jpg')">
          <h1 class="text-h4 text-md-h2 mb-2 font-weight-medium">Личный кабинет</h1>
        </v-img>
        <v-card>
          <v-card-title>Личная информация</v-card-title>
          <v-card-text>
            <v-card color="blue-grey darken-4">
              <v-form @submit.prevent="submitInfo" ref="infoForm" v-model="infoValid" class="pa-3">
                <v-text-field v-model="user.last_name" filled required outlined :rules="requiredRules"
                  label="Фамилия"></v-text-field>
                <v-text-field v-model="user.first_name" filled outlined required :rules="requiredRules"
                  label="Имя"></v-text-field>
                <v-text-field v-model="user.patronymic" filled outlined required :rules="requiredRules"
                  label="Отчество"></v-text-field>
                <v-text-field v-model="user.phone" filled outlined required :rules="requiredRules"
                  label="Телефон"></v-text-field>
                <v-text-field v-model="user.email" filled required :rules="emailRules" outlined
                  label="Почта"></v-text-field>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn @click="submitInfo" color="primary">Сохранить</v-btn>
                </v-card-actions>
              </v-form>
            </v-card>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col class="d-none d-md-block"> </v-col>
    </v-row>
  </v-container>
</template>
<script>
import Swal from "sweetalert2";
export default {
  async created() {
    if (!this.user) {
      this.$router.push("/login");
    }
  },
  data() {
    return {
      infoValid: false,
      infoValid: false,
      emailRules: [
        (v) => !!v || "Почта обязательно",
        (v) => /.+@.+\..+/.test(v) || "Неверный формат почты",
      ],
      requiredRules: [(v) => !!v || "Поле обязательно"],
    };
  },
  methods: {
    submitInfo() {
      this.$refs.infoForm.validate();
      if (this.infoValid) {
        this.$axios
          .patch(
            `api/v1/users/change/private_data/`,
            this.user,
            {
              withCredentials: true,
              headers: { Authorization: `Bearer ${this.token}` },
            }
          )
          .then((res) => {
            Swal.fire({
              position: "center",
              icon: "success",
              title: "Информация обновлена",
              showConfirmButton: false,
              timer: 3000,
            });
          });
      }

    },
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
