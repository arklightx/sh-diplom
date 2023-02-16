<template>
    <v-card>
        <v-card-text>
            <h2 class="text-h6 mb-2">Добавить комментарий</h2>
            <div v-if="to">
                Ответить: 
                <v-chip class="my-2">
                    @{{to.author.username}}
                </v-chip>
                <v-btn
                    @click="reset"
                    x-small
                    fab
                    icon
                >
                    <v-icon>
                        mdi-close
                    </v-icon>
                </v-btn>
            </div>
            
            <v-textarea
                @keyup.enter="add"
                outlined
                name="input-7-4"
                class="mb-0"
                label="Что вы об этом думаете?"
                v-model="comment"
                @blur="$v.comment.$touch()"
                @input="$v.comment.$touch()"
                :error-messages="commentErrors"
            ></v-textarea>
            <v-card-actions class="ma-0 pa-0">
                <v-spacer></v-spacer>
                <v-btn
                    @click="add"
                    color="primary"
                >
                    Отправить
                </v-btn>
            </v-card-actions>
        </v-card-text>
    </v-card>
</template>


<script>
import { validationMixin } from 'vuelidate'
import { required, email, maxLength, minLength, minValue, maxValue, numeric, url } from 'vuelidate/lib/validators'
export default {
    mixins: [validationMixin],
    props: {
        to: {
            default: false
        }
    },
    validations: {
        comment: {required, minLength: minLength(3)}, 
    },
    data(){
        return({
            comment: ''
        })
    },
    methods:{
        add(){
            this.$v.$touch()
            if(this.$v.$anyError) return
            this.$emit('addComment', this.comment)
            this.comment=''
            this.$v.$reset()
        },
        reset(){
            this.$emit('reset')
        }
    },
    computed: {
        commentErrors () {
            const errors = []
            if (!this.$v.comment.$dirty) return errors
            !this.$v.comment.required && errors.push('Введите комментарий')
            !this.$v.comment.minLength && errors.push('Введите комментарий')

            return errors
        },
    }
}
</script>
