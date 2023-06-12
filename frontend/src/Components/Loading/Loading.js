import React from 'react'
import { PuffLoader } from 'react-spinners'

export const Loading = () => (
  <div className='flex w-full h-[500px] items-center justify-center '>
    <PuffLoader color='white'/>
  </div>
)
