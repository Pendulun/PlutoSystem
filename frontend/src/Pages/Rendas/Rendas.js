import React, { useState } from 'react';

import { Grafico, Trofeu } from './components/figuras.js';

export const Rendas = () => {
  
  const [fileInputVisible, setFileInputVisible] = useState(false);

  const showFileInput = () => {
    setFileInputVisible(!fileInputVisible);
  };

  return (
    <>
      <div class="flex w-full h-auto justify-between items-center mb-[80px]">
        <div class="text-white font-Inter font-semibold text-xl">Rendas</div>
        <div class="relative flex">
          <button onClick={showFileInput} class="w-24 h-6 bg-darkTeal rounded-full">
            <span class="text-white text-sm font-Inter font-bold">Importar</span>
          </button>
          {fileInputVisible && (
            <div>
              <form>
                <input type='hidden' value="0"/>
                <div class="relative flex">
                  <input id="fileInput" type="file" class="ml-[16px] text-sm text-white"/>
                  <button class="text-xs ml-2 px-2 py-1 bg-white rounded-full text-black font-Inter font-bold">Enviar</button>
                </div>
              </form>
            </div>
          )}
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 mx-auto gap-8">
        <div class="">          
         <div class="w-full mx-auto h-[300px] bg-gray rounded-xl flex items-center justify-center">
            <Grafico/>
          </div>
          <div class="mt-4 w-full h-[100px] bg-gray rounded-xl flex items-center mb-[24px]">
            <div class="flex justify-start ml-[32px]">
              <Trofeu/>
              <p class="ml-[24px] text-white font-black font-Inter">Conquista<p class="font-normal text-xs">Lorem ipsum dolor sit amet consectetur.</p></p>
            </div>
          </div>
        </div>

        <div class="mx-auto overflow-x-scroll">
          <div class="flex items-center ">
            <button class="text-gray3 font-semibold font-Inter hover:bg-gray hover:text-lightBlue border-b-2 border-transparent hover:border-lightBlue py-2 px-6 rounded-t-2xl">Tudo</button>
            <button class="text-gray3 font-semibold font-Inter hover:bg-gray hover:text-lightBlue border-b-2 border-transparent hover:border-lightBlue py-2 px-6 rounded-t-2xl">Salário</button>
            <button class="text-gray3 font-semibold font-Inter hover:bg-gray hover:text-lightBlue border-b-2 border-transparent hover:border-lightBlue py-2 px-6 rounded-t-2xl">Investimentos</button>
          </div>
        </div>
      </div>
    </>
  )
}

export default Rendas;