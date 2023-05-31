import { useMemo, useEffect } from 'react'
import { Context } from './context'
import { useUser } from '../Hooks'

export const AppProvider = ({ children }) => {
	const user = useUser()

	useEffect(() => {
    const hasUser = JSON.parse(localStorage?.getItem('user'))
		if (hasUser) user.setUser(hasUser)
	}, [])

	const contextValues = useMemo(
		() => ({ user }), [user])

	return <Context.Provider value={contextValues}>{ children }</Context.Provider>
}