<template>
    <div class="form_container">
        <v-card width="500">
            <v-card-title>Авторизация</v-card-title>
            <v-card-text>
                <form @keyup.enter="submit">
                    <v-text-field
                        v-model="username"
                        :error-messages="nameErrors"
                        label="Имя пользователя"
                        required
                        @input="$v.username.$touch()"
                        @blur="$v.username.$touch()"
                    ></v-text-field>
                    <v-text-field
                        type="password"
                        v-model="password"
                        :error-messages="passErrors"
                        label="Пароль"
                        required
                        @input="$v.password.$touch()"
                        @blur="$v.password.$touch()"
                    ></v-text-field>
                    <v-btn
                        class="mr-4 primary"
                        @click="submit"
                    >
                        Войти
                    </v-btn>
                    <v-btn @click="clear">
                        Очистить
                    </v-btn>
                    <v-alert
                      border="bottom"
                      color="pink darken-1"
                      dark
                      v-if="errors"
                      class="mt-4"
                    >
                      {{errors}}
                    </v-alert>
                </form>
            </v-card-text>
           
        </v-card>
    </div>
</template>


<script>
  import { validationMixin } from 'vuelidate'
  import { required, minLength } from 'vuelidate/lib/validators'

  export default {
    mixins: [validationMixin],

    validations: {
      username: { required},
      password: { required, minLength: minLength(4)}
    },

    data: () => ({
      username: '',
      password: '',
    }),
    props:{
      errors:{
        type: String,
        default: null
      }
    },
    computed: {
      
      nameErrors () {
        const errors = []
        if (!this.$v.username.$dirty) return errors
        !this.$v.username.required && errors.push('Введите имя пользователя')
        return errors
      },
      passErrors () {
        const errors = []
        if (!this.$v.password.$dirty) return errors
        !this.$v.password.minLength && errors.push('Неверная длина')
        !this.$v.password.required && errors.push('Введите пароль')
        return errors
      },
    },

    methods: {
      submit () {
        this.$v.$touch()
        if(this.$v.$anyError) return
        let user = {
            username: this.username,
            password: this.password
        }
        this.$emit('submit', user)
      },
      clear () {
        this.$v.$reset()
        this.username = ''
        this.password = ''
      },
    },
  }
</script>


<style>
    .form_container{
        display: flex;
        justify-content: center;
        align-items: center;
        height: 80vh;
    }
</style>

