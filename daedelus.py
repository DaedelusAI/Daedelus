from utils.prompts import TOKEN_LAUNCH_GUIDE
from token_launcher import TokenLauncher

class Daedelus:
    def __init__(self):
        self.launcher = TokenLauncher()

    def handle_command(self, command, args):
        """Handle user commands."""
        if command == "launch":
            return self.launcher.launch_token(*args)
        elif command == "guide":
            return TOKEN_LAUNCH_GUIDE
        elif command == "status":
            return self.launcher.get_launch_status()
        return "Unknown command. Try /guide, /launch, or /status."
