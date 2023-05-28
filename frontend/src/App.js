import React from 'react';

import { Home } from './Pages';
import Perfil from './Pages/Perfil/Perfil';

import { BrowserRouter, Route, Routes } from 'react-router-dom'

function App() {
  return (
      <BrowserRouter>
          <Routes>
            <Route path='/perfil' element={<Perfil/>} />
            <Route path='/home' element={<Home/>} />
          </Routes>
      </BrowserRouter>
  )
}

export default App;