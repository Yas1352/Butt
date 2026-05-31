import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '8823080084:AAEKCjHOKvJw8oDt6_rJUwWYR6sSk-U_de0'
bot = telebot.TeleBot(TOKEN)

# لیست سوالات FAQ
faq_list = [
    "🔹 1. Who are you?\nWhat is Voyager Crypto? From within our accounts section or the tree link, enter the Voyager Crypto site and click on the About Us or Company section.",
    "🔹 2. What is this server about?\nThis server is a community space for conversation, project updates, official announcements, creative discussions, and interaction between members.",
    "🔹 3. Where should I start?\nWe recommend: 1. Rules, 2. Welcome, 3. FAQ, 4. Introduce yourself, 5. Support.",
    "🔹 4. How do I get roles?\nRoles are assigned automatically or through specific sections of the server. Contact Support if needed.",
    "🔹 5. How can I access the Holders Chat?\nHolders Chat is exclusive to verified holders. Open a ticket in Support for verification.",
    "🔹 6. Where can I find your official accounts?\nAll official links are listed in the Our-Account section. Do not trust other links.",
    "🔹 7. What should I do if I have a problem or need help?\nUse the Support section to submit requests, report technical issues, or ask questions.",
    "🔹 8. Where can I find the server rules?\nAll rules are located in the Rules channel.",
    "🔹 9. What are the differences between the chat sections?\nGeneral Chat (casual), Cosmic Chat (creative), and Holders Chat (exclusive).",
    "🔹 10. What is Voyager Card?\nEach NFT is a Voyager Card, a gift carrying a piece of the universe, explaining the story and creative process.",
    "🔹 11. Where can I follow official project updates?\nIn the Announcements and Roadmap sections.",
    "🔹 12. How do I connect my wallet or fix wallet issues?\nThe Wallet Help section contains full instructions.",
    "🔹 13. What should I do if someone breaks the rules?\nReport the issue through the Support section.",
    "🔹 14. Can I advertise here?\nAdvertising without admin approval is not allowed. Submit a request through Support.",
    "🔹 15. Can I share my own content?\nYes, but only in the appropriate channels.",
    "🔹 16. How can I view the Voyager Crypto NFTs?\nVisit the Collections section in the server.",
    "🔹 17. Where can I find the newest released NFTs?\nIn Announcements and Collections.",
    "🔹 18. How do I know which NFTs are still available for purchase?\nIn Collections, each NFT has a direct link to the marketplace.",
    "🔹 19. How can I get more information about each NFT?\nClick on any NFT in the Collections section to view metadata and links.",
    "🔹 20. Do I need to be a holder to view the NFTs?\nNo, everyone can view, but Holders Chat is exclusive.",
    "🔹 21. How can I quickly find a specific NFT?\nUse the organized categories in the Collections section.",
    "🔹 22. What should I do if an NFT link doesn’t work?\nReport it to the Support section.",
    "🔹 23. What if my question isn’t listed here?\nVisit the Support section and ask us directly."
]

def get_main_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton("🛒 Marketplace", callback_data="main_marketplace"))
    markup.add(InlineKeyboardButton("✨ Voyager family", callback_data="main_family"))
    markup.add(InlineKeyboardButton("🌐 Community", callback_data="main_community"))
    markup.row(InlineKeyboardButton("🎀 Showcases", callback_data="main_showcases"), InlineKeyboardButton("🗺️ Roadmap", callback_data="main_roadmap"))
    markup.row(InlineKeyboardButton("🌠 Collections", callback_data="main_collections"), InlineKeyboardButton("💰 Wallet-help", callback_data="main_wallet"))
    markup.row(InlineKeyboardButton("⚠️ FAQ", callback_data="faq_0"), InlineKeyboardButton("🛠️ Support", callback_data="main_support"))
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Welcome to the official Voyager Crypto Telegram Bot! 🌌✨", reply_markup=get_main_menu())

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    chat_id = call.message.chat.id
    msg_id = call.message.message_id
    data = call.data

    if data == "back_to_main":
        bot.edit_message_text(chat_id=chat_id, message_id=msg_id, text="Welcome to the official Voyager Crypto Telegram Bot! 🌌✨", reply_markup=get_main_menu())
    
    # Marketplace
    elif data == "main_marketplace":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("objkt", url="https://objkt.com/users/tz1WbCXq2b53SvrfhCv7kEPt2XmbhiZEZSH3"))
        markup.add(InlineKeyboardButton("Foundation", callback_data="coming_soon"))
        markup.add(InlineKeyboardButton("🏠 Back to Main Menu", callback_data="back_to_main"))
        bot.edit_message_text(chat_id=chat_id, message_id=msg_id, text="Marketplace options:", reply_markup=markup)

    # Voyager Family
    elif data == "main_family":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Voyager Crypto site", url="https://nftvoyagercrypto.wixstudio.com/vcnft"))
        markup.add(InlineKeyboardButton("Voyager card", url="https://bottles-call-hil.craft.me/nVIzcdjhWJMPf2"))
        markup.add(InlineKeyboardButton("Voyager chat", callback_data="show_email_family"))
        markup.add(InlineKeyboardButton("Mission(about Us)", url="https://nftvoyagercrypto.wixstudio.com/vcnft/company"))
        markup.add(InlineKeyboardButton("🏠 Back to Main Menu", callback_data="back_to_main"))
        bot.edit_message_text(chat_id=chat_id, message_id=msg_id, text="Voyager Family:", reply_markup=markup)

    # Community
    elif data == "main_community":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Discord", url="https://discord.gg/yH7yH9Zswy"))
        markup.add(InlineKeyboardButton("X", url="https://x.com/VCryptoNft"))
        markup.add(InlineKeyboardButton("Gmail", callback_data="show_email_community"))
        markup.add(InlineKeyboardButton("🏠 Back to Main Menu", callback_data="back_to_main"))
        bot.edit_message_text(chat_id=chat_id, message_id=msg_id, text="Our Community:", reply_markup=markup)

    # Showcases
    elif data == "main_showcases":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Oncyber", url="https://oncyber.io/@voyagercrypto"))
        markup.add(InlineKeyboardButton("🏠 Back to Main Menu", callback_data="back_to_main"))
        bot.edit_message_text(chat_id=chat_id, message_id=msg_id, text="Showcases:", reply_markup=markup)

    # Roadmap
    elif data == "main_roadmap":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("🏠 Back to Main Menu", callback_data="back_to_main"))
        bot.edit_message_text(chat_id=chat_id, message_id=msg_id, text="This section reveals the path ahead — a sequence of milestones that shine like stars guiding our future. Each step marks a new chapter in the expansion of our universe, showing the direction of our ascent. Here lies our journey’s map — clear, elegant, and reaching toward the infinite.", reply_markup=markup)

    # Collections
    elif data == "main_collections":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("collections", url="https://nftvoyagercrypto.wixstudio.com/vcnft/games"))
        markup.add(InlineKeyboardButton("🏠 Back to Main Menu", callback_data="back_to_main"))
        bot.edit_message_text(chat_id=chat_id, message_id=msg_id, text="Welcome to the gallery of our universe — where each collection shines like a solitary star in the cosmic dark. Every piece is a constellation of pixels, carrying a hidden story born from the void. Step gently, and discover the worlds waiting within.", reply_markup=markup)

    # Wallet Help
    elif data == "main_wallet":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("🏠 Back to Main Menu", callback_data="back_to_main"))
        bot.edit_message_text(chat_id=chat_id, message_id=msg_id, text="Here you’ll find guidance for your wallet — instructions on connecting, using, and solving common issues.", reply_markup=markup)

    # Support
    elif data == "main_support":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("🏠 Back to Main Menu", callback_data="back_to_main"))
        bot.edit_message_text(chat_id=chat_id, message_id=msg_id, text="The Support section is designed to assist you whenever you need help. Here you’ll find guidance for resolving common issues, answers to your questions, and ways to connect with our support team. The goal of this section is to provide quick and easy access to the information and assistance you need, ensuring a smoother and more reliable experience.", reply_markup=markup)

    # FAQ Logic
    elif data.startswith("faq_"):
        idx = int(data.split("_")[1])
        if idx == 0:
            text = "FAQ📃 \n“Here you’ll find answers to frequently asked questions — a quick guide to help you understand the rules, processes, and details of our brand.”\n\n" + faq_list[idx]
        else:
            text = faq_list[idx]
            
        markup = InlineKeyboardMarkup()
        row = []
        if idx > 0: row.append(InlineKeyboardButton("⬅️ Back", callback_data=f"faq_{idx-1}"))
        if idx < len(faq_list) - 1: row.append(InlineKeyboardButton("➡️ Next", callback_data=f"faq_{idx+1}"))
        markup.row(*row)
        markup.add(InlineKeyboardButton("🏠 Back to Main Menu", callback_data="back_to_main"))
        bot.edit_message_text(chat_id=chat_id, message_id=msg_id, text=text, reply_markup=markup)

    # Helper callbacks
    elif data == "show_email_family":
        bot.answer_callback_query(call.id, "Voyager.is.alive@gmail.com", show_alert=True)
    elif data == "show_email_community":
        bot.answer_callback_query(call.id, "nftVoyagerCrypto@gmail.com", show_alert=True)
    elif data == "coming_soon":
        bot.answer_callback_query(call.id, "Coming soon✨", show_alert=True)

    bot.answer_callback_query(call.id)

print("Voyager Bot is Running...")
bot.infinity_polling(none_stop=True)
