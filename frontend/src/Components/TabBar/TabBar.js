import React from 'react'
import { IconHome, IconRendas, IconDespesas, IconEstatisticas } from './Icons';
import { TabBarButton } from './TabBarButton';

export const TabBar = () => {

  return (
    <>
      <div class="block fixed inset-x-0 bottom-0 z-10 h-[85px] bg-gray text-primaryLight drop-shadow-lg px-5 pt-5 rounded-t-lg">
        <div id="tabs" class="flex max-w-lg mx-auto justify-between items-center">
          <TabBarButton PageLink='/home' Icon={<IconHome />} Title='Início'/>
          <TabBarButton PageLink='/rendas' Icon={<IconRendas/>} Title='Rendas'/>
          <TabBarButton PageLink='/despesas' Icon={<IconDespesas />} Title='Despesas'/>
          <TabBarButton PageLink='/estatisticas' Icon={<IconEstatisticas />} Title='Estatísticas'/>
        </div>
      </div>
    </>
	)
}