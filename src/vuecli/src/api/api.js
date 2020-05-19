import axios from 'axios'
// import moment from 'moment'

const BASE_URL = 'http://localhost:3001'

const client = axios.create({
  method: 'GET',
  baseURL: `${BASE_URL}/api`,
  resposeType: 'json',
  auth: {username: 'admin', password: 'mypass'},
  timeout: 5000
})

const chartLogData = (phy, dev, pla, at, gt) => {
  at = (at === undefined) ? '' : at
  gt = (gt === undefined) ? '' : gt
  return client.get('/users/')
    .then(res1 => {
      return client.get(`logs/?physics=${res1.data.physics[phy]}&\
device=${res1.data.device[dev]}&\
place=${res1.data.place[pla]}&\
created_at=${at}&\
created_gt=${gt}`)
        .then(res2 => {
          let parms = {'place': pla, 'physics': phy}
          res2.data.unshift(parms)
          return Promise.resolve(res2)
        })
    })
}

const chartDataArray = (phy, dev, pla, at, gt) => {
  return chartLogData(phy, dev, pla, at, gt)
    .then(res => {
      // let labelAndData = {'label': null, 'data': null}
      let cdata = []
      let label = `${res.data[0]['place']}の${res.data[0]['physics']}`
      res.data.slice(1).forEach(element => {
        // console.log(`cdata${element['created_at']}`)
        // console.log(`cdata${element['value']}`)
        cdata.push({
          t: new Date(element['created_at']),
          y: element['value']
        })
      })
      // labelAndData.label = label
      // labelAndData.data = cdata
      // console.log(`cdata${cdata[1]['t']}`)
      return Promise.resolve([label, cdata])
    })
}

const getChartDataFormat = (labels, datas) => {
  return {
    datasets: [{
      label: labels,
      backgroundColor: 'rgba(0,0,0,0)',
      borderColor: 'rgba(255,0,0,1)',
      data: datas
    }]
  }
}

const getChartOptionFormat = () => {
  return {
    scales: {
      xAxes: [{
        type: 'time'
      }]
    },
    plugins: {
      streaming: false
    }
  }
}

export {client, chartLogData, getChartDataFormat, getChartOptionFormat, chartDataArray}
