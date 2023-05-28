import { IconEditar } from './components/icon_editar.js';
import { IconMudarNomeUsuario, IconMudarEmail, IconDeletarConta, IconTermosECondicoes } from './components/opcoes_estaticas.js';

export const Login = () => {
  
  const handleClickLogin = () => {
    //Navegar para a tela de Login
    const cadastroUrl = '/';
    window.location.href = cadastroUrl;
  }

  return (
    <div class="flex flex-col items-center h-screen">
      <IconEditar/>
      <div class="text-white font-Inter font-bold text-bs mt-[12px]">Maria da Silva</div>
      <div class="text-white font-Inter font-normal text-xs mb-[32px]">maria.23@mail.com</div>
      <div class="flex flex-col justify-start">
        <div class="flex justify-start mb-[10px]">
          <IconMudarNomeUsuario/>
          <div class="ml-4">
            <p class="text-white font-Inter font-normal text-sm14">Mudar nome do Usuário</p>
          </div>
        </div>
        <div class="border border-gray5 h-0 w-52 mb-[10px]"></div>
        <div class="flex justify-start mb-[10px]">
          <IconMudarEmail/>
          <div class="ml-4">
            <p class="text-white font-Inter font-normal text-sm14">Mudar Email</p>
          </div>
        </div>
        <div class="border border-gray5 h-0 w-52 mb-[10px]"></div>
        <div class="flex justify-start mb-[10px]">
          <IconDeletarConta/>
          <div class="ml-4">
            <p class="text-white font-Inter font-normal text-sm14">Deletar conta</p>
          </div>
        </div>
        <div class="border border-gray5 h-0 w-52 mb-[10px]"></div>
        <div class="flex justify-start mb-[10px]">
          <IconTermosECondicoes/>
          <div class="ml-4">
            <p class="text-white font-Inter font-normal text-sm14">Termos e Condições</p>
          </div>
        </div>
        <div class="border border-gray5 h-0 w-52 mb-[24px]"></div>
      </div>
      <button class="mb-4 w-32 h-6 bg-darkTeal rounded-lg" onClick={handleClickLogin}><span class="text-white text-sm font-bold">Sair</span></button>
    </div>
  )
    
}
  
export default Login;