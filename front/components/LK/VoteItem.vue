<template>
  <v-card color="blue-grey darken-4">
    <v-card-title class="text-h6 mb-0 pb-0 primary--text">
      {{ item.theme }}
    </v-card-title>
    <v-card-text>
      <v-radio-group :disabled="!item.isActive" v-model="item.userVariant" column>
        <v-progress-linear
          :key="key"
          rounded
          :class="{'mb-3': (key != item.variants.length-1)}"
          v-for="(variant, key) in item.variants"
          :value="(variant.votes / totalVotes) * 100"
          :color="item.userVariant === variant.label ? 'blue-grey' : 'blue-grey darken-3'"
          height="50"
        >
          <template v-slot:default="{ value }">
            <div class="d-flex mt-2 pa-3 radio align-center justify-space-between">
              <v-radio :label="variant.label" :value="variant.label"></v-radio>
              <strong> {{ Math.ceil(value) }}% </strong>
            </div>
          </template>
        </v-progress-linear>
      </v-radio-group>
    </v-card-text>
    <v-card-actions v-if="item.isActive"> 
      <v-spacer></v-spacer>
      <v-btn @click="onVoteSend" color="primary">Проголосовать</v-btn></v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "VoteItem",
  data() {
    return {
      select: "",
    };
  },
  props: {
    item: {},
  },
  methods: {
    onVoteSend(){
      this.$emit("onVoteSend", this.item)
    }
  },
  computed: {
    totalVotes() {
      return this.item.variants.reduce((a, b) => {
        return a + b.votes;
      }, 0);
    },
  },
};
</script>

<style lang="scss" scoped>
.radio {
  display: flex;
  width: 100%;
  align-items: center;
}
</style>
