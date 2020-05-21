<template>
    <section class="container">
        <ul>
          <li><router-link to="/">Home</router-link></li>
          <li><router-link to="logchart">Realtime</router-link></li>
          <li><router-link to="logchart2">Log</router-link></li>
        </ul>
        <h1>Demo examples</h1>
        <div class="columns">
            <div class="column">
                <h3>Line Chart</h3>
                <myinput></myinput>
            </div>
            <div class="column">
                <h3>Line Chart</h3>
                <myinput></myinput>
            </div>
        </div>
        <div class="columns">
            <div class="column">
                <h3>Line Chart</h3>
                <myinput></myinput>
            </div>
            <div class="column">
                <h3>Line Chart</h3>
                <myinput></myinput>
            </div>
        </div>
    </section>
</template>

<script>
import Myinput from './Myinput'
// import { getChartDataFormat, getChartOptionFormat, chartDataArray } from '../api/api'

export default {
  name: 'VueChartJS',
  components: {
    Myinput
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
