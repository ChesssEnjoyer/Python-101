#! usr/bin/env python3

import webbrowser

print("What do you want t oserach in browser?")
question = input()
print("The browser is opening")
webbrowser.open("https://google.com/search?q=" + question)
