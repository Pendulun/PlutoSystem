import React from 'react'

export const AccountButton = ({ title, icon }) => {
  return (
    <div class="flex mb-[16px]">
      {icon}
      <div class="ml-4">
        <p class="text-white font-Inter font-normal">{title}</p>
      </div>
    </div>
  )
}