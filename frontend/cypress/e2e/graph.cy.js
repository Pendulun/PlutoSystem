const currentDate = new Date()
currentDate.setMonth(currentDate.getMonth() - 1)
const lastMonth = `${currentDate.getMonth() + 1}/${currentDate.getFullYear()}`

const getIframeBody = () => {
  return cy
  .get('iframe[data-cy="the-frame"]')
  .its('0.contentDocument.body').should('not.be.empty')
  .then(cy.wrap)
}

describe('Graph', () => {
  beforeEach(() => {
    cy.viewport('iphone-xr', 'portrait')
    cy.visit('/')
    cy.get('[data-cy="email"]').type('dan@gg.com')
    cy.get('[data-cy="submit"]').click()
    cy.url().should('include', '/home')
  })

  it('Incomes graph', () => {
    cy.visit('/rendas')
    cy.get('iframe').should('be.visible')
    getIframeBody().find('.gtitle').should('have.text', 'Receitas nos últimos doze meses')
    getIframeBody().find('.ytitle').should('have.text', 'Total')
    getIframeBody().find('.xtitle').should('have.text', 'Data')
    getIframeBody().find('g.trace.bars').find('g.point').should('have.length', 12)
    getIframeBody().find('g.xaxislayer-above').find('g.xtick').should('have.length', 6)
    getIframeBody().find('g.xaxislayer-above').find('g.xtick:eq(5)').should('have.text', lastMonth)
    getIframeBody().find('div.modebar-group:eq(0)').find('a.modebar-btn')
     .invoke('attr', 'data-title')
     .should('eq', 'Download plot as a png')
    getIframeBody().find('div.modebar-group:eq(0)').find('a.modebar-btn').click()
    cy.readFile('cypress/downloads/newplot.png').should('exist')
  })

  it('Expenses graph', () => {
    cy.visit('/despesas')
    cy.get('iframe').should('be.visible')
    getIframeBody().find('.gtitle').should('have.text', 'Gastos nos últimos doze meses')
    getIframeBody().find('.ytitle').should('have.text', 'Total')
    getIframeBody().find('.xtitle').should('have.text', 'Data')
    getIframeBody().find('g.trace.bars').find('g.point').should('have.length', 12)
    getIframeBody().find('g.xaxislayer-above').find('g.xtick').should('have.length', 6)
    getIframeBody().find('g.xaxislayer-above').find('g.xtick:eq(5)').should('have.text', lastMonth)
    getIframeBody().find('div.modebar-group:eq(0)').find('a.modebar-btn')
     .invoke('attr', 'data-title')
     .should('eq', 'Download plot as a png')
    getIframeBody().find('div.modebar-group:eq(0)').find('a.modebar-btn').click()
    cy.readFile('cypress/downloads/newplot.png').should('exist')
  })

  it('Stats graph', () => {
    cy.visit('/estatisticas')
    cy.get('iframe').should('be.visible')
    getIframeBody().find('.gtitle').should('have.text', 'Gastos e Receitas nos últimos doze meses')
    getIframeBody().find('.ytitle').should('have.text', 'Total')
    getIframeBody().find('.xtitle').should('have.text', 'Data')
    getIframeBody().find('g.trace.bars').find('g.point').should('have.length', 24)
    getIframeBody().find('g.xaxislayer-above').find('g.xtick').should('have.length', 6)
    getIframeBody().find('g.xaxislayer-above').find('g.xtick:eq(5)').should('have.text', lastMonth)
    getIframeBody().find('div.modebar-group:eq(0)').find('a.modebar-btn')
     .invoke('attr', 'data-title')
     .should('eq', 'Download plot as a png')
    getIframeBody().find('div.modebar-group:eq(0)').find('a.modebar-btn').click()
    cy.readFile('cypress/downloads/newplot.png').should('exist')
  })
})