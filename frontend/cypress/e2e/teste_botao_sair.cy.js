describe('Testando se o botão de sair do perfil leva novamente à tela de login', () => {
  it('Fazer login e sair de um perfil', function () {
    cy.visit('/')
    cy.get('[data-cy="email"]').type('leticia@email.com')
    cy.get('[data-cy="password"]').type('123')
    cy.get('[data-cy="submit"]').click()
    cy.url().should('include', '/home')
    cy.get('[data-cy="profile-picture"]').click()
    cy.url().should('include', '/perfil')
    cy.get('[data-cy="name"]').should('contain', 'Leticia Alves')
    cy.get('[data-cy="email"]').should('contain', 'leticia@email.com')

    // Verificar se o botão de sair existe e clicar nele
    cy.get('button').then(($button) => {
      if ($button.length) {
        cy.wrap($button).click()
        cy.url().should('include', '/')
        cy.contains('Entre no PlutoSystem!').should('be.visible')
      }
    })
  })
})