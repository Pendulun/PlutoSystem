describe('Teste de filtragem de despesas', () => {
  beforeEach(() => {
    cy.viewport('iphone-xr', 'portrait')
    cy.visit('/')
    cy.get('[data-cy="email"]').type('leticia@email.com')
    cy.get('[data-cy="password"]').type('123')
    cy.get('[data-cy="submit"]').click()
    cy.url().should('include', '/home')
    cy.get('[href="/despesas"]').click()
    cy.url().should('include', '/despesas')

    cy.wait(3000)

    cy.get('.w-24').selectFile('cypress/fixtures/teste.csv')
    cy.get('.w-24').contains('Enviar').click()
  })

  it('Deve exibir tanto o item chocolate quanto o antialergico após clicar no botão Tudo', function () {
    cy.wait(5000)
    cy.contains('Tudo')
    // Clicar no botão Tudo
    .click()
    cy.wait(5000)
    .then(() => {
      // Verificar se o item chocolate está visível
      cy.contains('chocolate').should('be.visible')
      // Verificar se o item antialergico está visível
      cy.contains('antialergico').should('be.visible')
    })  
  })

  it('Deve exibir apenas o item chocolate após clicar no botão Mercado', function () {
    cy.wait(5000)
    cy.contains('Mercado')
    // Clicar no botão Mercado
    .click()
    cy.wait(5000)
    .then(() => {
      // Verificar se o item chocolate está visível
      cy.contains('chocolate').should('be.visible')
      // Verificar se outros itens (no caso antialergico) não estão visíveis
      cy.contains('antialergico').should('not.exist')
    })  
  })

  it('Deve exibir apenas o item antialergico após clicar no botão Farmácia', function () {
    cy.wait(5000)
    cy.contains('Farmácia')
    // Clicar no botão Farmácia
    .click()
    cy.wait(5000)
    .then(() => {
      // Verificar se o item chocolate está visível
      cy.contains('antialergico').should('be.visible')
      // Verificar se outros itens (no caso chocolate) não estão visíveis
      cy.contains('chocolate').should('not.exist')
    })  
  })
})