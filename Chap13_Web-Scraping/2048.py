# The game 2048 is a simple game in which you combine tiles by sliding them up, 
# down, left, or right with the arrow keys. You can actually get a fairly high 
# score by sliding tiles in random directions. Write a program that will open 
# the game at https://play2048.co and keep sending up, right, down, and left 
# keystrokes to automatically play the game.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# fire up chrome browser
browser = webdriver.Chrome()
print("Loading...")

# open the play2048.co link
browser.get('https://play2048.co')
print("Page successfully loaded!")

# Locate the 2048 header
elems = browser.find_element(By.TAG_NAME, 'h1')
# locate the html tag for the keystrokes
html_elem = browser.find_element(By.TAG_NAME, 'html')

# Activate keystrokes
print("Game Started.")
while elems.is_displayed():
    # up keystroke
    html_elem.send_keys(Keys.UP)
    # right keystroke
    html_elem.send_keys(Keys.RIGHT)
    # down keystroke
    html_elem.send_keys(Keys.DOWN)
    # left keystroke
    html_elem.send_keys(Keys.LEFT)

# end game after losing
print("Game Over.")
