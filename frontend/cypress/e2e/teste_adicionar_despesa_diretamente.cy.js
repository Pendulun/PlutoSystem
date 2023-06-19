describe('Testando adicionar uma despesa diretamente', () => {
  it('Adicionar uma despesa de forma direta', function () {
    cy.visit('/')
    cy.get('[data-cy="email"]').type('leticia@email.com')
    cy.get('[data-cy="password"]').type('123')
    cy.get('[data-cy="submit"]').click()
    cy.url().should('include', '/home')

    cy.get('[href="/despesas"]').click()
    cy.url().should('include', '/despesas')
    cy.get('button.ml-5').should('be.visible').click()

    cy.get('[data-cy="title"]').type('Brinquedo para gatos')
    cy.get('[data-cy="amount"]').type('15')
    cy.get('[data-cy="tag"]').type('Gatos')
  
    cy.contains('Salvar')
    .click()

    cy.wait(5000)

    cy.contains('Brinquedo para gatos').should('be.visible')
    cy.contains('- R$ 15').should('be.visible')
  })
})