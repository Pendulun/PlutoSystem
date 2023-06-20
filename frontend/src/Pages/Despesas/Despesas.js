import React, { useState } from 'react'
import { toast } from 'react-hot-toast'
import { BottomSheet } from 'react-spring-bottom-sheet'
import 'react-spring-bottom-sheet/dist/style.css'
import { AddIcon, BottomSheetContent, ImportButton, Loading } from '../../Components'
import { useMutationAddExpense, useMutationUploadExpenses, useQueryListExpensesTag } from '../../Services/queries'
import { ListItemExpense } from '../Home/Components/ListItem'
import { IconDeletarConta } from '../Perfil/components/Icons/opcoes_estaticas.js'
import { TagButton } from './components/TagButton/TagButton'

export const Despesas = () => {
  const [file, setFile] = useState()
  const [tag, setTag] = useState()
  const [open, setOpen] = useState(false)

  const user = JSON.parse(localStorage?.getItem('user'))

  const { data: { expenses } = [], isLoading, isError, refetch } = useQueryListExpensesTag(user.id, tag)
  const upload = useMutationUploadExpenses(user.id)
  const addExpense = useMutationAddExpense()

  const selectFile = (e) => {
    e.preventDefault()
    setFile(e.target.files[0])
  }

  const handleDelete = (e) => {
    e.preventDefault()
    setFile()
  }

  const handleTagChange = (tag) => {
    setTag(tag)
    setTimeout(refetch, 100)
  }

  function reloadPage() {
    document.location.reload()
  }

  const handleNewExpense = () => {
    const user = JSON.parse(localStorage?.getItem('user'))
    const title = document.getElementById('title').value
    const value = document.getElementById('amount').value
    const tag = document.getElementById('tag').value
  
    const data = {
      "user_id": user.id,
      "src": title,
      "amount": value,
      "tag_name": tag
    }

    addExpense.mutate( data, {
      onSuccess: () => {
        toast.success('Despesa adicionada com sucesso', { duration: 5000})
        setTimeout(reloadPage, 2600)
        setOpen(false)
      },
      onError: (error) => {
        toast.error(error)
      },
    })

  }

  const handleSubmit = (event) => {
    event.preventDefault()
    var modelForm = new FormData()
    modelForm.append('user_id', user.id)
    modelForm.append('file', file)

    upload.mutate(modelForm, {
      onSuccess: () => {
        toast.success('Arquivo recebido com sucesso', { duration: 5000})
        setTimeout(reloadPage, 2600)
        setFile()
      },
      onError: (error) => {
        toast.error(error)
      },
    })
  }

  if (isLoading) return <Loading/>
  if (isError) toast.error('Erro ao carregar informações, por favor atualize a página')

  return (
    <div class="mb-[80px]">
      <div class="flex w-full h-auto justify-between items-center">
        <div class="text-white font-Inter font-semibold text-xl">Despesas</div>
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
          <BottomSheetContent Title='Adicionar despesa' handleSubmit={handleNewExpense} isExpense />
        </BottomSheet>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 mx-auto gap-8 mt-[60px]">
        <div class="w-full p-5 bg-white rounded-xl flex items-center justify-center">
          <iframe data-cy="the-frame" src={`http://localhost:5000/dash_expenses/${user?.id}`} title='plot view' width={1000} height={450}/>
        </div>
        
        {expenses?.length > 0 && (
        <div class="mt-[40px]">
          <div class="flex items-center justify-center">
            <TagButton tagId={1} title='Tudo' onClick={() => handleTagChange('')} />
            <TagButton tagId={2} title='Farmácia' onClick={() => handleTagChange('farmacia')}/>
            <TagButton tagId={3} title='Mercado' onClick={() => handleTagChange('mercado')}/>
          </div>

          <div class="mt-[40px]">
            {expenses?.map((item) => (
              <div class="mt-4 px-5 max-w-lg mx-auto">
                <ListItemExpense title={item?.src} value={item?.amount}/>
                <hr class='text-gray'/>
              </div>
            ))}
          </div>
        </div>
        )}
      </div>
    </div>
  )
}

export default Despesas