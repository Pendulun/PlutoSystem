import { IconEditar } from './components/icon_editar.js';
import { OpcoesEstaticas } from './components/opcoes_estaticas.js';

export const Login = () => {
  
    const handleClickCadastro = () => {
      // Navegar para a tela de cadastro
      const cadastroUrl = '/cadastro';
      window.location.href = cadastroUrl;
    }
  
    return (
      <div class="flex flex-col items-center h-screen">
        <IconEditar/>
        <div class="text-white font-Inter font-bold text-bs mt-[32px] mb-[4px]">Maria da Silva</div>
        <div class="text-white font-Inter font-normal text-xs mb-[12px]">maria.23@mail.com</div>
        <OpcoesEstaticas/>
        <button class="mb-4 w-32 h-6 bg-darkTeal rounded-lg"><span class="text-white text-sm font-bold">Sair</span></button>
      </div>
    )
    
  }
  
  export default Login;