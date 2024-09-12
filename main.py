import pyautogui, time, random, os, signal, logging
from random import randint
from datetime import datetime

C = "\033[36m"
G = "\033[32m"
R = "\033[31m"

base_dir = os.path.dirname(os.path.realpath(__file__))
logging.basicConfig(filename="{}/app.log".format(base_dir), level=logging.INFO)


def runKeyboardEvent():
    count = randint(15, 30)
    logging.info("[+] Doing keyboard event with {} hits.".format(count))
    action = ["left", "right", "up", "down"]
    for number in range(count):
        pyautogui.press(random.choice(action))


def runMouseEvent():
    count = randint(5, 10)
    logging.info("[+] Doing mouse event with {} hits.".format(count))
    for number in range(count):
        pyautogui.click()


def run():
    count = randint(5, 10)
    pyautogui.keyDown("ctrl")
    for number in range(count):
        pyautogui.press("tab")
    pyautogui.keyUp("ctrl")
    runKeyboardEvent()
    time.sleep(10)
    runMouseEvent()
    time.sleep(40)


def signalHandler(sig, frame):
    logging.info("[+] CTRL+C detected. Closing terminal window...")
    os.kill(os.getppid(), signal.SIGHUP)


if __name__ == "__main__":
    option = pyautogui.confirm("Shall I proceed?")
    if "ok" in option.lower():
        signal.signal(signal.SIGINT, signalHandler)
        while True:
            logging.info(
                "[+] Started at: {}".format(datetime.now().strftime("%H:%M:%S"))
            )
            run()
            logging.info(
                "-"*50
            )
