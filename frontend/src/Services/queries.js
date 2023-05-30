import axios from 'axios'
import { useQuery, useMutation } from 'react-query'

const BASE_URL = 'http://127.0.0.1:5000'

export const useQueryListUsers = () =>
  useQuery(
    'list users', () =>
    axios
        .get(`${BASE_URL}/users/`)
        .then(result => result.data)
        .catch(result => result)
  )