<template>
  <v-snackbar v-model="show" :color="color" :timeout="timeout">
    {{ message }}
    <v-btn @click="show = false" text>Close</v-btn>
  </v-snackbar>
</template>

<script>
export default {
  data() {
    return {
      show: false,
      message: '',
      color: '',
      timeout: 3000
    }
  },

  created() {
    this.$store.subscribe((mutation, state) => {
      if (mutation.type === 'snackbar/showMessage') {
        this.message = state.snackbar.content
        this.color = state.snackbar.color
        this.timeout = state.snackbar.timeout
        this.show = true
      }
    })
  }
}
</script>
