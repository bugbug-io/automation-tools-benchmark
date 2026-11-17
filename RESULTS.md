# Hands-on test: raw results (run 2026-11-16, Europe/Warsaw afternoon; first Playwright run 14:11 UTC)

Scenario (same as Katalon's Nov 4, 2026 test): open https://demo.playwright.dev/todomvc/, add "Write the regression suite",
check the item is listed and the counter reads "1 item left". 5 runs per tool, median reported.

Machine: macOS 14 (Darwin 23.3.0), Node 24.22.1, Python 3.14.5, Google Chrome 157.0.8103.51.

| Tool | Version | Non-blank lines | Runs passed | Per-run times | Median | What the time measures |
|---|---|---|---|---|---|---|
| Playwright (@playwright/test, channel chrome) | 1.65.1 | 9 (+3 config) | 5/5 (+1 cold run 961 ms) | 384, 515, 360, 354, 354 ms | 360 ms | test body as reported by Playwright, warm |
| Cypress (chrome headless) | 16.3.0 | 8 (+3 config) | 5/5 (+1 first run 254 ms) | 252, 436, 254, 281, 268 ms | 268 ms | test body as reported by Cypress |
| Selenium (Python + pytest 9.2.0) | 4.52.0 | 20 | 5/5 (+1 first run 4.29 s total) | call: 1.44, 1.34, 0.36, 0.30, 0.33 s; setup: 0.51, 0.48, 0.48, 0.45, 0.47 s | call 0.36 s, setup 0.48 s | pytest call phase; setup = ChromeDriver + browser start |
| BugBug (cloud run, profile "Base") | extension 14.23.1, cloud Chrome 150, Linux | 4 steps, no code | 5/5 after fix (first run failed) | 8.26, 7.34, 7.38, 8.62, 10.75 s | 8.26 s | whole cloud run start→end incl. browser start and default waiting conditions |

BugBug first run (8d24fe8c-8be0-45d4-8e48-5eecd3752ca7) failed at step 4: waiting condition "elementIsNotCovered"
returned false for [data-testid="todo-count"] (TodoMVC footer is overlapped). Fix: disabled that one waiting condition on that step.
BugBug test: project "Do Testów", test id cacef02c-573e-4409-b01d-6f7bab9bbe28.
Passing run ids: 6d4edf69-baf2-4e31-9f82-ea1598ddfa63, 7324d73f-8eda-4e6a-bc3e-0b647aa3d59c, c67244bc-dd46-4d39-ad65-f137dca66902,
fb190571-f0a0-49c0-bf1b-6ddff39b685c, ac234a9d-b6a1-4931-9b88-f5a7fadd6ef2.

Times are NOT a speed ranking: each tool measures a different scope (local warm test body vs full cloud session).
