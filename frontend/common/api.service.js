export const createApiRepository = ($axios) => ({
  query(resource, params) {
    return $axios.get(resource, params).catch((error) => {
      throw new Error(`[Suite] ApiService ${error}`)
    })
  },

  get(resource, slug = '') {
    return $axios.get(`${resource}/${slug}`).catch((error) => {
      throw new Error(`[Suite] ApiService ${error}`)
    })
  },

  post(resource, params) {
    return $axios.post(`${resource}`, params)
  },

  update(resource, slug, params) {
    return $axios.put(`${resource}/${slug}`, params)
  },

  put(resource, params) {
    return $axios.put(`${resource}`, params)
  },

  delete(resource) {
    return $axios.delete(resource).catch((error) => {
      throw new Error(`[Suite] ApiService ${error}`)
    })
  }
})

export const authApiRepository = (genericApiService) => ({
  login({ email, password }) {
    return genericApiService.post('/authentication/users/login/', {
      user: { email, password }
    })
  },
  register({ email, password, username }) {
    return genericApiService.post('/authentication/users/', {
      user: { email, password, username }
    })
  }
})

export const riskTypeRepository = (genericApiService) => ({
  listRiskTypes(page) {
    page = page || 1
    return genericApiService.query('/suite/risk_types', {
      params: { page }
    })
  },
  retrieveRiskType(id) {
    return genericApiService.get('/suite/risk_types', id)
  }
})
