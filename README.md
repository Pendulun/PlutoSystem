# PlutoSystem

## Sobre o sistema
O PlutoSystem é um sistema de gerenciamento de finanças pessoais. Nesse sistema, o usuário poderá cadastrar despesas e ganhos, atribuir categorias, estabelecer metas e orçamento, visualizar a situação por meio de gráficos e, caso queira, compartilhar o gerenciamento de parte ou todo de suas despesas com outras pessoas como companheiro/a, familiares ou outros.

## Membros e papéis

- Alexander: Backend
- Daniel: Backend
- Ilana: Fullstack
- Letícia: Fullstack

## Tecnologias

1. Linguagem de programação backend: Python
2. Framework de desenvolvimento Web Python: Flask com Dash para gráficos interativos
3. Banco de Dados: postgresql
4. Framework para desenvolvimento frontend: React

## Backlog do Produto

1. Eu, como usuário, gostaria de adicionar despesas e receitas
2. Eu, como usuário, gostaria de agrupar gastos por categorias ou tags
3. Eu, como usuário, gostaria de adicionar fontes de renda
4. Eu, como usuário, gostaria de definir metas de gastos e orçamentos
5. Eu, como usuário, gostaria de ver estatísticas básicas sobre os meus gastos
6. Eu, como usuário, gostaria de definir gastos ou despesas recorrentes mensais
7. Eu, como usuário, gostaria de ver gráficos interativos sobre os meus gastos
8. Eu, como usuário, gostaria de poder compartilhar uma visualização do meu estado financeiro
9. Eu, como quem recebeu compartilhado a visualização das finanças de outra pessoa, gostaria de ver gráficos e estatísticas apropriados sobre o estado financeiro dela
10. Eu, como usuário, gostaria de ter uma previsão sobre os meus gastos no próximo mês
11. Eu, como usuário, gostaria de associar minhas contas em bancos
12. Eu, como usuário, gostaria de me cadastrar e ter um perfil
13. Eu, como usuário, gostaria de importar meus gastos e receitas por meio de um arquivo csv
14. Eu, como usuário, gostaria de exportar meus gastos e receitas por meio de um arquivo csv
15. Eu, como usuário, gostaria de criar um grupo em que vários usuários poderiam adicionar despesas e gastos contidos no próprio grupo
16. Eu, como usuário, gostaria de poder replicar um gasto ou receita adicionado em um grupo na minha parte financeira pessoal

## Backlog da Sprint

1. Eu, como usuário, gostaria de adicionar despesas e receitas
    - Criar banco de dados e tabelas necessárias **(Alex)**
    - Criar rota para recuperação de despesas e receitas usando o Flask **(Alex)**
    - Criar versão inicial da tela inicial (Tela 'A' com menor granularidade) **(Lana)**
    - Criar rota para cadastro de despesas com o Flask **(Daniel)**
    - Criar rota para cadastro de receitas com o Flask **(Daniel)**
    - Adaptar tela inicial (Tela 'A') para poder adicionar despesas e receitas **(Lana)**
2. Eu, como usuário, gostaria de agrupar gastos por categorias ou tags
    - Adicionar opções de adicionar/remover/alterar tags na tela inicial (Tela 'A') **(Letícia)**
    - Criar qualquer tabela necessária para as tags no banco de dados **(Daniel)**
    - Criar rotas para adicionar/remover/alterar tags de um gasto com o Flask **(Letícia)**
    - Adaptar tela com visualização de gastos (Tela 'A') para poder filtrar gastos por tags **(Lana)**
    - Criar rota de recuperação de gastos do usuário filtrando por tag com o Flask **(Alex)**
3. Eu, como usuário, gostaria de ver estatísticas básicas sobre os meus gastos
    - Criar versão inicial tela de visualização de informações dos gastos (Tela 'B' com maior granularidade) **(Letícia)**
    - Criar lógica que computa as estatísticas sobre os gastos **(Alex)**
    - Criar rota que retorna algumas estatísticas sobre os gastos com o Flask **(Letícia)**
4. Eu, como usuário, gostaria de ver gráficos interativos sobre os meus gastos
    - Adaptar tela de visualização de informações dos gastos (Tela 'B') para poder receber alguns gráficos **(Lana)**
    - Criar lógica que gera os gráficos interativos usando o Dash **(Daniel)**
    - Criar rota que retorne os gráficos interativos **(Daniel)**
5. Eu, como usuário, gostaria de me cadastrar e ter um perfil
    - Criar tela de cadastro de usuário **(Letícia)**
    - Criar tabelas necessárias no banco de dados **(Alex)**
    - Criar rota de cadastro de usuário **(Alex)**
    - Criar rota que retorne as informações do usuário **(Lana)**
    - Criar versão inicial da tela de perfil de usuário com algumas informações básicas **(Letícia)**
6. Eu, como usuário, gostaria de importar meus gastos e receitas por meio de um arquivo csv
    - Alterar a tela inicial de visualização de gastos e receitas (Tela 'A') para poder importar por arquivo **(Lana)**
    - Criar lógica de processamento de arquivo de receitas **(Daniel)**
    - Criar rota que recebe arquivo de receita e o processa **(Daniel)**
    - Criar lógica de preocessamento de arquivo de despesas **(Alex)**
    - Criar rota que recebe arquivo de despesa e o processa **(Alex)**
