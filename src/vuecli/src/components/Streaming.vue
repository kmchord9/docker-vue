<script>
import { Line } from 'vue-chartjs'
import 'chartjs-plugin-streaming'
import axios from 'axios'

export default {
  extends: Line,
  props: {
    msg: String
  },
  methods: {
    getdata: async (msg) => {
      var res = await axios.get(msg)
      console.log(msg)
      return res.data.ADT7410.temp
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
