<template>
  <v-container>
    <v-layout row>
      <v-flex md6>
        <label>
          <slot />
        </label>
        <v-text-field
          v-if="controlType === 'Text'"
          v-bind="$attrs"
          :value="value"
          @input="$emit('input', $event)"
          required
        ></v-text-field>
        <v-text-field
          v-if="controlType === 'Number'"
          v-bind="$attrs"
          :value="value"
          @input="$emit('input', $event)"
        ></v-text-field>
        <v-select
          v-if="controlType === 'Enum'"
          v-bind="$attrs"
          :value="value"
          @change="$emit('change', $event)"
        ></v-select>
        <v-menu
          ref="menu1"
          v-if="controlType === 'Date'"
          v-model="menu1"
          :close-on-content-click="false"
          transition="scale-transition"
          offset-y
          full-width
          max-width="290px"
          min-width="290px"
        >
          <template v-slot:activator="{ on }">
            <v-text-field
              v-bind="$attrs"
              v-model="dateFormatted"
              @blur="date = parseDate(dateFormatted)"
              v-on="on"
              persistent-hint
              prepend-icon="event"
            ></v-text-field>
          </template>
          <v-date-picker
            v-model="date"
            @input="menu1 = false"
            no-title
          ></v-date-picker>
        </v-menu>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  name: 'AppInputControl',
  inheritAttrs: false,
  props: {
    controlType: {
      type: String,
      default: 'input'
    },
    value: {
      type: String,
      default: ''
    }
  },
  data() {
    return {
      date: new Date().toISOString().substr(0, 10),
      dateFormatted: this.formatDate(new Date().toISOString().substr(0, 10)),
      menu1: false
    }
  },
  computed: {
    computedDateFormatted() {
      return this.formatDate(this.date)
    }
  },

  watch: {
    date(val) {
      this.dateFormatted = this.formatDate(this.date)
    }
  },

  methods: {
    formatDate(date) {
      if (!date) return null

      const [year, month, day] = date.split('-')
      return `${month}/${day}/${year}`
    },
    parseDate(date) {
      if (!date) return null

      const [month, day, year] = date.split('/')
      return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
    }
  }
}
</script>
