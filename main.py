import capture as cp

def menu():
  """
  Shows simple interface to work with the stereo vision project.
  """
  choice = ""
  while not choice == "q":
    print "1. Get live feed from the Stereo Camera's"
    print "2. Caliberate Camera Parameters"
    print "q. Exit"

    choice = raw_input("> ")
    if not ((choice.isdigit() and (0 < int(choice) < 3)) or choice == "q"):
      print "Please enter a correct choice : "
      continue

    if choice == "1":
      cp.live(0,1)
      continue

    if choice == "2":
      #Blank as of now.
      continue
      
    if choice == "q":
      print "Exiting."
      break

if __name__ == "__main__":
  menu()
