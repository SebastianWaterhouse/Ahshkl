from ... import ahshklsettings as sett

class modCommands():
	#For modders to place commands. PLEASE do not place in the ahshklcommands file.
	def passs(): #Delete this functions
		print("Please delete")
	commands = {
	"pass":passs #Delete this line
	}
	#Register commands in the commands dictionary by placing "command_name":command_function

class modCredits():
	def TheRambler():
		github_username = "TheRambler" #REQUIRED
		real_name = "Sebastian W." #OPTIONAL
		email = "littlestllama6@gmail.com" #RECOMMENDED
		twitter = "@littlestllama6" #OPTIONAL
	credits = {
		"pass":TheRambler #Delete this line
	}
