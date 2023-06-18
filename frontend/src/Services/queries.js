import axios from 'axios'
import { useMutation, useQuery } from 'react-query'

const BASE_URL = 'http://127.0.0.1:5000'

export const useQueryLogin = () =>
  useQuery(
    'login', (user) =>
      axios
        .get(`${BASE_URL}/users/`, { params: user })
        .then(result => result.data)
        .catch(result => result)
  )

export const useMutationRegister = () =>
  useMutation(
    data =>
      axios
        .post(`${BASE_URL}/users/`, data)
        .then(result => result.data)
        .catch(result => result)
  )

export const useQueryListUsers = () =>
  useQuery(
    'list users', () =>
    axios
        .get(`${BASE_URL}/users/`)
        .then(result => result.data)
        .catch(result => result)
  )

export const useQueryListIncomes = (userId) =>
  useQuery(
    'incomes', () =>
    axios
        .get(`${BASE_URL}/incomes/?user_id=${userId}`)
        .then(result => result.data)
        .catch(result => result)
  )

export const useQueryListExpenses = (userId) =>
  useQuery(
    'expenses', () =>
    axios
        .get(`${BASE_URL}/expenses/?user_id=${userId}`)
        .then(result => result.data)
        .catch(result => result)
  )

export const useQueryListExpensesTag = (userId, tag = '') =>
  useQuery(
    'expenses', () =>
    axios
        .get(`${BASE_URL}/expenses/?user_id=${userId}`, tag ? {params: { tag_name: tag }} : '')
        .then(result => result.data)
        .catch(result => result)
  )

export const useMutationAddIncome = () =>
  useMutation(
    data =>
      axios
        .post(`${BASE_URL}/incomes/`, data)
        .then(result => result.data)
        .catch(result => result)
  )

export const useMutationUploadIncomes = (userId) =>
  useMutation(
    data =>
      axios
        .post(`${BASE_URL}/upload/incomes/?user_id=${userId}`, data)
        .then(result => result.data)
        .catch(result => result)
  )

export const useMutationAddExpense = () =>
  useMutation(
    data =>
      axios
        .post(`${BASE_URL}/expenses/`, data)
        .then(result => result.data)
        .catch(result => result)
  )

export const useMutationUploadExpenses = (userId) =>
  useMutation(
    data =>
      axios
        .post(`${BASE_URL}/upload/expenses/?user_id=${userId}`, data)
        .then(result => result.data)
        .catch(result => result)
  )