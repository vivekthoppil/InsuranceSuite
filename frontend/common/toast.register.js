const toastOptions = {
  position: 'bottom-center',
  keepOnHover: true,
  singleton: true
}

const errorToastOptions = {
  ...toastOptions,
  type: 'error',
  icon: 'error_outline'
}

export const createToastRegistry = ($toast) => {
  $toast.register(
    'app_error',
    (payload) => {
      if (!payload.message) {
        return 'Oops.. Something Went Wrong..'
      }
      return payload.message
    },
    errorToastOptions
  )
}
