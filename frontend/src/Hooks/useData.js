export const useData = () => {
  const getArrTotal = (data) => Array.isArray(data) ? data?.reduce((acumulador, elemento) => acumulador + elemento.amount, 0) : 0
  const getBalance = (incomes, expenses) => (
    getArrTotal(incomes) - getArrTotal(expenses))
    .toLocaleString('pt-BR', { minimumFractionDigits: 2, maximumFractionDigits: 2 }
  )

  return { getArrTotal, getBalance }
}