import { useQueryListUsers } from "../../Services/queries";

export const Home = () => {
  const { data = [] } = useQueryListUsers()
  console.log(data)

  return (
    <>
      <div class="flex gap-4 items-center mb-[32px]">
        <div class="relative w-14 h-14 overflow-hidden bg-white rounded-full dark:bg-gray-600"></div>
        <div>
          <h1 class="text-white font-black text-bs">Olá, Maria da Silva</h1>
          <h2 class="text-white font-light text-sm">Bem-vinda de volta!</h2>
        </div>
      </div>
      <h1 class="text-lighterGray font-black text-bs mb-[20px]">Seu balanço</h1>
      <h1 class="text-white font-semibold text-3xl mb-[20px]">R$ 15.653</h1>
      <hr class="text-lightGray mb-[20px]"/>
      <h1 class="text-lighterGray font-black text-bs mb-[20px]">Visão geral</h1>
      <div class="relative w-auto min-h-[400px] overflow-hidden bg-gray rounded-xl dark:bg-gray-600 p-5">
        <div class="flex justify-between items-center mb-4">
          <h1 class="text-lighterGray font-medium text-bs">Investimentos</h1>
          <h2 class="text-lighterGray font-medium text-bs">+ R$ 500</h2>
        </div>
        <div class="flex justify-between items-center mb-4">
          <h1 class="text-lighterGray font-medium text-bs">Mercado</h1>
          <h2 class="text-lighterGray font-medium text-bs">- R$ 120</h2>
        </div>
        <div class="flex justify-between items-center mb-4">
          <h1 class="text-lighterGray font-medium text-bs">Hamburguer</h1>
          <h2 class="text-lighterGray font-medium text-bs">- R$ 34,98</h2>
        </div>
      </div>
    </>
  )

}

export default Home;