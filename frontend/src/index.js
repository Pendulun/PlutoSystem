import React from 'react'
import ReactDOM from 'react-dom/client'
import { Toaster } from 'react-hot-toast'
import {
  QueryClient,
  QueryClientProvider,
} from 'react-query'
import App from './App'
import { TabBar } from './Components'
import './index.css'

const root = ReactDOM.createRoot(document.getElementById('root'))
const queryClient = new QueryClient()
const isLogged = (window.location.pathname === '/cadastro' || window.location.pathname === '/') ? false : true

root.render(
  <QueryClientProvider client={queryClient}>
    <Toaster/>
    {isLogged && <TabBar/>}
    <App />
  </QueryClientProvider>
)
