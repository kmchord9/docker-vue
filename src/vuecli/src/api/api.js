import axios from 'axios'
import moment from 'moment'

const BASE_URL = 'http://localhost:3001'

const client = axios.create({
  method: 'GET',
  baseURL: `${BASE_URL}/api`,
  resposeType: 'json',
  auth: {username: 'admin', password: 'mypass'},
  timeout: 5000
})

client.interceptors.response.use(
  (res) => {
    let sensorData = {
      'temperature': [],
      'humidity': [],
      'create': []
    }
    res.data.forEach((element) => {
      sensorData.temperature.push(element.temperature)
      sensorData.humidity.push(element.humidity)
      sensorData.create.push(
        moment(element.created_at).format('YYYY-MM-DD HH:mm:ss')
      )
    })
    res.data = sensorData
    return res
  }
)

export default client
