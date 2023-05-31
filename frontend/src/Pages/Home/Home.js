import { useMemo, useState } from "react";
import axios from 'axios';
import { ListItemIncome, ListItemExpense } from './Components/ListItem'
import { useUserContext } from "../../Context/useContextValues";

export const Home = () => {
  const { user } = useUserContext()
  const [incomes, setIncomes] = useState()
  const [expenses, setExpenses] = useState()

  const handleClickPerfil = () => {
    // Navegar para a tela de cadastro
    const cadastroUrl = '/perfil';
    window.location.href = cadastroUrl;
  }

  const _incomes = useMemo(() => {
    axios.get(`http://127.0.0.1:5000/incomes/?user_id=${user.id}`)
    .then(response => {
      setIncomes(response.data)
    })
    .catch(error => {
      console.error('Ocorreu um erro:', error);
    });
  }, [user.id])

  const _expenses = useMemo(() => {
    axios.get(`http://127.0.0.1:5000/expenses/?user_id=${user.id}`)
    .then(response => {
      setExpenses(response.data) 
    })
    .catch(error => {
      console.error('Ocorreu um erro:', error);
    });
  }, [user.id])

  const getTotal = (array) => array?.reduce((acumulador, elemento) => acumulador + elemento.amount, 0)
  const totalIncomomes = getTotal(incomes)
  const totalExpenses = getTotal(expenses)
  const balance = (totalIncomomes - totalExpenses).toLocaleString('pt-BR', { minimumFractionDigits: 2, maximumFractionDigits: 2 })

  return (
    <div class="max-w-xl mx-auto mb-[80px]">
      <button class="flex gap-4 items-center mb-[32px]" onClick={handleClickPerfil}>
        <div class="relative w-14 h-14 overflow-hidden bg-white rounded-full dark:bg-gray-600"></div>
        <div class="text-left">
          <div class="text-white font-black text-bs">Olá, {user.name}</div>
          <div class="text-white font-light text-sm">Bem-vind@ de volta!</div>
        </div>
      </button>
      <h1 class="text-lighterGray font-black text-bs mb-[20px]">Seu balanço</h1>
      <h1 class="text-white font-semibold text-2xl mb-[20px]">R$ {balance}</h1>
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

export default Home;