<script>
import { Bubble } from 'vue-chartjs'

export default {
  extends: Bubble,
  mounted () {
    this.renderChart({
      labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
      datasets: [
        {
          label: 'Data',
          backgroundColor: '#79f8b9',
          data: [
            {
              x: 100,
              y: 0,
              r: 10
            },
            {
              x: 60,
              y: 30,
              r: 20
            },
            {
              x: 40,
              y: 60,
              r: 25
            },
            {
              x: 80,
              y: 80,
              r: 50
            },
            {
              x: 30,
              y: 100,
              r: 5
            }
          ]
        }
      ]
    })
  }
}
</script>

<style scoped>
</style>
