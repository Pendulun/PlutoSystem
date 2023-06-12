import React from 'react'

export const ImportButton = ({ file, handleSubmit, selectFile }) => (
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
)
