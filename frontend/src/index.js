import React from 'react'
import ReactDOM from 'react-dom/client'
import './index.css'
import App from './App'
import { TabBar } from './Components'

const root = ReactDOM.createRoot(document.getElementById('root'))
const isLogged = (window.location.pathname === '/cadastro' || window.location.pathname === '/') ? false : true

root.render(
  <React.StrictMode>
    {isLogged && <TabBar/>}
    <App />
  </React.StrictMode>,
)
