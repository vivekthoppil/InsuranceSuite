import {
  authApiRepository,
  createApiRepository,
  riskTypeRepository
} from '@/common/api.service'
export default (ctx, inject) => {
  const repositoryWithAxios = createApiRepository(ctx.$axios)
  inject('apiService', repositoryWithAxios)

  const authServiceInitialized = authApiRepository(repositoryWithAxios)
  inject('authService', authServiceInitialized)

  const riskTypeServiceInitialized = riskTypeRepository(repositoryWithAxios)
  inject('riskTypeService', riskTypeServiceInitialized)
}
