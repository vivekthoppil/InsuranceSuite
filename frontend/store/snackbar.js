export const state = () => ({
  content: '',
  color: '',
  timeout: ''
})

export const mutations = {
  showMessage(state, payload) {
    state.content = payload.content
    state.color = payload.color
    state.timeout = payload.timeout
  }
}
