// import { useQuery } from "react-query"
import axios from "axios";

export const Login = () => {
  const handleSubmit = () => {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
  
    const dadosLogin = {
      email: email,
      password: password
    }

    axios.get('http://127.0.0.1:5000/users/', { params: dadosLogin } )
      .then(response => {
        localStorage.setItem('user', JSON.stringify(response?.data[0]))
        window.location.href = '/home'
      })
      .catch(error => {
        alert('Ocorreu um erro no login. Por favor, verifique suas credenciais e tente novamente.')
        console.error('Ocorreu um erro:', error)
      });
  }
  
  const handleClickCadastro = () => {
    window.location.href = '/cadastro'
  }

  return (
    <div class="flex flex-col justify-center items-center h-screen">
      <h1 class="text-white font-Inter font-bold text-2xl">Bem-vindo!</h1>
      <h2 class="text-gray3 font-Inter font-normal text-sm14 mb-[48px]">Entre no PlutoSystem!</h2>
      <input data-cy="email" id="email" class="w-64 h-10 rounded-t-lg outline outline-1 outline-gray4 bg-gray2 placeholder-gray4 pl-5 pr-5" type="text" placeholder="Email"></input>
      <input data-cy="password" id="password" class="mb-4 w-64 h-10 rounded-b-lg outline outline-1 outline-gray4 bg-gray2 placeholder-gray4 pl-5 pr-5" type="password" placeholder="Senha"></input>
      <button data-cy="submit" class="mb-4 w-56 h-10 bg-darkTeal rounded-lg" onClick={handleSubmit}><span class="text-white text-sm font-bold">Entrar</span></button>
      <div class="border border-gray5 h-0 w-64"></div>
      <div class="mt-2 whitespace-no-wrap flex-col">
        <p class="text-xs flex-shrink">
          <span class="text-white font-Inter text-sm font-normal">Ainda não tem uma conta? </span>
          <button class="text-teal-400 font-Inter text-sm font-normal text-lightBlue" onClick={handleClickCadastro}>Cadastre-se</button>
        </p>
      </div>
    </div>
  )
  
}

export default Login