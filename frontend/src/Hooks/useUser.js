import { useCallback, useState } from 'react'

export const useUser = () => {
    const [user, setUser] = useState({})

    const clearUserData = useCallback(() => {
        localStorage.clear()
        setUser()
    }, [])

    return { user, setUser, clearUserData }
}