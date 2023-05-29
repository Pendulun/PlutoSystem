import { IconEditar } from './components/Icons/icon_editar.js';
import { IconMudarNomeUsuario, IconMudarEmail, IconDeletarConta, IconTermosECondicoes } from './components/Icons/opcoes_estaticas.js';
import { AccountButton } from './components/AccountButton.js'

export const Login = () => {
  
  const handleClickLogin = () => {
    //Navegar para a tela de Login
    const cadastroUrl = '/';
    window.location.href = cadastroUrl;
  }

  return (
    <div class="flex flex-col min-h-screen max-w-lg mx-auto pt-[60px] px-6 items-center">
      <div class="flex flex-col items-center">
        <div className='w-[154px] mx-auto bg-gray aspect-square rounded-full overflow-hidden -mb-6'>
          <img alt="" />
        </div>
        <IconEditar/>
      </div>

      <div class="text-white font-Inter font-bold text-rg mt-[30px]">Maria da Silva</div>
      <div class="text-white font-Inter font-normal text-bs mb-[60px]">maria.23@mail.com</div>
      
      <div class="w-full justify-start text-bs">
        <AccountButton title='Mudar nome do Usuário' icon={<IconMudarNomeUsuario/>}/>
        <hr class="text-gray5 mb-[22px]"></hr>

        <AccountButton title='Mudar email' icon={<IconMudarEmail/>}/>
        <hr class="text-gray5 mb-[22px]"></hr>

        <AccountButton title='Deletar conta' icon={<IconDeletarConta/>}/>
        <hr class="text-gray5 mb-[22px]"></hr>

        <AccountButton title='Termos e condições' icon={<IconTermosECondicoes/>}/>
        <hr class="text-gray5 mb-[22px]"></hr>
      </div>

      <button class="mt-[40px] w-[218px] h-[40px] bg-darkTeal rounded-lg" onClick={handleClickLogin}><span class="text-white text-sm font-bold">Sair</span></button>
    </div>
  )
    
}
  
export default Login;
