import React from 'react'

export const ListItemIncome = ({ title, value }) => (
  <div class="flex justify-between items-center mb-4">
    <h1 class="text-lighterGray font-medium text-bs">{title}</h1>
    <h2 class="text-lighterGray font-medium text-bs">+ R$ {value}</h2>
  </div>
)

export const ListItemExpense = ({ title, value }) => (
  <div class="flex justify-between items-center mb-4">
    <h1 class="text-lighterGray font-medium text-bs">{title}</h1>
    <h2 class="text-lighterGray font-medium text-bs">- R$ {value}</h2>
  </div>
)
