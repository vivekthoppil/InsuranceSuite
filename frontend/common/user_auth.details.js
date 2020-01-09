const ID_TOKEN_KEY = 'id_token'
const USER_NAME_KEY = 'suite_user'

export const getToken = () => {
  return window.localStorage.getItem(ID_TOKEN_KEY)
}

export const getUsername = () => {
  return window.localStorage.getItem(USER_NAME_KEY)
}

export const saveToken = (token) => {
  window.localStorage.setItem(ID_TOKEN_KEY, token)
}

export const saveUsername = (username) => {
  window.localStorage.setItem(USER_NAME_KEY, username)
}

export const destroyToken = () => {
  window.localStorage.removeItem(ID_TOKEN_KEY)
}

export const destroyUsername = () => {
  window.localStorage.removeItem(USER_NAME_KEY)
}

export default {
  getToken,
  getUsername,
  saveToken,
  saveUsername,
  destroyToken,
  destroyUsername
}
