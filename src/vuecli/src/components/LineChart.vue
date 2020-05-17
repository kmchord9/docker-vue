<script>
import { Line } from 'vue-chartjs'
// import moment from 'moment'
// import axios from 'axios'
import {chartLogData} from '../api/api'

export default {
  extends: Line,
  data: () => {
    return {
      chartData: [],
      label: 'testlabels'
    }
  },
  props: {
    msg: String
  },
  methods: {
    async getdata (at, gt) {
      let res = await chartLogData('温度', 'BME280', '部屋028', at, gt)
      console.log(res.data[0]['place'])
      this.label = `${res.data[0]['place']}の${res.data[0]['physics']}`
      res.data.slice(1).forEach(element => {
        this.chartData.push({
          t: new Date(element['created_at']),
          y: element['value']
        })
      })
      // this.lastDate = moment(this.chartData.slice(-1)[0]['t']).format('YYYY-MM-DD hh:mm:ss.SSS')
      // console.log(`更新時間${this.lastDate}`)
    },
    promiseGet (phy, dev, pla, at, gt, id) {
      console.log(this.label)
      return chartLogData(phy, dev, pla, at, gt, id)
        .then(res => {
          console.log(this.label)
          this.label = `${res.data[0]['place']}の${res.data[0]['physics']}`
          res.data.slice(1).forEach(element => {
            this.chartData.push({
              t: new Date(element['created_at']),
              y: element['value']
            })
          })
          return Promise.resolve()
        })
    }
  },
  created () {
    console.log('create')
    // this.getdata('2020-05-17')
    // console.log(this.chartData)
  },
  mounted () {
    console.log('mount')
    console.log(this.chartData)
    this.promiseGet('温度', 'BME280', '部屋028', '2020-05-16')
      .then(() => {
        this.renderChart({
          datasets: [{
            label: this.label,
            backgroundColor: 'rgba(0,0,0,0)',
            borderColor: 'rgba(255,0,0,1)',
            // lineTension: 0.4,
            // borderWidth: 1,
            data: this.chartData
          }]
        }, {
          scales: {
            xAxes: [{
              type: 'time'
              // time: {
              // unit: 'second',
              // displayFormats: {
              //   second: 'h:mm:ss'
              // }
              // }
            }]
          }
        })
      })
  }
}
</script>

<style scoped>
</style>
