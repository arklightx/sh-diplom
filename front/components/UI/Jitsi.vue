<template>
  <v-card>
    <v-card-text>
      <div id="meet"></div>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  mounted() {
    const domain = "meet.jit.si";
    const options = {
      roomName: "jitsy-for-users-of-sergey-diplom"+this.homeId,
      width: "100%",
      height: 700,
      parentNode: document.querySelector("#meet"),
    };
    const api = new JitsiMeetExternalAPI(domain, options);
  },
  data() {
    return {};
  },
  props:{
    homeId: 0
  }
};
</script>
