<template>
    <section class="container">
        <ul>
            <li><router-link to="/">Home</router-link></li>
            <li><router-link to="chartjs">vue-chartjs</router-link></li>
            <li><router-link to="logchart">log-chartjs</router-link></li>
        </ul>
        <h1>Demo examples</h1>
        <div class="columns">
            <div class="column">
                <h3>Line Chart</h3>
                <reactive
                  :create="'2020-05-17'"
                  :device="'BME280'"
                  :place="'部屋001'"
                  :physic="'温度'"/>
            </div>
            <div class="column">
                <h3>Bar Chart</h3>
                <reactive
                  :create="'2020-05-18'"
                  :device="'BME280'"
                  :place="'部屋001'"
                  :physic="'温度'"/>
            </div>
        </div>
        <div class="columns">
            <div class="column">
                <h3>Bubble Chart</h3>
                <reactive
                  :create="'2020-05-19'"
                  :device="'BME280'"
                  :place="'部屋001'"
                  :physic="'温度'"/>
            </div>
            <div class="column">
                <h3>Reactivity - Live update upon change in datasets</h3>
                <realtime
                  :device="'MAX31855'"
                  :place="'部屋003'"
                  :physic="'温度'"/>
            </div>
        </div>
    </section>
</template>

<script>
import Reactive from './Reactive'
import Realtime from './Realtime'
// import { getChartDataFormat, getChartOptionFormat, chartDataArray } from '../api/api'

export default {
  name: 'VueChartJS',
  components: {
    Reactive,
    Realtime
  },
  data () {
    return {
      // dataContents: null,
      // chartData: null
      // options: getChartOptionFormat(),
      // loaded: false
    }
  },
  created () {
  },
  methods: {
  }
}
</script>

<style scoped>
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
