export default (ctx, inject) => {
  inject('formatApiErrorMessages', (apiErrors) => {
    const errors = []
    if ('detail' in apiErrors) {
      errors.push(apiErrors.detail)
    }
    return errors
  })
}
