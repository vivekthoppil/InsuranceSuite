export default ({ app, store }, inject) => {
  inject('notifier', {
    showMessage({ content = '', color = '', timeout = 3000 }) {
      store.commit('snackbar/showMessage', { content, color, timeout })
    }
  })
}
