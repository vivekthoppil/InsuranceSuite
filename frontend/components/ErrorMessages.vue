<template>
  <v-banner single-line>
    One line message text string with two actions on tablet / Desktop

    <template v-slot:actions>
      <v-btn text color="deep-purple accent-4">
        Action
      </v-btn>
    </template>
  </v-banner>
</template>

<script>
export default {
  name: 'ErrorMessages',
  props: {
    error: {
      type: Object,
      default() {
        return {}
      }
    }
  },
  computed: {
    errFormatted() {
      return Object.keys(this.error).reduce((result, errorKey) => {
        if (!Array.isArray(this.error[errorKey])) {
          return result.concat(this.error[errorKey])
        }
        // const messages = this.error[errorKey].map(
        //   (msgElm) => `${errorKey} ${msgElm}`
        // )
        // return result.concat(messages)
      }, [])
    }
  }
}
</script>

<style scoped>
.error-messages {
  color: #b85c5c !important;
  font-weight: 700;
}
</style>
