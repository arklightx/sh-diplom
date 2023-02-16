<template>
  <div>
    <v-list>
      <div v-for="item in menu">
        <v-list-item
          v-if="!item.submenu"
          :key="item.to"
          nuxt
          active-class="primary--text"
          :to="item.to"
        >
          <v-list-item-icon>
            <v-icon>{{ item.ico }}</v-icon>
          </v-list-item-icon>
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item>
        <v-list-group v-else :prepend-icon="item.ico">
          <template v-slot:activator>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </template>
          <v-list-item
            :href="subitem.href ? subitem.href : ''"
            :nuxt="!!subitem.href"
            v-for="subitem in item.submenu"
            :key="subitem.to"
            nuxt
            active-class="activeLink"
            :to="subitem.to"
            class="ml-6"
          >
            <v-list-item-icon>
              <v-icon small>{{ subitem.ico }}</v-icon>
            </v-list-item-icon>
            <v-list-item-title>{{ subitem.title }}</v-list-item-title>
          </v-list-item>
        </v-list-group>
      </div>
    </v-list>
  </div>
</template>

<script>
export default {
  props: {
    value: {
      type: Boolean,
      default: false,
    },
    menu: [],
  },
  methods: {
    close() {
      this.$emit("close");
    },
  },
};
</script>
