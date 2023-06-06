<template>
    <v-container>
        <v-row no-gutters>
            <v-col class="col col-1 d-none d-md-block"></v-col>
            <v-col class="col col-12 col-md-10">
                <v-card class="mt-2">
                    <v-card-text>
                        <v-card class="mt-2">
                            <v-card-title> Обращения </v-card-title>
                            <v-card-text>
                                <request-item class="mb-6" v-for="(item, key) in requests" :key="key"
                                    :item="item"></request-item>
                                <div class="d-flex justify-center flex-column">
                                    <request-form @submit="submitRequest" class="mt-4"
                                        v-if="suggestRequestStatus"></request-form>
                                    <v-btn @click="suggestRequestStatus = !suggestRequestStatus"
                                        class="align-self-center mt-2">
                                        <template v-if="!suggestRequestStatus">
                                            Создать <v-icon right dark> mdi-plus </v-icon>
                                        </template>
                                        <template v-else>
                                            Скрыть <v-icon right dark> mdi-minus </v-icon>
                                        </template>
                                    </v-btn>
                                </div>
                            </v-card-text>
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
import RequestForm from "~/components/LK/RequestForm.vue";
import RequestItem from "~/components/LK/RequestItem.vue";
export default {
    components: {
        RequestItem,
        RequestForm,
    },
    async created() {
        if (!this.user) {
            this.$router.push("/login");
        }
        setTimeout(() => {
            this.$axios
                .get(`api/v1/requests/${this.home.id}`, {
                    withCredentials: true,
                    headers: { Authorization: `Bearer ${this.token}` },
                })
                .then((res) => {
                    this.requests = res.data;
                });

        }, 200);
    },
    data() {
        return {
            requiredRules: [(v) => !!v || "Поле обязательно"],
            suggestStatus: false,
            suggestRequestStatus: false,
            requests: [],
        };
    },
    methods: {
        submitRequest(data) {
            this.$axios
                .post(
                    `api/v1/requests/`,
                    {
                        user: this.user.id,
                        home: this.home.id,
                        theme: data.theme,
                        text: data.text,
                    },
                    {
                        withCredentials: true,
                        headers: { Authorization: `Bearer ${this.token}` },
                    }
                )
                .then((res) => {
                    Swal.fire({
                        position: "center",
                        icon: "success",
                        title: "Запрос отправлен!",
                        showConfirmButton: false,
                        timer: 3000,
                    });
                });
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
  