import { useState, useMemo } from "react"
import axios from 'axios'
import { ListItemIncome } from "../Home/Components/ListItem.js"
import { IconDeletarConta } from '../Perfil/components/Icons/opcoes_estaticas.js'
import { useUserContext } from "../../Context/useContextValues.js"

export const Rendas = () => {
  const { user } = useUserContext()
  const [file, setFile] = useState()
  const [incomes, setIncomes] = useState()


  const selectFile = (e) => {
    e.preventDefault()
    setFile(e.target.files[0])
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

    axios.post(`http://127.0.0.1:5000/upload/incomes/?user_id=${user.id}`, modelForm)
    .then(response => {
      window.location.reload(true);
    })
    .catch(error => {
      // Faça algo em caso de erro no cadastro
      console.error('Ocorreu um erro:', error);
    });
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

  const getTotal = (array) => array?.reduce((acumulador, elemento) => acumulador + elemento.amount, 0)
  const totalIncomes = getTotal(incomes)

  return (
    <>
      <div class="flex w-full h-auto justify-between items-center ">
        <div class="text-white font-Inter font-semibold text-xl">Rendas</div>
        <label for="fileInput" type='button' class="w-24 h-[28px] bg-darkTeal rounded-full text-white text-sm font-Inter inline-flex items-center justify-center">
            {file ? (
                <button class="text-sm text-white" onClick={handleSubmit}>Enviar</button>
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

      <div class="grid grid-cols-1 md:grid-cols-2 mx-auto gap-8 mt-[60px] content-center items-center justify-center">
        <div class="">          
          <div class="w-full p-5 bg-white rounded-xl flex items-center justify-center">
            <iframe src={`http://localhost:5000/dash_incomes/${user?.id}`} title='plot view' width={1000} height={450}/>
          </div>
        </div>

        <div class="mt-[40px] mx-5 mb-[90px]">
          <h1 class="text-lighterGray font-black text-bs mb-[10px] mt-[40px] text-center">Histórico</h1>
          <hr class="text-lightGray mb-[25px]"/>
          {incomes?.map((item) => (
            <ListItemIncome title={item?.src} value={item?.amount}/>
          ))}
          <hr class="text-lightGray mb-[25px] border-dashed"/>
          <ListItemIncome title={'Total'} value={totalIncomes}/>
        </div>
      </div>
    </>
  )
}

export default Rendas;