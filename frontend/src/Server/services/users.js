const User = require('../models/users')

class UserService {
    constructor(apiServerClient) {
        this.User = new User(apiServerClient)
    }

    async getUser(req) {
        try {
            return await this.User.getUser(req)
        } catch (e) {
            throw e
        }
    }

    async getUsers(req) {
        try {
            return await this.User.getUsers(req)
        } catch (e) {
            throw e
        }
    }

    async postUser(req) {
        try {
            return await this.User.postUser(req)
        } catch (e) {
            throw e
        }
    }

    async putUser(req) {
        try {
            return await this.User.putUser(req)
        } catch (e) {
            throw e
        }
    }
}

module.exports = UserService
