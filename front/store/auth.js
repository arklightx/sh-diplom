import { getItem, setItem } from "@/helpers/persistanceStorage";
import Cookies from "js-cookie";
import vue from "vue";
export const state = () => ({
    currentUser: {},
    errors: null,
    accessToken: null,
    isLoggedIn: true,
    refreshToken: null,
    base: "http://127.0.0.1:8000"
});

export const actions = {
    login({ commit }, data) {
        return new Promise((resolve, reject) => {
            this.$axios
                .post("/api/auth/authorize/", data, { withCredentials: true })
                .then((res) => {
                    let data = res.data;
                    let user = data.user;
                    console.log(data)
                    Cookies.set("user", JSON.stringify(user), { expires: 7 });
                    commit("setAccessToken", data.access);
                    commit("setUser", user);
                    resolve(user);
                })
                .catch((err) => {
                    reject("Проверьте данные");
                });
        });
    },
    tokenPair({ commit }, refresh) {
        return new Promise((resolve, reject) => {
            this.$axios
                .post(
                    "api/auth/token_pair/",
                    null,
                    { withCredentials: true }
                )
                .then((res) => {
                    let result = res.data;
                    commit("setAccessToken", result.access);
                    let user = this.$cookiz.get("user");
                    commit("setUser", user);
                    resolve(result.user);
                })
                .catch((err) => {
                    this.$cookiz.set("user", null);
                    reject("Время сессии истекло");
                });
        });
    },
    logOut({ commit, state }, refresh) {
        return new Promise((resolve, reject) => {
            this.$axios
                .delete("api/auth/logout/", {
                    withCredentials: true,
                    headers: {
                        Authorization: `Bearer ${state.accessToken}`,
                    },
                })
                .then((res) => {
                    commit("setAccessToken", null);
                    commit("setUser", null);
                    this.$cookiz.remove("user");
                    this.$router.push("/");
                    resolve("shik");
                    return;
                })
                .catch((err) => {
                    this.$router.push("/");
                    reject("Ошибка выхода");
                });
        });
    },
};

export const mutations = {
    setAccessToken(state, token) {
        console.log(token)
        state.accessToken = token;
    },
    setRefreshToken(state, token) {
        state.refreshToken = token;
    },
    setUser(state, user) {
        vue.set(state, ["currentUser"], { ...user });
    },
    setIsLoggedIn(state, status){
        state.isLoggedIn = status
    }
};

export const getters = {
    getAccessToken: (s) => s.accessToken,
    getRefreshToken: (s) => s.refreshToken,
    getUser: (s) => s.currentUser,
    getBase: (s) => s.base,
};
