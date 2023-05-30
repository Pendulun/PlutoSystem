const UserService = require('../services/users')
const apiServerClient = require('../client/apiServer')

const getUser = async (req, res, next) => {
    try {
        const userService = new UserService(new apiServerClient())
        const userGetResponse = await userService.getUser(req)
        res.status(200).send(userGetResponse.data)
    } catch (e) {
        next(e)
    }
}

const getUsers = async (req, res, next) => {
    try {
        const userService = new UserService(new apiServerClient())
        const userGetResponse = await userService.getUser(req)
        res.status(200).send(userGetResponse.data)
    } catch (e) {
        next(e)
    }
}

const postUser = async (req, res, next) => {
    try {
        const userService = new UserService(new apiServerClient())
        const userPostResponse = await userService.postUser(req)
        res.status(200).send(userPostResponse.data)
    } catch (e) {
        next(e)
    }
}

const putUser = async (req, res, next) => {
    try {
        const userService = new UserService(new apiServerClient())
        const userPutResponse = await userService.putUser(req)
        res.status(200).send(userPutResponse.data)
    } catch (e) {
        next(e)
    }
}

module.exports = {
    getUser,
    getUsers,
    postUser,
    putUser,
}
