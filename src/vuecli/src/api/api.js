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

const chartLogData = (phy, dev, pla, at, gt, id) => {
  at = (at === undefined) ? '' : at
  gt = (gt === undefined) ? '' : gt
  id = (id === undefined) ? '' : id
  return client.get('/users/')
    .then(res1 => {
      return client.get(`logs/?physics=${res1.data.physics[phy]}&\
device=${res1.data.device[dev]}&\
place=${res1.data.place[pla]}&\
created_at=${at}&\
created_gt=${gt}&\
id_num=${id}`)
        .then(res2 => {
          let parms = {'place': pla, 'physics': phy}
          res2.data.unshift(parms)
          return Promise.resolve(res2)
        })
    })
}

export {client, chartLogData}
