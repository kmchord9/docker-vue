<script>
import { Line } from 'vue-chartjs'
import 'chartjs-plugin-streaming'
// import axios from 'axios'
import moment from 'moment'
import {chartLogData} from '../api/api'

export default {
  extends: Line,
  data: () => {
    return {
      chartData: [],
      // lastDate: undefined,
      lastDate: moment(new Date()).format('YYYY-MM-DD HH:mm:ss.SSS')
      // todate: moment(new Date()).format('YYYY-MM-DD')
    }
  },
  props: {
    dev: String,
    room: String
  },
  methods: {
    async getdata (dev, room, at, gt) {
      // at = (gt === undefined) ? at : ''
      console.log(`更新時間1${this.lastDate}`)
      let res = await chartLogData('温度', dev, room, at, gt)
      res.data.slice(1).forEach(element => {
        this.chartData.push({
          t: new Date(element['created_at']),
          y: element['value']
        })
      })
      this.lastDate = moment(this.chartData.slice(-1)[0]['t']).format('YYYY-MM-DD HH:mm:ss.SSS')
      console.log(`更新時間2${this.lastDate}`)
    }
  },
  mounted () {
    this.renderChart({
      datasets: [{
        label: 'label',
        data: this.chartData,
        borderColor: 'rgba(255,0,0,1)',
        backgroundColor: 'rgba(0,0,0,0)'
      }]
    }, {
      scales: {
        xAxes: [{
          type: 'realtime',
          realtime: {
            delay: 2000,
            refresh: 5000,
            duration: 300000,
            onRefresh: () => {
              this.getdata(this.dev, this.room, '', this.lastDate)
            }
          }
        }],
        yAxes: [{
          ticks: {
            suggestedMax: 40,
            suggestedMin: 20,
            stepSize: 2
          }
        }]
      }
    })
  }
}
</script>
