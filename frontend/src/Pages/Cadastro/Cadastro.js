import { toast } from 'react-hot-toast'
import { useMutationRegister } from '../../Services/queries'

export const Cadastro = () => {
  const register = useMutationRegister()

  const handleSubmit = () => {
    const nome = document.getElementById('nome').value
    const email = document.getElementById('email').value
    const senha = document.getElementById('senha').value
  
    const dadosUsuario = {
      name: nome,
      email: email,
      password: senha
    }

    register.mutate(dadosUsuario, {
      onSuccess: () => {
        toast.success('Cadastro realizado com sucesso!', { duration: 5000})
        document.getElementById('nome').value = ''
        document.getElementById('email').value = ''
        document.getElementById('senha').value = ''
      },
      onError: (error) => {
        toast.error(error)
      },
    })
  }
  
  const handleClickLogin = () => {
    window.location.href = '/'
  }

  return (
    <div class="flex flex-col justify-center items-center h-screen">
      <h1 class="text-white font-Inter font-bold text-2xl">Bem-vindo!</h1>
      <h2 class="text-gray3 font-Inter font-normal text-sm14 mb-[48px]">Entre no PlutoSystem!</h2>
      <input data-cy="name" id="nome" class="w-64 h-10 rounded-t-lg outline outline-1 outline-gray4 bg-gray2 placeholder-gray4 pl-5 pr-5" type="text" placeholder="Nome"></input>
      <input data-cy="email" id="email" class="w-64 h-10 outline outline-1 outline-gray4 bg-gray2 placeholder-gray4 pl-5 pr-5" type="text" placeholder="Email"></input>
      <input data-cy="password" id="senha" class="mb-4 w-64 h-10 rounded-b-lg outline outline-1 outline-gray4 bg-gray2 placeholder-gray4 pl-5 pr-5" type="password" placeholder="Senha"></input>
      <button data-cy="submit" class="mb-4 w-56 h-10 bg-darkTeal rounded-lg" onClick={handleSubmit}><span class="text-white text-sm font-bold">Cadastrar</span></button>
      <div class="border border-gray5 h-0 w-64"></div>
      <div class="mt-2 whitespace-no-wrap flex-col">
        <p class="text-xs flex-shrink">
          <span class="text-white font-Inter text-sm font-normal">Já tem uma conta? </span>
          <button class="text-teal-400 font-Inter text-sm font-normal text-lightBlue" onClick={handleClickLogin}>Entre</button>
        </p>
      </div>
    </div>
  )
  
}

export default Cadastro