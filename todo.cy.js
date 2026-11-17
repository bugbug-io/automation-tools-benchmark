describe('todo', () => {
  it('adds a todo item', () => {
    cy.visit('https://demo.playwright.dev/todomvc/');
    cy.get('.new-todo').type('Write the regression suite{enter}');
    cy.get('[data-testid="todo-title"]').should('have.text', 'Write the regression suite');
    cy.get('[data-testid="todo-count"]').should('have.text', '1 item left');
  });
});
