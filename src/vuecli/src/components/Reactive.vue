<script>
import { Line, mixins } from 'vue-chartjs'
// import { getChartDataFormat, getChartOptionFormat, chartDataArray } from '../api/api'

export default {
  extends: Line,
  mixins: [mixins.reactiveProp],
  props: [
    'chartData',
    'options'
  ],
  mounted () {
    this.renderChart(this.chartData, this.options)
  }
}
</script>

<style scoped>
</style>
