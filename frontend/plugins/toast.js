import { createToastRegistry } from '@/common/toast.register'

export default (ctx) => {
  createToastRegistry(ctx.app.$toast)
}
