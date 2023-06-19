describe('Testando adicionar uma renda diretamente', () => {
  it('Adicionar uma renda de forma direta', function () {
    cy.visit('/')
    cy.get('[data-cy="email"]').type('leticia@email.com')
    cy.get('[data-cy="password"]').type('123')
    cy.get('[data-cy="submit"]').click()
    cy.url().should('include', '/home')

    cy.get('[href="/rendas"]').click()
    cy.url().should('include', '/rendas')
    cy.get('button.ml-5').should('be.visible').click()

    cy.get('[data-cy="title"]').type('Renda extra')
    cy.get('[data-cy="amount"]').type('1000')
  
    cy.contains('Salvar')
    .click()

    cy.wait(5000)

    cy.contains('Renda extra').should('be.visible')
    cy.contains('+ R$ 1000').should('be.visible')
  })
})