describe('CSV Upload', () => {
  beforeEach(() => {
    cy.viewport('iphone-xr', 'portrait')
    cy.visit('/')
    cy.get('[data-cy="email"]').type('dan@gg.com')
    cy.get('[data-cy="submit"]').click()
    cy.url().should('include', '/home')
  })

  it('Incomes Upload', function () {
    cy.get('[href="/rendas"]').click()
    cy.url().should('include', '/rendas')

    cy.window().then(w => w.beforeReload = true)
    cy.window().should('have.prop', 'beforeReload', true)

    cy.get('.w-24').selectFile('cypress/fixtures/teste.csv')
    cy.get('.w-24').contains('Enviar').click()
    cy.get('.go2072408551').as('successToast').should('be.visible')
    cy.get('@successToast').should('contain', 'Arquivo recebido com sucesso')

    cy.wait(5000)
    cy.window().should('not.have.prop', 'beforeReload')
  })

  it('Expenses Upload', function () {
    cy.get('[href="/despesas"]').click()
    cy.url().should('include', '/despesas')

    cy.window().then(w => w.beforeReload = true)
    cy.window().should('have.prop', 'beforeReload', true)

    cy.get('.w-24').selectFile('cypress/fixtures/teste.csv')
    cy.get('.w-24').contains('Enviar').click()
    cy.get('.go2072408551').as('successToast').should('be.visible')
    cy.get('@successToast').should('contain', 'Arquivo recebido com sucesso')

    cy.wait(5000)
    cy.window().should('not.have.prop', 'beforeReload')
  })
})