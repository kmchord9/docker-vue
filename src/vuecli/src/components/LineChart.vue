<script>
import { Line } from 'vue-chartjs'
// import moment from 'moment'
// import axios from 'axios'
import client from '../api/api'

export default {
  extends: Line,
  data: () => {
    return {
      chartx: []
    }
  },
  props: {
    msg: String
  },
  methods: {
    getdata: async () => {
      return client.get('/logs/')
    }
  },
  created () {
    this.getdata().then((res) => {
      this.chartx = res.data.temperature
    })
  },
  mounted () {
    this.getdata().then((res) => {
      this.renderChart({
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        datasets: [
          {
            label: 'Data',
            backgroundColor: '#f87979',
            borderWidth: 1,
            data: this.chartx
          }
        ]
      })
    })
  }
}
</script>

<style scoped>
</style>
