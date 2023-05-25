import React from 'react';

import Home from './Pages/Home/Home';
import Login from './Pages/Login/Login';
import Cadastro from './Pages/Cadastro/Cadastro';

import { BrowserRouter, Route, Routes } from 'react-router-dom'

// Criando c component 
class App extends React.Component {
    // Função que renderiza o componente
    render() {
        return (
           <BrowserRouter>
                <Routes>
                  <Route path='/' element={<Home/>} />
                  <Route path='/login' element={<Login/>} />
                  <Route path='/cadastro' element={<Cadastro/>} />
                </Routes>
           </BrowserRouter>
        )
    }

}

export default App;