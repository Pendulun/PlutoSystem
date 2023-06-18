import React, { useState } from 'react'
import { toast } from 'react-hot-toast'
import { ImportButton, Loading } from '../../Components'
import { useMutationUploadExpenses, useQueryListExpensesTag } from '../../Services/queries'
import { ListItemExpense } from '../Home/Components/ListItem'
import { IconDeletarConta } from '../Perfil/components/Icons/opcoes_estaticas.js'
import { TagButton } from './components/TagButton/TagButton'

export const Despesas = () => {
  const [file, setFile] = useState()
  const [tag, setTag] = useState()

  const user = JSON.parse(localStorage?.getItem('user'))

  const { data: { expenses } = [], isLoading, isError, refetch } = useQueryListExpensesTag(user.id, tag)
  const upload = useMutationUploadExpenses(user.id)

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

      <div class="grid grid-cols-1 md:grid-cols-2 mx-auto gap-8 mt-[60px]">
        <div class="w-full p-5 bg-white rounded-xl flex items-center justify-center">
          <iframe src={`http://localhost:5000/dash_expenses/${user?.id}`} title='plot view' width={1000} height={450}/>
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
              <ListItemExpense title={item?.src} value={item?.amount}/>
            ))}
          </div>
        </div>
        )}
      </div>
    </div>
  )
}

export default Despesas