<template>
  <v-container fluid>
    <v-layout row>
      <v-flex md6>
        <v-subheader class="blue lighten-4" light
          ><h1>Risk Details</h1></v-subheader
        >
        <v-spacer />
        <v-form ref="form" v-model="valid" lazy-validation>
          <AppControlInput
            v-for="(riskAttribute, i) in risk.riskAttributes"
            :key="i"
            v-model="riskAttribute.rawValue"
            :control-type="riskAttribute.attributeTypeName"
            :label="riskAttribute.label"
            :items="riskAttribute.options"
          ></AppControlInput>
          <v-btn
            :disabled="!valid"
            @click="onSave"
            color="success"
            class="mr-4"
          >
            Save
          </v-btn>
        </v-form>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
import AppControlInput from '@/components/UI/AppControlInput'

export default {
  components: {
    AppControlInput
  },
  asyncData(context) {
    return context.app.$riskTypeService
      .retrieveRiskType(context.route.params.id)
      .then((res) => {
        const risk = {
          riskTypeId: res.data.risk_type.id,
          riskAttributes: []
        }
        res.data.risk_type.attributes.forEach(function(attribute, index) {
          const riskAttribute = {
            attributeTypeId: attribute.attribute_type.id,
            attributeTypeName: attribute.attribute_type.name,
            label: attribute.label,
            required: attribute.required,
            options: attribute.options ? attribute.options.split(',') : null,
            rawValue: null
          }
          risk.riskAttributes.push(riskAttribute)
        })
        return {
          valid: true,
          risk
        }
      })
  },
  methods: {
    onSave() {
      this.$notifier.showMessage({
        content: JSON.stringify('Work in progress !!!'),
        color: 'error'
      })
    }
  }
}
</script>
