import React from 'react';

import Home from './Pages/Home/Home';
import Login from './Pages/Login/Login';
import Cadastro from './Pages/Cadastro/Cadastro';
import Perfil from './Pages/Perfil/Perfil';

import { BrowserRouter, Route, Routes } from 'react-router-dom'

function App() {
  return (
      <BrowserRouter>
          <Routes>
            <Route path='/' element={<Login/>} />
            <Route path='/home' element={<Home/>} />
            <Route path='/cadastro' element={<Cadastro/>} />
            <Route path='/perfil' element={<Perfil/>} />
          </Routes>
      </BrowserRouter>
  )
}

export default App;