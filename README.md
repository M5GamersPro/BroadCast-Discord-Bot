# Discord Broadcast Bot 🚀

An efficient, custom-built Discord utility bot engineered to broadcast text announcements to server members via Direct Messages. Built using Python and the `discord.py` framework, this project supports legacy compatibility patches for modern Python runtime environments (including Python 3.14).

---

## 🛠️ Complete Local Installation Setup

Follow these exact steps to download, install, and execute this bot repository locally on your computer.

### Step 1: Clone the Project Workspace
Open your system terminal (Command Prompt on Windows or Terminal on macOS) and run the following command to download this project folder:
```bash
git clone https://github.com/BossProGamerYT/BroadCast-Discord-Bot
```

cd Broadcast-Bot
```

### Step 2: Install System Dependencies
Install all core routing requirements and library frameworks listed in the setup manifest:
```bash
pip install -r requirements.txt
```
*(Note: If you are running macOS, use `pip3 install -r requirements.txt` instead).*

### Step 3: Enable Developer Gateway Intents
For the broadcast mechanism to find and index your target server members, you must activate specific permission parameters in the developer panel:
1. Navigate to the **[Discord Developer Portal](https://discord.com)**.
2. Click on your active application profile card, then select the **Bot** tab on the left sidebar.
3. Scroll down to the **Privileged Gateway Intents** section.
4. Toggle **ON** the switches for both `Server Members Intent` and `Message Content Intent`.
5. Click **Save Changes** at the bottom of the screen.

### Step 4: Configure Local Token Execution
1. Open the `bot.py` file inside your project folder using a text editor.
2. Scroll to the bottom of the file and paste your secret authorization token inside the quotation marks:
   ```python
   SECRET_TOKEN = "YOUR_DISCORD_BOT_TOKEN_HERE"
   ```
3. Initialize the application connection from your terminal window:
   ```bash
   python bot.py
   ```
   *(Note: Use `python3 bot.py` if running on macOS).*

---

## ☁️ Complete 24/7 Free Cloud Deployment Steps

To host your bot online 24/7 for free using **Render** without revealing your private bot token to the public, follow these platform deployment steps:

### Step 1: Prepare the Cloud Code Configuration
Ensure the bottom of your `bot.py` file is configured to look for environmental storage variables instead of a hardcoded string:
```python
import os
SECRET_TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(SECRET_TOKEN)
```

### Step 2: Connect Repository to Render
1. Navigate to **[Render](https://render.com)** and create or sign into a free account utilizing your GitHub account authorization.
2. From the main dashboard screen, click the blue **New +** button in the upper-right corner and select **Background Worker**.
3. Under the GitHub repository integration menu list, find `Omar-Broadcast-Bot` and click **Connect**.

### Step 3: Configure Cloud Environment Profiles
Input these exact configurations on the deployment creation workspace screen:
- **Name:** `omar-community-bot`
- **Region:** Choose the location closest to your target audience.
- **Runtime:** `Python`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `python bot.py`

### Step 4: Securely Input Your Secret Token
1. On that same creation page, click the **Advanced** drop-down array or look for the **Environment Variables** block.
2. Click **Add Environment Variable**.
3. In the **Key** field, type: `DISCORD_TOKEN`
4. In the **Value** field, paste your actual secret Discord Bot Token.
5. Scroll to the bottom, verify that the **Free Tier (\$0/mo)** plan profile is actively highlighted, and click **Create Background Worker**.

---

## 📬 Usage Command Map

| Command | Permission Level | Context Description |
| :--- | :--- | :--- |
| `-obc {message}` | **Administrator** | Initiates a direct message broadcast loop containing your message string to all accessible server users. |

*Example Live Interaction:*
```text
-obc Hello team! This is an official update regarding our upcoming server migration details.
```

---

## ⚠️ Security Notice & Platform Policy
**Important Disclaimer:** Automated mass direct messaging features run an extremely high risk of triggering automated spam detection algorithms on the Discord network. This utility script is engineered exclusively for closed, internal community management distribution. The repository author does not accept liability for administrative account terminations resulting from platform manipulation violations or policy non-compliance. **Never commit your active production token keys directly to public GitHub files.**
