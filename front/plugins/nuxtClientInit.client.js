export default async context => {
    context.store.dispatch('auth/tokenPair')
        .finally(()=>context.app.store.commit("auth/setIsLoggedIn", true))
    if (context.$cookiz.get('user')){
        setInterval(()=>{
            context.store.dispatch('auth/tokenPair')
        }, 100000)
    }
}