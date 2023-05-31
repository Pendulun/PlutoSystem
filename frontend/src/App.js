import React from 'react'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import { Home, Login, Cadastro, Rendas, Despesas, Estatisticas, Perfil } from './Pages'
import { AppProvider } from './Context'

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