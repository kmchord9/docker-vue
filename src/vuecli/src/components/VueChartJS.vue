<template>
    <section class="container">
        <ul>
            <li><router-link to="/">Home</router-link></li>
            <li><router-link to="chartjs">vue-chartjs</router-link></li>
        </ul>
        <h1>Demo examples</h1>
        <div class="columns">
            <div class="column">
                <h3>Line Chart</h3>
                <line-chart></line-chart>
            </div>
            <div class="column">
                <h3>Bar Chart</h3>
                <line-chart msg='http://localhost:3000/api/logs/?created_at__date=2020-05-02&format=json'></line-chart>
            </div>
        </div>
        <div class="columns">
            <div class="column">
                <h3>Bubble Chart</h3>
                <bubble-chart></bubble-chart>
            </div>
            <div class="column">
                <h3>Reactivity - Live update upon change in datasets</h3>
                <reactive :chart-data="dataContents"></reactive>
                <button class="button is-primary" @click="fillData()">Ramdomize</button>
            </div>
        </div>
    </section>
</template>

<script>
import LineChart from './LineChart'
// import BarChart from './BarChart'
import BubbleChart from './BubbleChart'
import Reactive from './Reactive'
// import Stream from './Streaming'

export default {
  name: 'VueChartJS',
  components: {
    LineChart,
    // BarChart,
    BubbleChart,
    Reactive
    // Stream
  },
  data () {
    return {
      dataContents: null
    }
  },
  created () {
    this.fillData()
  },
  methods: {
    fillData () {
      this.dataContents = {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        datasets: [
          {
            label: 'Data reractive',
            backgroundColor: '#f8b979',
            data: [this.getRandomNum(), this.getRandomNum(), this.getRandomNum(), this.getRandomNum(), this.getRandomNum(), this.getRandomNum(), this.getRandomNum(), this.getRandomNum(), this.getRandomNum(), this.getRandomNum(), this.getRandomNum(), this.getRandomNum()]
          }
        ]
      }
    },
    getRandomNum () {
      return Math.floor(Math.random() * (50 - 5 + 1)) + 5
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
