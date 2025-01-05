from solana.transaction import Transaction
from solana.system_program import CreateAccountParams, create_account
from solana.rpc.api import Client
from solana.keypair import Keypair

class TokenLauncher:
    def __init__(self):
        self.status = "Not started"
        self.client = Client("https://api.mainnet-beta.solana.com")

    def launch_token(self, name, symbol, decimals, supply):
        """Launch a new SPL token."""
        self.status = "Launching..."
        try:
            mint = Keypair.generate()
            owner = Keypair.generate()
            
            # Create the mint account
            create_account_params = CreateAccountParams(
                from_pubkey=owner.public_key,
                new_account_pubkey=mint.public_key,
                lamports=self.client.get_minimum_balance_for_rent_exemption(82)["result"],
                space=82,
                program_id="TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA",
            )
            tx = Transaction().add(create_account(create_account_params))
            self.client.send_transaction(tx, owner)

            # Additional steps for mint initialization, setting metadata, etc.
            self.status = f"Token '{name}' ({symbol}) launched successfully!"
            return self.status
        except Exception as e:
            self.status = f"Error: {str(e)}"
            return self.status

    def get_launch_status(self):
        """Get the current status of the token launch."""
        return self.status
