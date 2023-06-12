import React from 'react'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import { AppProvider } from './Context'
import { Cadastro, Despesas, Estatisticas, Home, Login, Perfil, Rendas } from './Pages'

function App() {
  return (
    <AppProvider>
      <BrowserRouter>
          <Routes>
            <Route path='/' element={<Login/>} />
            <Route path='/home' element={<Home/>} />
            <Route path='/cadastro' element={<Cadastro/>} />
            <Route path='/perfil' element={<Perfil/>} />
            <Route path='/despesas' element={<Despesas/>} />
            <Route path='/rendas' element={<Rendas/>} />
            <Route path='/estatisticas' element={<Estatisticas/>} />
          </Routes>
      </BrowserRouter>
    </AppProvider>
  )
}

export default App;