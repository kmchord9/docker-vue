<script>
import { Line } from 'vue-chartjs'
// import moment from 'moment'
// import axios from 'axios'
import client from '../api/api'

export default {
  extends: Line,
  data: () => {
    return {
      charty: [],
      chartt: []
      // timestamp: ['2018/04/16 22:18', '2018/04/16 23:18', '2018/04/17 00:18', '2018/04/17 01:18']
    }
  },
  props: {
    msg: String
  },
  methods: {
    getdata: async () => {
      return client.get('/logs/?created_gt=2020-05-09 15:15:18')
    },
    setdata: (arrT, arrY) => {
      const data = []
      if (arrT.length === arrY.length) {
        for (let i = 0; i < arrT.length; i++) {
          // console.log(arrT[i])
          data.push({
            t: arrT[i],
            y: arrY[i]
          })
        }
      } else {
        console.log('The number of elements is different')
      }
      console.log(data)
      return data
    }
  },
  async mounted () {
    const res = await this.getdata()
    this.charty = res.data.temperature
    res.data.created_at.forEach(element => {
      this.chartt.push(new Date(element))
    })
    // this.chartt = res.data.created_at
    var plot = this.setdata(this.chartt, this.charty)

    this.renderChart({
      datasets: [
        {
          label: 'Data',
          backgroundColor: 'rgba(0,0,0,0)',
          borderColor: 'rgba(255,0,0,1)',
          lineTension: 0.4,
          // borderWidth: 1,
          data: plot
        }
      ]
    },
    {
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
  }
}
</script>

<style scoped>
</style>
