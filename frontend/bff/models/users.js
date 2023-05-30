class User {
    constructor(apiServerClient) {
        this.apiServerClient = apiServerClient
    }

    async getUser(req) {
        return await this.apiServerClient
            .getUser(req)
            .then(res => res)
            .catch(e => {
                throw e
            })
    }

    async getUsers(req) {
        return await this.apiServerClient
            .getUsers(req)
            .then(res => res)
            .catch(e => {
                throw e
            })
    }

    async postUser(req) {
        return await this.apiServerClient
            .postUser(req)
            .then(res => res)
            .catch(e => {
                throw e
            })
    }

    async putUser(req) {
        return await this.apiServerClient
            .putUser(req)
            .then(res => res)
            .catch(e => {
                throw e
            })
    }
}

module.exports = User
