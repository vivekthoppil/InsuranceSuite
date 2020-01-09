import { getToken } from '~/common/user_auth.details'

const PUBLIC_URLS = ['/authentication/users/login/', '/authentication/users/']

export default function({ $axios, app, store }) {
  $axios.onRequest((config) => {
    if (PUBLIC_URLS.includes(config.url)) {
      return
    }
    if (getToken()) {
      config.headers.common.Authorization = 'Bearer ' + getToken()
    }
  })
  $axios.onError((error) => {
    const code = parseInt(error.response && error.response.status)
    if (code === 401) {
      store.dispatch('auth/logout')
    }
    return Promise.reject(error)
  })
}
