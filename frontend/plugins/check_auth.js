export default (ctx, inject) => {
  if (!ctx.store.getters['auth/isAuthenticated']) {
    return
  }
  return new Promise((resolve, reject) => {
    ctx.app.$riskTypeService
      .listRiskTypes()
      .then(({ data }) => {
        resolve('success')
      })
      .catch((data) => {
        resolve('success')
      })
  })
}
