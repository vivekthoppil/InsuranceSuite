<template>
  <v-container>
    <v-layout row>
      <v-flex md6>
        <v-subheader class="blue lighten-4" light><h1>Sign Up</h1></v-subheader>
        <v-spacer />
        <v-form ref="form" v-model="valid" lazy-validation>
          <v-text-field
            v-model="email"
            :rules="emailRules"
            label="E-mail"
            required
          ></v-text-field>
          <v-text-field
            v-model="username"
            :rules="userNameRules"
            label="Username"
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
            @click="onSignUp"
            color="success"
            class="mr-4"
          >
            Register
          </v-btn>
        </v-form>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { createNamespacedHelpers } from 'vuex'
import { REGISTER } from '@/store/actions.type'
const { mapActions } = createNamespacedHelpers('auth')

export default {
  middleware: 'anonymous',
  data: () => ({
    valid: true,
    passwordRules: [
      (v) => !!v || 'Password is required',
      (v) => v.length >= 8 || 'Min password length is 8'
    ],
    emailRules: [
      (v) => !!v || 'E-mail is required',
      (v) => /.+@.+\..+/.test(v) || 'E-mail must be valid'
    ],
    userNameRules: [(v) => !!v || 'Username is required'],

    password: '',
    email: '',
    username: ''
  }),
  methods: {
    ...mapActions([REGISTER]),
    onSignUp() {
      if (!this.$refs.form.validate()) {
        return
      }
      this.register({
        email: this.email,
        password: this.password,
        username: this.username
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
