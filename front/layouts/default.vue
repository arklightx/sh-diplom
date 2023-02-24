<template>
	<v-app>
		<Header class="z-index-12" />
		<v-main>
			<v-container>
				<Nuxt v-if="isLoggedIn" class="z-index-1" />
			</v-container>
		</v-main>
		<Footer class="z-index-10" />
	</v-app>
</template>

<script>
import Header from '@/components/UI/Header.vue'
import {mapState} from "vuex"
export default {
	name: 'DefaultLayout',
	components: {
		Header,
	},
	data() {
		return ({
			counter: 0,
			user: false,
		})
	},
	computed:{
		...mapState("auth", ["isLoggedIn", "accessToken"])
	}
}
</script>

<style>
.z-index-12 {
	z-index: 12;
}
</style>

