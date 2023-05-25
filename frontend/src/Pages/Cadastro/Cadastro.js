import React from 'react'

import classes from './LoginPreenchido.module.css';

class Cadastro extends React.Component{
  handleClickLogin = () => {
    // Navegar para a tela de cadastro
    const cadastroUrl = '/login'; // Defina a URL da tela de cadastro
    window.location.href = cadastroUrl;
  }

  render(){
    return (
      <div className={classes.alinhamento}>
        <div className={classes.bemVindo}>Bem-vindo!</div>
        <div className={classes.entreNoPlutoSystem}>Cadastre-se no PlutoSystem!</div>
        <input class={classes.ret_input_nome} type="text" placeholder=" Nome"></input>
        <input class={classes.ret_input_email} type="text" placeholder=" Email"></input>
        <input class={classes.ret_input_senha} type="text" placeholder=" Senha"></input>
        <button class={classes.ret_botao_entrar}><span class={classes.estilo_botao_entrar}>Cadastrar</span></button>
        <div className={classes.linha_divisao}></div>
        <div className={classes.texto_cadatrar}>
          <p className={classes.labelWrapper}>
            <span className={classes.label}>Já tem uma conta? </span>
            <button class={classes.label2} onClick={this.handleClickLogin}>Entre</button>
          </p>
        </div>
      </div>
    )
  }
}

export default Cadastro;