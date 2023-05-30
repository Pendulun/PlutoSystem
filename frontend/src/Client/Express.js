import axios from 'axios'

const EXPRESS_CLIENT_TIMEOUT = 1000 // Milliseconds

class ExpressClient {
    constructor() {
        const APPLICATION_JSON_MIME_TYPE = 'application/json'

        this.instance = axios.create({
            baseURL: window.location.origin,
            timeout: EXPRESS_CLIENT_TIMEOUT,
            headers: {
                common: {
                    Accept: APPLICATION_JSON_MIME_TYPE,
                },
                post: { 'Content-Type': APPLICATION_JSON_MIME_TYPE },
                put: { 'Content-Type': APPLICATION_JSON_MIME_TYPE },
            },
        })
    }

    async get(url, config = {}) {
        return this.instance.get(url, config)
    }

    async post(url, data = {}, config = {}) {
        return this.instance.post(url, JSON.stringify(data), config)
    }

    async put(url, data = {}, config = {}) {
        return this.instance.put(url, JSON.stringify(data), config)
    }

    async postUser(data) {
        const url = '/users'
        console.log("Posting to /users/")
        this.post(url, data)
    }
}

export default ExpressClient
