import React, { useState, useMemo } from 'react'
import axios from 'axios';
import { ListItemExpense } from '../Home/Components/ListItem'
import { IconDeletarConta } from '../Perfil/components/Icons/opcoes_estaticas.js'
import { useUserContext } from "../../Context/useContextValues.js"

export const Despesas = () => {
  const { user } = useUserContext()
  const [file, setFile] = useState();
  const [expenses, setExpenses] = useState()

  const selectFile = (e) => {
    e.preventDefault()
    setFile(e.target.files[0]);
  }

  const handleDelete = (e) => {
    e.preventDefault()
    setFile()
  }

  const handleSubmit = (event) => {
    event.preventDefault()
    var modelForm = new FormData()
    modelForm.append('user_id', user.id)
    modelForm.append('file', file)

    axios.post('http://localhost:5000/upload/expenses/', modelForm)
    .then(response => {
      window.location.reload(true);
    })
    .catch(error => {
      // Faça algo em caso de erro no cadastro
      console.error('Ocorreu um erro:', error);
    });
  }

  const _expenses = useMemo(() => {
    axios.get(`http://127.0.0.1:5000/expenses/?user_id=${user.id}`)
    .then(response => {
      setExpenses(response.data) 
    })
    .catch(error => {
      console.error('Ocorreu um erro:', error);
    });
  }, [user.id])

  return (
    <>
      <div class="flex w-full h-auto justify-between items-center ">
        <div class="text-white font-Inter font-semibold text-xl">Despesas</div>
        <label for="fileInput" type='button' class="w-24 h-[28px] bg-darkTeal rounded-full text-white text-sm font-Inter inline-flex items-center justify-center">
            {file ? (
                <button onClick={handleSubmit} class="text-sm text-white">Enviar</button>
            ) : (
              <>
                <input onChange={selectFile} id="fileInput" type="file"  accept='.csv' style={{ display: 'none' }} class="ml-[16px] text-sm text-white"/>
                Importar
              </>
            )}
        </label>
      </div>

      {file && (
        <div class="mt-5 flex gap-5 items-center justify-end">
          <div class=" text-white text-right text-sm">{file.name} selecionado</div>
          <button variant="outlined" onClick={(e) => handleDelete(e)}>
            <IconDeletarConta/>
          </button>
        </div>
      )}

      <div class="grid grid-cols-1 md:grid-cols-2 mx-auto gap-8 mt-[60px]">
        <div class="">          
         <div class="w-full p-5 bg-white rounded-xl flex items-center justify-center">
            <iframe src={`http://localhost:5000/dash_expenses/${user?.id}`} title='plot view' width={1000} height={450}/>
          </div>
        </div>
        
        {expenses?.length > 0 && (
        <div class="mt-[40px] overflow-x-scroll mb-[100px]">
          <div class="flex items-center justify-center ">
            <button class="text-gray3 font-semibold font-Inter hover:bg-gray hover:text-lightBlue border-b-2 border-transparent hover:border-lightBlue py-2 px-6 rounded-t-2xl">Tudo</button>
            <button class="text-gray3 font-semibold font-Inter hover:bg-gray hover:text-lightBlue border-b-2 border-transparent hover:border-lightBlue py-2 px-6 rounded-t-2xl">Salário</button>
            <button class="text-gray3 font-semibold font-Inter hover:bg-gray hover:text-lightBlue border-b-2 border-transparent hover:border-lightBlue py-2 px-6 rounded-t-2xl">Investimentos</button>
          </div>
          <div class="mt-[40px]">
            {expenses?.map((item) => (
              <ListItemExpense title={item?.src} value={item?.amount}/>
            ))}
          </div>
        </div>
        )}
      </div>

      {/* <div class="flex w-full h-auto justify-between items-center">
        <button class="mt-[40px] w-[218px] mx-auto h-[40px] bg-darkTeal rounded-lg mb-[120px]" ><span class="text-white text-sm font-bold">Adicionar Despesa</span></button>
      </div> */}
    </>
  )
}

export default Despesas;