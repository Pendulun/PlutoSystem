const express = require('express')
require('dotenv').config()

const usersRouter = require('./routers/users')

PORT = process.env.PORT || 3001
const app = express()

app.disable('etag');

// Please set all the base routers in place here
app.use('/users', usersRouter)

// Necessary to refresh requests, otherwise will get 304 status
app.get('/*', function(_, res, next){ 
    res.setHeader('Last-Modified', (new Date()).toUTCString())
    next();
})

app.listen(PORT, () => {
    console.log(`BFF server listening on port ${PORT}`)
})
