from ECE16Lib.Communication import Communication
from time import sleep

if __name__ == "__main__":

  try:
    # Main program code should go here
    comms = Communication()
    comms = Communication("COM4", 115200)
    comms.clear()
    for X in range(1, 31):
        message = str(X) + " seconds"
        comms.send_message(message)
        sleep(1)
        received = comms.receive_message()
        print(received)
    print("Normal program execution finished")
  except KeyboardInterrupt:
    print("User stopped the program with CTRL+C input")
  finally:
    # Clean up code should go here (e.g., closing comms)
    comms.clear()
    print("Cleaning up and exiting the program")

  