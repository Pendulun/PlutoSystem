const express = require('express')
const handler = require('../handlers/users')
const router = express.Router()

const USERS_ROOT_PATH = '/'

router.get(USERS_ROOT_PATH, handler.getUsers)
router.post(USERS_ROOT_PATH, handler.postUser)

router.use((err, req, res, next) => {
    console.log(err)
})

module.exports = router
