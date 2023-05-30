import React, { useState } from 'react';

import { Grafico, Trofeu } from './components/figuras.js';

export const Home = () => {
  
  const [fileInputVisible, setFileInputVisible] = useState(false);

  const showFileInput = () => {
    setFileInputVisible(!fileInputVisible);
  };

  return (
    <>
      <div class="flex">
        <div class="w-1/2">
          <div class="flex gap-4 items-center mb-[32px]">
            <div class="flex justify-start w-50 h-30">
              <div class="text-white font-Inter font-semibold text-xl mr-[102px]">Despesas</div>
              <div class="relative flex">
              <button class="w-24 h-6 bg-darkTeal rounded-full mr-[16px]"><span class="text-white text-sm font-Inter font-bold">Exportar</span></button>
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
          </div>
          <div class="flex">
            <button class="text-gray3 font-semibold font-Inter hover:bg-gray hover:text-lightBlue border-b-2 border-transparent hover:border-lightBlue py-2 px-6 rounded-t-2xl">Tudo</button>
            <button class="text-gray3 font-semibold font-Inter hover:bg-gray hover:text-lightBlue border-b-2 border-transparent hover:border-lightBlue py-2 px-6 rounded-t-2xl">Alimentação</button>
            <button class="text-gray3 font-semibold font-Inter hover:bg-gray hover:text-lightBlue border-b-2 border-transparent hover:border-lightBlue py-2 px-6 rounded-t-2xl">Casa</button>
            <button class="text-gray3 font-semibold font-Inter hover:bg-gray hover:text-lightBlue border-b-2 border-transparent hover:border-lightBlue py-2 px-6 rounded-t-2xl">Outros</button>
          </div>
          <hr class="w-[416px] text-lightGray mb-[20px]"/>
        </div>
        <div class="w-1/2">          
          <div class="w-[500px] h-[300px] bg-gray rounded-xl flex items-center justify-center mt-[64px]">
            <Grafico/>
          </div>
          <div class="mt-4 w-[500px] h-[100px] bg-gray rounded-xl flex items-center mb-[24px]">
            <div class="flex justify-start ml-[32px]">
              <Trofeu/>
              <p class="ml-[24px] text-white font-black font-Inter">Conquista<p class="font-normal text-xs">Lorem ipsum dolor sit amet consectetur.</p></p>
            </div>
          </div>
        </div>
      </div>
    </>
  )

}

export default Home;