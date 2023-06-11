import { useMemo, useState } from "react"
import { toast } from 'react-hot-toast'
import { ImportButton, Loading } from '../../Components'
import { useData } from '../../Hooks/useData'
import { useMutationUploadIncomes, useQueryListIncomes } from "../../Services/queries"
import { ListItemIncome } from "../Home/Components/ListItem.js"
import { IconDeletarConta } from '../Perfil/components/Icons/opcoes_estaticas.js'

export const Rendas = () => {
  const { getArrTotal } = useData()
  const [file, setFile] = useState()

  const user = JSON.parse(localStorage?.getItem('user'))
  const { data: incomes = [], isLoading, isError } = useQueryListIncomes(user.id)

  const upload = useMutationUploadIncomes(user.id)

  const selectFile = (e) => {
    e.preventDefault()
    setFile(e.target.files[0])
  }

  const handleDelete = (e) => {
    e.preventDefault()
    setFile()
  }

  function reloadPage() {
    document.location.reload()
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    var modelForm = new FormData()
    modelForm.append('user_id', user.id)
    modelForm.append('file', file)

    upload.mutate(modelForm, {
      onSuccess: () => {
        toast.success('Arquivo recebido com sucesso', { duration: 4000 })
        setTimeout(reloadPage, 2600)
        setFile()
      },
      onError: (error) => {
        toast.error(error)
      },
    })
  }

  const totalIncomes = useMemo(() => getArrTotal(incomes), [incomes, getArrTotal])

  if (isLoading) return <Loading/>
  if (isError) toast.error('Erro ao carregar informações, por favor atualize a página')

  return (
    <div class="mb-[80px]">
      <div class="flex w-full h-auto justify-between items-center ">
        <div class="text-white font-Inter font-semibold text-xl">Rendas</div>
        <ImportButton file={file} handleSubmit={handleSubmit} selectFile={selectFile}/>
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

        <div class="mt-[40px] mx-5">
          <h1 class="text-lighterGray font-black text-bs mb-[10px] mt-[40px] text-center">Histórico</h1>
          <hr class="text-lightGray mb-[25px]"/>
          {incomes?.map((item) => (
            <ListItemIncome title={item?.src} value={item?.amount}/>
          ))}
          <hr class="text-lightGray mb-[25px] border-dashed"/>
          <ListItemIncome title={'Total'} value={totalIncomes}/>
        </div>
      </div>
    </div>
  )
}

export default Rendas