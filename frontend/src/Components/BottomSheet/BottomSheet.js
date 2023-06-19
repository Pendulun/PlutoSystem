import React from 'react'

export const BottomSheetContent = ({ Title, handleSubmit, isExpense = false }) => (
  <div class="flex flex-col h-auto w-auto max-w-lg p-[50px] justify-center items-center mx-auto pb-[80px]">
    <div class="text-white font-Inter font-semibold text-[18px] text-center mb-5">{Title}</div>
    <input data-cy="title" id="title" class="w-full h-10 rounded-md outline outline-1 outline-gray4 bg-gray2 placeholder-gray4 pl-5 pr-5 mb-5" type="text" placeholder="Título" />
    <input data-cy="amount" id="amount" class="w-full h-10 rounded-md outline outline-1 outline-gray4 bg-gray2 placeholder-gray4 pl-5 pr-5 mb-5" type="number" placeholder="Valor" />
    {isExpense && <input data-cy="tag" id="tag" class="w-full h-10 rounded-md outline outline-1 outline-gray4 bg-gray2 placeholder-gray4 pl-5 pr-5" type="text" placeholder="Tag" />}
    <button onClick={handleSubmit} class="mt-[40px] w-[218px] h-[40px] bg-darkTeal rounded-lg"><span class="text-white text-sm font-bold">Salvar</span></button>
  </div>
)