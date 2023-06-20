describe('Registration', () => {
  beforeEach(() => {
    cy.viewport('iphone-xr', 'portrait')
  })

  it('Register new user', () => {
    cy.visit('/cadastro')
    cy.get('[data-cy="name"]').type('Prática em Desenvolvimento')
    cy.get('[data-cy="email"]').type('pds@gg.com')
    cy.get('[data-cy="password"]').type('c@mpt4caO')
    cy.get('[data-cy="submit"]').click()
    cy.get('.go2072408551').as('successToast').should('be.visible')
    cy.get('@successToast').should('contain', 'Cadastro realizado com sucesso!')
  })

  it('New user should login', function () {
    cy.visit('/')
    cy.get('[data-cy="email"]').type('pds@gg.com')
    cy.get('[data-cy="password"]').type('c@mpt4caO')
    cy.get('[data-cy="submit"]').click()
    cy.url().should('include', '/home')
    cy.get('[data-cy="profile-picture"]').click()
    cy.url().should('include', '/perfil')
    cy.get('[data-cy="name"]').should('contain', 'Prática em Desenvolvimento')
    cy.get('[data-cy="email"]').should('contain', 'pds@gg.com')
  })
})