import { useMemo } from 'react'
import { Context } from './context'

export const AppProvider = ({ children }) => {

	const contextValues = useMemo(
		() => ({}), [])

	return <Context.Provider value={contextValues}>{ children }</Context.Provider>
}