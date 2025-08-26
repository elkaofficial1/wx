import os
import time


frame1 = [
    "       \\ | /\n",
    "    '-.;;;.-'\n",
    "   -==;;;;;==-\n",
    "    .-';;;'-.\n",
    "      / | \\\n",
    "        '\n"
]

frame2 = [
    "      - \\ / -\n",
    "    .-';;;;-.'\n",
    "   ==;;;;;;;==\n",
    "    '-.;;;.-'\n",
    "      - / \\ -\n",
    "        '\n"
]

frame3 = [
    "      / | \\\n",
    "    .-';;;;-.'\n",
    "   ==;;;;;;;==\n",
    "    '-.;;;.-'\n",
    "      \\ | /\n",
    "        '\n"
]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_animation():
    while True:
        print(*frame1) 
        time.sleep(0.9)
        clear()
        return frame2
        time.sleep(0.9)
        clear()


#print(*frame3)
#time.sleep(0.3)
#clear()


show_animation()

