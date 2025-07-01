# 🤖 Telegram Hinglish Translator Bot

✨ This is an AI-powered Telegram bot that seamlessly translates text between two specified languages, converting them into Hinglish (a vibrant mix of Hindi and English) or vice-versa. It harnesses the power of the Google Gemini API for its intelligent translation capabilities.

## 🚀 Features

*   **Bilingual Translation:** Effortlessly translates between any two user-defined languages.
*   **Hinglish Conversion:** Uniquely designed to provide natural and fluent translations into or from Hinglish.
*   **User-Specific Language Pairs:** Each user can personalize their translation experience by setting their preferred language pair with a simple command.
*   **AI-Powered:** Driven by the advanced `gemini-2.5-flash` model, ensuring accurate, context-aware, and high-quality translations.

## 🛠️ Installation

Follow these simple steps to get your Hinglish Translator Bot up and running:

### 📋 Prerequisites

Ensure you have the following installed:

*   Python 3.8 or higher
*   `pyTelegramBotAPI` library
*   `google-generativeai` library

### 🔑 1. Obtain API Keys

To enable the bot's functionality, you'll need two essential API keys:

*   **Telegram Bot Token:** Create a new bot on Telegram using [@BotFather](https://t.me/botfather) and retrieve your unique API token.
*   **Google Gemini API Key:** Get your API key from the [Google AI Studio](https://aistudio.google.com/app/apikey) (formerly Google Cloud AI Platform).

### ⬇️ 2. Clone the Repository (or Create `bot.py`)

If you have cloned the repository, navigate to the project directory. Otherwise, create a new file named `bot.py` and paste the provided code into it.

### 📦 3. Install Dependencies

Open your terminal or command prompt and execute the following command to install the necessary Python libraries:

```bash
pip install pyTelegramBotAPI google-generativeai
```

### ⚙️ 4. Configure the Bot

Open the `bot.py` file in your preferred text editor and replace the placeholder values with your actual API keys:

```python
API_KEY = "your-gemini-api-key"  # ➡️ Replace with your Google Gemini API Key
BOT_TOKEN = "your-bot-token"    # ➡️ Replace with your Telegram Bot Token
```

### ▶️ 5. Run the Bot

Once configured, launch the bot by running the `bot.py` file from your terminal:

```bash
python bot.py
```

Your bot should now be active and ready to translate messages on Telegram!

## 💬 Usage

Interacting with your Hinglish Translator Bot is straightforward:

### 🌐 Setting Translation Languages

Before you begin translating, you must define your desired source and target languages. Use the `/set` command in this format:

`/set <source_language>_to_<target_language>`

**Examples:**

*   `/set hindi_to_gujarati` 🇮🇳
*   `/set english_to_hindi` 🇬🇧➡️🇮🇳
*   `/set gujarati_to_english` 🇮🇳➡️🇬🇧

### ✍️ Translating Text

After successfully setting your language pair, simply send any text message to the bot. The bot will intelligently detect the language (between the two you've set) and provide a Hinglish translation in response.

## 🧠 How it Works (AI-Powered Guide)

This bot's core translation logic is powered by Google's Generative AI, specifically the `gemini-2.5-flash` model. Here's a detailed breakdown of its intelligent workflow:

1.  **Language Pair Configuration:** When a user initiates the `/set` command, the bot securely stores their chosen source and target languages (e.g., Hindi and Gujarati) in a configuration file.
2.  **Dynamic Prompt Generation:** For every incoming message, the bot dynamically crafts a tailored prompt for the Gemini model. This prompt explicitly instructs the AI to function as a bilingual casual translator, translating the input sentence into Hinglish based on the user's pre-configured language pair.
3.  **AI Translation:** The Gemini model then processes this prompt along with the user's message. It performs the complex task of language detection and translation, generating the appropriate Hinglish output.
4.  **Hinglish Output Delivery:** Finally, the bot extracts the translated text from the AI's response, formats it, and promptly sends it back to the user on Telegram.

This sophisticated approach enables highly flexible and intelligent translation, seamlessly adapting to individual user preferences and delivering natural-sounding Hinglish translations.

## 🤝 Contributing

We welcome contributions to enhance this project! If you have suggestions for improvements, new features, or bug fixes, please feel free to open an issue or submit a pull request. Your contributions are highly valued!
