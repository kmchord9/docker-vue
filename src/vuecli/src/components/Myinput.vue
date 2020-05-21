<template>
  <div id="app">
    <tr>
      <td align="right">日付:</td>
      <td><input type="text" v-model="create"></td>
      <td align="right">場所:</td>
      <td><input type="text" v-model="place"></td>
    </tr>
    <tr>
      <td align="right">センサー:</td>
      <td><input type="text" v-model="device"></td>
      <td align="right">物理量:</td>
      <td><input type="text" v-model="physic"></td>
      <td><button v-on:click="readData">更新</button></td>
    </tr>
    <reactive
      ref="read"
      :create="create"
      :device="device"
      :place="place"
      :physic="physic"/>
  </div>
</template>
<script>
import Reactive from './Reactive'
import moment from 'moment'

export default {
  name: 'MyInput',
  components: {
    Reactive
  },
  data () {
    return {
      create: moment(new Date()).format('YYYY-MM-DD'),
      place: '部屋001',
      device: 'BME280',
      physic: '温度'
    }
  },
  methods: {
    readData () {
      this.$refs.read.setChartData()
    }
  }
}
</script>
