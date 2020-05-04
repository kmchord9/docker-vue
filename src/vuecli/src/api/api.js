import axios from 'axios'

const BASE_URL = 'http://localhost:3000'

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
      'humidity': []
    }
    res.data.forEach((element) => {
      sensorData.temperature.push(element.temperature)
      sensorData.humidity.push(element.humidity)
    })
    res.data = sensorData
    return res
  }
)

export default client
