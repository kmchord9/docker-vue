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
            </div>
            <div class="column">
                <h3>Bar Chart</h3>
            </div>
        </div>
        <div class="columns">
            <div class="column">
                <h3>Bubble Chart</h3>
                <reactive
                  v-if="loaded"
                  :chart-data="chartData"
                  :options="options"/>

            </div>
            <div class="column">
                <h3>Reactivity - Live update upon change in datasets</h3>
            </div>
        </div>
    </section>
</template>

<script>
import Reactive from './Reactive'
import { getChartDataFormat, getChartOptionFormat, chartDataArray } from '../api/api'

export default {
  name: 'VueChartJS',
  components: {
    Reactive
  },
  data () {
    return {
      dataContents: null,
      chartData: null,
      options: getChartOptionFormat(),
      loaded: false
    }
  },
  created () {
  },
  methods: {
  },
  mounted () {
    this.loaded = false
    try {
      // chartDataArray(this.physics, this.device, this.place, this.createat, this.creategt)
      chartDataArray('温度', 'BME280', '部屋001', '2020-05-19')
        .then((res) => {
          this.chartData = getChartDataFormat(res[0], res[1])
        })
      this.loaded = true
    } catch (e) {
      console.error(e)
    }
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
