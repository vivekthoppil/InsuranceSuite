import { SET_AUTH, PURGE_AUTH, SET_ERROR } from './mutations.type'
import { LOGIN, LOGOUT, REGISTER } from './actions.type'
import UserAuthService from '~/common/user_auth.details'

export const state = () => ({
  user: UserAuthService.getUsername(),
  isAuthenticated: !!UserAuthService.getToken()
})

export const getters = {
  currentUser(state) {
    return state.user
  },
  isAuthenticated(state) {
    return state.isAuthenticated
  }
}

export const actions = {
  [LOGIN](context, credentials) {
    const serviceCall = (resolve, reject) => {
      this.$authService
        .login(credentials)
        .then(({ data }) => {
          context.commit(SET_AUTH, data.user)
          resolve(data)
        })
        .catch(({ response }) => {
          reject(response)
        })
    }
    return new Promise(serviceCall)
  },
  [LOGOUT](context) {
    context.commit(PURGE_AUTH)
  },
  [REGISTER](context, credentials) {
    const serviceCall = (resolve, reject) => {
      this.$authService
        .register(credentials)
        .then(({ data }) => {
          context.commit(SET_AUTH, data.user)
          resolve(data)
        })
        .catch(({ response }) => {
          reject(response)
        })
    }
    return new Promise(serviceCall)
  }
}

export const mutations = {
  [SET_ERROR](state, errorObj) {
    const errors = this.$formatApiErrorMessages(errorObj)
    state.errors = errors
  },
  [SET_AUTH](state, user) {
    state.isAuthenticated = true
    state.user = user.username
    UserAuthService.saveUsername(user.username)
    UserAuthService.saveToken(user.token)
  },
  [PURGE_AUTH](state) {
    state.isAuthenticated = false
    state.user = ''
    UserAuthService.destroyUsername()
    UserAuthService.destroyToken()
  }
}
