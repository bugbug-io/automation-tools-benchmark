import { test, expect } from '@playwright/test';

test('add a todo item', async ({ page }) => {
  await page.goto('https://demo.playwright.dev/todomvc/');
  const input = page.getByPlaceholder('What needs to be done?');
  await input.fill('Write the regression suite');
  await input.press('Enter');
  await expect(page.getByTestId('todo-title')).toHaveText(['Write the regression suite']);
  await expect(page.getByTestId('todo-count')).toHaveText('1 item left');
});
