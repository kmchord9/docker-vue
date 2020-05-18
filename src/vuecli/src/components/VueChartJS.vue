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
                <stream dev="ADT7410" room="部屋002"></stream>
            </div>
            <div class="column">
                <h3>Bar Chart</h3>
                <stream dev="MAX31855" room="部屋003"></stream>
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
import Stream from './Streaming'
import {chartLogData} from '../api/api'

export default {
  name: 'VueChartJS',
  components: {
    LineChart,
    // BarChart,
    BubbleChart,
    Reactive,
    Stream
  },
  data () {
    return {
      chartData: [],
      dataContents: null
    }
  },
  created () {
    this.fillData()
  },
  methods: {
    promiseGet (phy, dev, pla, at, gt, id) {
      return chartLogData(phy, dev, pla, at, gt, id)
        .then(res => {
          this.label = `${res.data[0]['place']}の${res.data[0]['physics']}`
          res.data.slice(1).forEach(element => {
            this.chartData.push({
              t: new Date(element['created_at']),
              y: element['value']
            })
          })
          return Promise.resolve()
        })
    },
    fillData () {
      this.promiseGet('温度', 'MAX31855', '部屋003', '2020-05-18')
        .then(() => {
          this.dataContents = {
            labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
            datasets: [
              {
                label: 'Data reractive',
                backgroundColor: '#f8b979',
                data: this.chartData
              }
            ]
          }
        })
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
