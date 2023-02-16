<template>
    <div class="d-flex align-center justify-center">
        <LoginForm @submit="submit"/>
    </div>
</template>

<script>
import LoginForm from '~/components/UI/LoginForm';
export default{
    components: {
        LoginForm
    },
    data(){
        return {

        }
    },
    methods: {
        submit(data){
            this.$store.dispatch('auth/login', data).then(res=>{
                if(res){
                    console.log(res)
                    this.errors = null
                    this.$router.push('/')
                }
            }).catch(err=>{
                this.errors = err
                console.log(this.errors)
            })
        }
    }
}
</script>