# Daedelus 🚀

**Daedelus** is an AI-powered framework for launching and managing Solana tokens. It combines the power of conversational AI with blockchain automation, offering guided token creation, real-time updates, and seamless Telegram integration. Developers can use Daedelus to simplify blockchain development with minimal effort.

---

## **Features** ✨

- **Automated Token Deployment**: Effortlessly launch SPL tokens on Solana.
- **AI Guidance**: Conversational AI to assist with tokenomics and launch steps.
- **Interactive Commands**: Use `/launch`, `/guide`, and `/status` to manage token creation and tracking.
- **Token Access**: Powered by **$DAI** tokens for secure and controlled functionality.
- **Seamless Integration**: Works out of the box with Telegram and CLI tools.

---

## **How It Works** 🔧

1. **$DAI Token Requirement**:
   - To use Daedelus, you must hold a minimum balance of **100 $DAI** in your wallet.
   - The system checks your wallet before executing any commands.

2. **Command Structure**:
   - `/launch`: Create a new token with specified parameters.
   - `/guide`: Get a detailed guide on launching tokens.
   - `/status`: View the current status of your token launch.

---

## **Setup** 🛠️

### **Prerequisites**

1. **Python 3.9+** installed on your system.
2. A **Solana wallet** with at least 100 $DAI tokens.
3. A **Telegram bot token** from BotFather.

### **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/DaedelusAI/Daedelus.git
   cd Daedelus
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables in a `.env` file:
   ```env
   TELEGRAM_TOKEN=your_telegram_bot_token
   SOLANA_RPC_URL=https://api.mainnet-beta.solana.com
   ```

4. Run the Telegram bot:
   ```bash
   python app.py
   ```

---

## **Usage** 💬

### **Telegram Commands**

- **`/guide`**: View the token launch guide.
- **`/launch <name> <symbol> <decimals> <supply>`**:
  - Launch a new SPL token.
  - Example: `/launch MyToken MYT 9 1000000`
- **`/status`**: Check the status of your launch.

### **$DAI Token Integration**

- Before using any command, Daedelus verifies that your wallet holds the required **100 $DAI**.
- This ensures a secure and token-gated environment for all users.

---

## **Example Interaction** 🤖

1. User sends `/guide`.
   - Bot responds with the Token Launch Guide.

2. User sends `/launch MyToken MYT 9 1000000`.
   - Daedelus verifies the wallet balance and launches the token.
   - Bot confirms the successful creation of the token.

3. User sends `/status`.
   - Bot provides the current status of the token launch process.

---

## **Roadmap** 🛤️

- **Wallet Integration**: Enhanced support for wallet interactions.
- **Analytics**: Add tracking for token performance metrics.
- **Multi-Platform Support**: Extend functionality to Discord and Slack.
- **More Token Utilities**: Integrate staking, governance, and liquidity tools.

---

## **License** 📜

This project is licensed under the **MIT License**.

For more details, visit the [Daedelus GitHub Repository](https://github.com/DaedelusAI/Daedelus).

