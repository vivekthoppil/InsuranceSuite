<template>
  <v-container fluid>
    <v-layout row justify-center class="text-xs-center mb-4">
      <v-flex
        v-for="riskType in riskTypes"
        :key="riskType.name"
        xs12
        sm12
        md4
        class="mx-2"
      >
        <v-card>
          <v-card-title v-text="riskType.name"></v-card-title>
          <v-card-text v-text="riskType.description"></v-card-text>
          <v-card-actions>
            <v-btn
              @click="$router.push('/risktypes/' + riskType.id)"
              color="primary"
              >Create Risk</v-btn
            >
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
    <v-layout row class="text-xs-center">
      <v-flex>
        <v-pagination
          :length="pageLength"
          @input="next"
          v-model="page"
        ></v-pagination>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
export default {
  computed: {
    pageLength() {
      return Math.ceil(this.totalResults / this.pageSize)
    }
  },
  asyncData(context) {
    return context.app.$riskTypeService.listRiskTypes().then((res) => {
      return {
        page: 1,
        pageSize: 2,
        totalResults: res.data.count,
        riskTypes: res.data.risk_types
      }
    })
  },
  methods: {
    next(page) {
      return this.$riskTypeService.listRiskTypes(page).then((res) => {
        this.riskTypes = res.data.risk_types
      })
    }
  }
}
</script>
