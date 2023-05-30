const axios = require('axios')

class apiServerClient {

    constructor() {
        const APPLICATION_JSON_MIME_TYPE = 'application/json'

        this.instance = axios.create({
            // Notice that we need API_SERVER_URL to be defined in the environmment.
            baseURL: 'http://localhost:5000',
            timeout: 1000, // Milliseconds
            headers: {
                common: { Accept: APPLICATION_JSON_MIME_TYPE },
                post: { 'Content-Type': APPLICATION_JSON_MIME_TYPE },
                put: { 'Content-Type': APPLICATION_JSON_MIME_TYPE },
            },
        })

        this.instance.defaults.headers['Content-Type'] = APPLICATION_JSON_MIME_TYPE
    }

    async get(...args) {
        return this.instance.get(...args)
    }

    async post(...args) {
        return this.instance.post(...args)
    }

    async put(...args) {
        return this.instance.put(...args)
    }

    async getUser(req) {
        return await this.get(req.originalUrl, req)
            .then(res => res)
            .catch(e => {
                throw e
            })
    }

    async getUsers(req) {
        return await this.get(req.originalUrl, req)
            .then(res => res)
            .catch(e => {
                throw e
            })
    }

    async postUser(req) {
        return await this.post(req.originalUrl, req)
            .then(res => res)
            .catch(e => {
                throw e
            })
    }

    async putUser(req) {
        return await this.put(req.originalUrl, req)
            .then(res => res)
            .catch(e => {
                throw e
            })
    }
}

module.exports = apiServerClient
