import { useMemo, useState } from "react"
import { toast } from 'react-hot-toast'
import { BottomSheet } from 'react-spring-bottom-sheet'
import 'react-spring-bottom-sheet/dist/style.css'
import { AddIcon, BottomSheetContent, ImportButton, Loading } from '../../Components'
import { useData } from '../../Hooks/useData'
import { useMutationAddIncome, useMutationUploadIncomes, useQueryListIncomes } from "../../Services/queries"
import { ListItemIncome } from "../Home/Components/ListItem.js"
import { IconDeletarConta } from '../Perfil/components/Icons/opcoes_estaticas.js'

export const Rendas = () => {
  const { getArrTotal } = useData()
  const [file, setFile] = useState()
  const [open, setOpen] = useState(false)

  const user = JSON.parse(localStorage?.getItem('user'))
  const { data: incomes = [], isLoading, isError } = useQueryListIncomes(user.id)

  const upload = useMutationUploadIncomes(user.id)
  const addIncome = useMutationAddIncome()

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

  const handleNewIncome = () => {
    const user = JSON.parse(localStorage?.getItem('user'))
    const title = document.getElementById('title').value
    const value = document.getElementById('amount').value
  
    const data = {
      "user_id": user.id,
      "src": title,
      "amount": value
    }

    addIncome.mutate( data, {
      onSuccess: () => {
        toast.success('Renda adicionada com sucesso', { duration: 5000})
        setTimeout(reloadPage, 2600)
        setOpen(false)
      },
      onError: (error) => {
        toast.error(error)
      },
    })

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
        <div class="flex my-auto justify-between items-center">
          <ImportButton file={file} handleSubmit={handleSubmit} selectFile={selectFile}/>
          <button class="ml-5" variant="outlined" onClick={() => setOpen(true)}>
              <AddIcon />
          </button>
        </div>
      </div>

      {file && (
        <div class="mt-5 flex gap-5 items-center justify-end">
          <div class=" text-white text-right text-sm">{file.name} selecionado</div>
          <button variant="outlined" onClick={(e) => handleDelete(e)}>
            <IconDeletarConta/>
          </button>
        </div>
      )}

      <div>
        <BottomSheet open={open} onDismiss={() => setOpen(false)} class="block fixed inset-x-0 bottom-0 z-10">
          <BottomSheetContent Title='Adicionar renda' handleSubmit={handleNewIncome} />
        </BottomSheet>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 mx-auto gap-8 mt-[60px] content-center items-center justify-center">
        <div class="">          
          <div class="w-full p-5 bg-white rounded-xl flex items-center justify-center">
            <iframe data-cy="the-frame" src={`http://localhost:5000/dash_incomes/${user?.id}`} title='plot view' width={1000} height={450}/>
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