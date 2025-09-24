# The game 2048 is a simple game in which you combine tiles by sliding them up, 
# down, left, or right with the arrow keys. You can actually get a fairly high 
# score by sliding tiles in random directions. Write a program that will open 
# the game at https://play2048.co and keep sending up, right, down, and left 
# keystrokes to automatically play the game.

from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.firefox.launch(headless=False, slow_mo=50)
page = browser.new_page()
page.goto('https://play2048.co')
page.locator('html').press('End')

