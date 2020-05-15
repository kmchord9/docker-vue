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

const chartLogData = (pla, phy) => {
  return client.get('/users/')
    .then(res1 => {
      return client.get(`logs/?place=${res1.data.place[pla]}&physics${res1.data.physics[phy]}`)
        .then(res2 => {
          let parms = {'place': pla, 'physics': phy}
          res2.data.unshift(parms)
          return Promise.resolve(res2)
        })
    })
}

export default {client, chartLogData}
