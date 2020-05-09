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
      'created_at': []
    }
    res.data.forEach((element) => {
      sensorData.temperature.push(element.temperature)
      sensorData.humidity.push(element.humidity)
      sensorData.created_at.push(moment(element.created_at).format('YYYY/MM/DD HH:mm:ss'))
      // sensorData.created_at.push(element.created_at)
    })
    res.data = sensorData
    // console.log(res.data)
    return res
  }
)

export default client
