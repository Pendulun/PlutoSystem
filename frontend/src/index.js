import React from 'react'
import ReactDOM from 'react-dom/client'
import './index.css'
import App from './App'
import { TabBar } from './Components'
import {
  QueryClient,
  QueryClientProvider,
} from 'react-query'

const root = ReactDOM.createRoot(document.getElementById('root'))
const queryClient = new QueryClient()
const isLogged = (window.location.pathname === '/cadastro' || window.location.pathname === '/') ? false : true

root.render(
  <React.StrictMode>
    <QueryClientProvider client={queryClient}>
      {isLogged && <TabBar/>}
      <App />
    </QueryClientProvider>
  </React.StrictMode>,
)
