import axios from 'axios'

export function request(config) {
    const instance = axios.create({
        baseURL: 'http://127.0.0.1:8000',
        timeout: 5000,
    })

    instance.interceptors.request.use(config => {
        config.headers.Authorization = sessionStorage.getItem('token')
        window.console.log(config)
        return config
    }, err => {
        window.console.log(err)
    })

    instance.interceptors.response.use(config => {
        return config
    }, err => {
        window.console.log(err)
    })

    return instance(config)
}