const PUBLIC_URLS = ['/signin', '/signin/', '/signup', '/signup/']

export default function(context) {
  if (PUBLIC_URLS.includes(context.route.path)) {
    return
  }
  if (!context.store.getters['auth/isAuthenticated']) {
    return context.redirect('/signin')
  }
}
