import { default as ExpressClient } from '../Client/Express'

const useUser = () => {
	const expressClient = new ExpressClient()

	const postUser = async userData => {
		try {
			return await expressClient.postUser(userData).then(res => res)
		} catch (e) {
			console.error("Error when posting user")
		}
	}

	return {
		postUser,
	}
}

export default useUser
