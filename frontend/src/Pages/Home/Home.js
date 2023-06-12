import { useMemo } from 'react'
import { toast } from 'react-hot-toast'
import { Loading } from '../../Components'
import { useData } from '../../Hooks'
import { useQueryListExpenses, useQueryListIncomes } from "../../Services/queries"
import { ListItemExpense, ListItemIncome } from './Components'

export const Home = () => {
  const { getBalance } = useData()

  const handleClickPerfil = () => { window.location.href = '/perfil' }

  const user = JSON.parse(localStorage?.getItem('user'))

  const { data: incomes, isLoading: isLoadingIncomes, isError: isErrorIncomes } = useQueryListIncomes(user.id)
  const { data: { expenses } = {}, isLoading: isLoadingExpenses, isError: isErrorExpenses } = useQueryListExpenses(user.id)

  const balance = useMemo(() => getBalance(incomes, expenses), [incomes, expenses, getBalance])

  if (isLoadingExpenses || isLoadingIncomes) return <Loading/>
  if (isErrorExpenses || isErrorIncomes) toast.error('Erro ao carregar informações, por favor atualize a página')

  return (
    <div class="max-w-xl mx-auto">
      <button data-cy="profile-picture" class="flex gap-4 items-center mb-[32px]" onClick={handleClickPerfil}>
        <div class="relative w-14 h-14 overflow-hidden bg-white rounded-full dark:bg-gray-600"></div>
        <div class="text-left">
          <div class="text-white font-black text-bs">Olá, {user.name}</div>
          <div class="text-white font-light text-sm">Bem-vind@ de volta!</div>
        </div>
      </button>
      <h1 class="text-lighterGray font-black text-bs mb-[20px]">Seu balanço</h1>
      <h1 data-cy="total-balance" class="text-white font-semibold text-2xl mb-[20px]">R$ {balance}</h1>
      <hr class="text-lightGray mb-[20px]"/>
      <h1 class="text-lighterGray font-black text-bs mb-[20px]">Visão geral</h1>
      <div class="relative w-auto min-h-[340px] overflow-hidden bg-gray rounded-xl dark:bg-gray-600 p-5">
        <h1 class="text-lighterGray font-black text-bs mb-[10px] text-center">Rendas</h1>
        <hr class="text-lightGray mb-[25px]"/>
        {incomes?.map((item) => (
          <ListItemIncome title={item?.src} value={item?.amount}/>
        ))}
        {expenses?.length > 0 && (
          <>
            <h1 class="text-lighterGray font-black text-bs mb-[10px] mt-[40px] text-center">Despesas</h1>
            <hr class="text-lightGray mb-[25px]"/>
          </>
        )}

        {expenses?.map((item) => (
          <ListItemExpense title={item?.src} value={item?.amount}/>
        ))}
      </div>
    </div>
  )

}

export default Home