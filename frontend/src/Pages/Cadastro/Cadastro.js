import React from 'react'
import { default as useUser } from '../../Hooks/useUser'
import { useForm } from 'react-hook-form'

export const Cadastro = () => {

  const { postUser } = useUser()

  // Form hooks
  const {
    register,
    handleSubmit
  } = useForm({
    defaultValues: {
      name: '',
      email: '',
      password: '',
    },
    mode: 'onChange',
  })
  const onSubmit = async registerFormData => {
    console.log(`Requesting registration with '${Object.values(registerFormData)}'`)
    postUser(registerFormData).then(res => console.log("resp:", res))
  }


  const handleClickLogin = () => {
    //Navegar para a tela de Login
    const cadastroUrl = '/';
    window.location.href = cadastroUrl;
  }

  return (
    <div className="flex flex-col justify-center items-center h-screen">
      <h1 className="text-white font-Inter font-bold text-2xl">Bem-vindo!</h1>
      <h2 className="text-gray3 font-Inter font-normal text-sm14 mb-[48px]">Entre no PlutoSystem!</h2>
      <form
        id="register-form"
        style={{
          all: 'inherit'
        }}
        onSubmit={handleSubmit(onSubmit)}
      >
        <input className="w-64 h-10 rounded-t-lg outline outline-1 outline-gray4 bg-gray2 placeholder-gray4 pl-5 pr-5" type="text" {...register("name")} placeholder="Nome"></input>
        <input className="w-64 h-10 outline outline-1 outline-gray4 bg-gray2 placeholder-gray4 pl-5 pr-5" type="text" {...register("email")} placeholder="Email"></input>
        <input className="mb-4 w-64 h-10 rounded-b-lg outline outline-1 outline-gray4 bg-gray2 placeholder-gray4 pl-5 pr-5" type="text" {...register("password")} placeholder="Senha"></input>
        <button className="mb-4 w-56 h-10 bg-darkTeal rounded-lg" type="submit"><span className="text-white text-sm font-bold">Cadastrar</span></button>
      </form>
      <div className="border border-gray5 h-0 w-64"></div>
      <div className="mt-2 whitespace-no-wrap flex-col">
        <p className="text-xs flex-shrink">
          <span className="text-white font-Inter text-sm font-normal">Já tem uma conta? </span>
          <button className="text-teal-400 font-Inter text-sm font-normal text-lightBlue" onClick={handleClickLogin}>Entre</button>
        </p>
      </div>
    </div>
  )

}

export default Cadastro;
