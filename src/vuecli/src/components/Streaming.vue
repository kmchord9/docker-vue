<script>
import { Line } from 'vue-chartjs'
import 'chartjs-plugin-streaming'
import axios from 'axios'
import client from '../api/api'

export default {
  extends: Line,
  data: () => {
    return {
      lasttime: '',
      temp: ''
    }
  },
  props: {
    msg: String
  },
  methods: {
    setdata: async () => {
      //var url = ''
      client.get('/logs/?created_gt=2020-05-08 15:22:14')
        .then(res => {
          this.temp = res.data.temperature
        })
    },
    getdata: () => {
      this.setdata()
      return this.temp
    }
  },
  mounted () {
    this.renderChart({
      datasets: [{
        data: [],
        borderColor: 'rgba(255,0,0,1)',
        backgroundColor: 'rgba(0,0,0,0)'
      }]
    }, {
      scales: {
        xAxes: [{
          type: 'realtime',
          realtime: {
            delay: 2000,
            refresh: 2000,
            duration: 300000,
            onRefresh: (chart) => {
              chart.data.datasets.forEach(async (dataset) => {
                dataset.data.push({
                  x: Date.now(),
                  y: await this.getdata(this.msg)
                })
              })
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
