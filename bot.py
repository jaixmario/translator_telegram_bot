import os
import json
import telebot
import google.generativeai as genai

# === Configuration ===
API_KEY = "your-gemini-api-key"
BOT_TOKEN = "your-bot-token"
CONFIG_FILE = "user_config.json"

# === Setup ===
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")
bot = telebot.TeleBot(BOT_TOKEN)

# === Load/Save Config ===
def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_config(data):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

user_config = load_config()

# === Command Handler ===
@bot.message_handler(commands=["set"])
def handle_set(message):
    try:
        parts = message.text.split()
        if len(parts) != 2 or "_to_" not in parts[1]:
            return bot.reply_to(message, "❌ Usage: /set hindi_to_gujarati")

        user_id = str(message.from_user.id)
        source_lang, target_lang = parts[1].split("_to_")
        user_config[user_id] = {
            "lang1": source_lang.lower(),
            "lang2": target_lang.lower()
        }
        save_config(user_config)
        bot.reply_to(message, f"✅ Set translation pair: {source_lang} ↔ {target_lang}")
    except Exception as e:
        bot.reply_to(message, f"❌ Error: {e}")

# === Prompt ===
def build_prompt(text, lang1, lang2):
    return f"""
You are a bilingual casual translator. Detect whether this sentence is in {lang1} or {lang2}.
If it's in {lang1}, translate it to {lang2} in Hinglish. If it's in {lang2}, translate to {lang1} in Hinglish.
Only reply with the translated sentence in Hinglish, no explanation.

Sentence: "{text}"
Translation:
"""

# === Message Handler ===
@bot.message_handler(func=lambda m: True)
def handle_message(message):
    user_id = str(message.from_user.id)
    if user_id not in user_config:
        return bot.reply_to(message, "⚙️ Please set direction first using /set hindi_to_gujarati or similar.")

    lang1 = user_config[user_id]["lang1"]
    lang2 = user_config[user_id]["lang2"]
    text = message.text.strip()

    prompt = build_prompt(text, lang1, lang2)

    try:
        response = model.generate_content(prompt)
        translation = response.text.strip().strip("\"")
        bot.reply_to(
            message,
            f"🔁 Translated Hinglish:\n`{translation}`",
            parse_mode="Markdown"
        )
    except Exception as e:
        bot.reply_to(message, f"❌ Error: {e}")

# === Start Bot ===
print("🤖 Bot is running...")
bot.infinity_polling()
