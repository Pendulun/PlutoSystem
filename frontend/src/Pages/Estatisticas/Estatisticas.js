import React from 'react';

export const Estatisticas = () => {
  const user = JSON.parse(localStorage?.getItem('user'));

  return (
    <div class="text-center mx-auto max-w-[1000px]">
      <div class="text-white font-Inter font-semibold text-xl">Estatisticas</div>
      <div class="mx-auto gap-8 mt-[60px]">
        <div class="">          
         <div class="w-full p-5 bg-white rounded-xl flex items-center justify-center">
            <iframe src={`http://localhost:5000/dash_entries/${user?.id}`} title='plot view' width={1000} height={450}/>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Estatisticas;