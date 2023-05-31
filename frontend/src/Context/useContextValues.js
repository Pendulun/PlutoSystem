import { useContext } from 'react'
import { Context } from './context'

export const useContextValue = () => useContext(Context)

export const useUserContext = () => {
    const context = useContextValue()
    return context.user
}
