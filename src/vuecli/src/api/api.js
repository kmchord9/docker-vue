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

const chartLogData = (at, phy, dev, pla) => {
  return client.get('/users/')
    .then(res1 => {
      return client.get(`logs/?created_at=${at}&\
physics=${res1.data.physics[phy]}&\
device=${res1.data.device[dev]}&\
place=${res1.data.place[pla]}`)
        .then(res2 => {
          let parms = {'place': pla, 'physics': phy}
          res2.data.unshift(parms)
          return Promise.resolve(res2)
        })
    })
}

export {client, chartLogData}
