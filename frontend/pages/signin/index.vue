<template>
  <v-container>
    <v-layout row>
      <v-flex md6>
        <v-subheader class="blue lighten-4" light><h1>Sign In</h1></v-subheader>
        <v-spacer />
        <v-form ref="form" v-model="valid" lazy-validation>
          <v-text-field
            v-model="email"
            :rules="emailRules"
            label="E-mail"
            required
          ></v-text-field>
          <v-text-field
            v-model="password"
            :rules="passwordRules"
            :type="'password'"
            label="Password"
            required
          ></v-text-field>
          <v-btn
            :disabled="!valid"
            @click="onSignIn"
            color="success"
            class="mr-4"
          >
            Sign In
          </v-btn>

          <v-btn @click="$router.push('/signup')" color="error" class="mr-4">
            Sign Up
          </v-btn>
        </v-form>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { createNamespacedHelpers } from 'vuex'
import { LOGIN } from '@/store/actions.type'
const { mapActions } = createNamespacedHelpers('auth')

export default {
  middleware: 'anonymous',
  data: () => ({
    valid: true,
    passwordRules: [(v) => !!v || 'Password is required'],
    emailRules: [
      (v) => !!v || 'E-mail is required',
      (v) => /.+@.+\..+/.test(v) || 'E-mail must be valid'
    ],

    password: null,
    email: null
  }),
  methods: {
    ...mapActions([LOGIN]),
    onSignIn() {
      if (!this.$refs.form.validate()) {
        return
      }
      this.login({
        email: this.email,
        password: this.password
      })
        .then(() => this.$router.push('/'))
        .catch((response) => {
          this.$notifier.showMessage({
            content: response.data.errors.detail,
            color: 'error'
          })
        })
    }
  }
}
</script>
