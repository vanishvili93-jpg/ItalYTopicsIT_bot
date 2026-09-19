import os
import re
import telebot
from telebot import types

BOT_TOKEN = re.sub(r"\s+", "", os.environ["TELEGRAM_BOT_TOKEN"])
WEB_APP_URL = os.environ.get("WEB_APP_URL", "").strip()

bot = telebot.TeleBot(BOT_TOKEN)

try:
    if WEB_APP_URL:
        bot.set_chat_menu_button(menu_button=types.MenuButtonWebApp(type="web_app", text="Ανοίξτε", web_app=types.WebAppInfo(url=WEB_APP_URL)))
except Exception as e:
    print("Menu button error: " + str(e))


def open_button():
    if WEB_APP_URL:
        return types.InlineKeyboardButton(text="📊 Ανοίξτε την πλατφόρμα", web_app=types.WebAppInfo(url=WEB_APP_URL))
    return types.InlineKeyboardButton(text="📊 Ανοίξτε την πλατφόρμα", url="https://www.athexgroup.gr")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Θέματα ημέρας", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Περίληψη", callback_data="summary"))
    text = ("📊 *Καλώς ήρθατε.*\n\n"
        "Επενδυτικές αναλύσεις, ενημέρωση αγορών "
        "και διαχείριση χαρτοφυλακίου — κάθε μέρα "
        "στο Telegram.\n\n"
        "Τριάντα χρόνια στην ελληνική κεφαλαιαγορά. "
        "Μετοχές, παράγωγα, διαχείριση κεφαλαίων.\n\n"
        "Πατήστε *Θέματα ημέρας* για να ξεκινήσετε.")
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "headlines")
def headlines(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(text="📈 Μετοχές — ανάλυση αγοράς", callback_data="stocks"),
        types.InlineKeyboardButton(text="📉 Παράγωγα — στρατηγικές", callback_data="derivatives"),
        types.InlineKeyboardButton(text="💼 Διαχείριση χαρτοφυλακίου", callback_data="portfolio"),
        types.InlineKeyboardButton(text="🏛 Περίληψη", callback_data="summary"))
    text = ("📋 *Θέματα ημέρας*\n\n"
        "Τρία κείμενα επιλεγμένα για σήμερα.\n\n"
        "*Μετοχές* — ανάλυση αγοράς: Γενικός "
        "Δείκτης, τραπεζικός, βασικοί τίτλοι.\n\n"
        "*Παράγωγα* — στρατηγικές σε options "
        "και futures στο ΧΑ.\n\n"
        "*Διαχείριση χαρτοφυλακίου* — πώς "
        "λειτουργεί η μερίδα και τι προσφέρει "
        "ο υπεύθυνος σύμβουλος.\n\n"
        "Πατήστε έναν τίτλο για να διαβάσετε.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "stocks")
def stocks(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Θέματα ημέρας", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Περίληψη", callback_data="summary"))
    text = ("📈 *Ανάλυση αγοράς — Χρηματιστήριο Αθηνών*\n\n"
        "*Γενικός Δείκτης: 1.684,20* (+0,55%)\n"
        "Η αγορά κινήθηκε ανοδικά με αυξημένο "
        "όγκο συναλλαγών. Οι τράπεζες οδήγησαν "
        "την άνοδο.\n\n"
        "*ΕΤΕ — 8,74 (+1,14%)*\n"
        "Η Εθνική συνεχίζει ανοδικά μετά τα "
        "αποτελέσματα τριμήνου. Αναλυτές βλέπουν "
        "στόχο κοντά στα 9,50.\n\n"
        "*METLEN — 38,46 (+0,78%)*\n"
        "Σταθερή πορεία για τη Metlen Energy. "
        "Η ενεργειακή δραστηριότητα στηρίζει "
        "τα μεγέθη.\n\n"
        "*ΟΠΑΠ — 16,92 (-0,35%)*\n"
        "Ήπια διόρθωση μετά τις πρόσφατες "
        "ανόδους. Το μέρισμα παραμένει ελκυστικό "
        "για τους μακροπρόθεσμους επενδυτές.\n\n"
        "*ΟΤΕ — 15,20 (+0,40%)*\n"
        "Σταθερή ζήτηση στον τίτλο. Η μερισματική "
        "πολιτική ενισχύει το ενδιαφέρον.\n\n"
        "_Ενδεικτικές τιμές με καθυστέρηση 15 λεπτών._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "derivatives")
def derivatives(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Θέματα ημέρας", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Περίληψη", callback_data="summary"))
    text = ("📉 *Παράγωγα — στρατηγικές στο ΧΑ*\n\n"
        "*Futures Γενικού Δείκτη*\n"
        "Ο Σεπτέμβριος κλείνει με premium "
        "στις 12 μονάδες. Οι θέσεις αγοράς "
        "υπερτερούν.\n\n"
        "*Options ΕΤΕ*\n"
        "Αυξημένο ενδιαφέρον στα call options "
        "Δεκεμβρίου. Η αγορά τοποθετείται "
        "για συνέχεια ανόδου.\n\n"
        "*Στρατηγική covered call*\n"
        "Για τον επενδυτή που κρατάει μετοχές "
        "και θέλει επιπλέον απόδοση. Πουλάτε "
        "call πάνω από την τρέχουσα τιμή και "
        "εισπράττετε το premium.\n\n"
        "*Στρατηγική protective put*\n"
        "Για προστασία χαρτοφυλακίου σε "
        "περίοδο αβεβαιότητας. Αγοράζετε "
        "put στην τιμή που θέλετε να κλειδώσετε.\n\n"
        "_Τα παράγωγα ενέχουν κίνδυνο απώλειας "
        "κεφαλαίου. Συμβουλευτείτε ειδικό._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "portfolio")
def portfolio(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Θέματα ημέρας", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Περίληψη", callback_data="summary"))
    text = ("💼 *Διαχείριση χαρτοφυλακίου*\n\n"
        "*Σύμβουλος με όνομα*\n"
        "Κάθε μερίδα αντιστοιχεί σε έναν "
        "υπεύθυνο με απευθείας τηλέφωνο. "
        "Καμία ουρά.\n\n"
        "*Χρεώσεις ολόκληρες*\n"
        "Προμήθεια, δικαιώματα χρηματιστηρίου "
        "και φόρος αναγράφονται πριν δοθεί "
        "η εντολή.\n\n"
        "*Χρήματα πελατών χωριστά*\n"
        "Τα χρήματα τηρούνται σε διακριτούς "
        "λογαριασμούς. Οι τίτλοι στη δική σας "
        "μερίδα στο Σ.Α.Τ.\n\n"
        "*Μία είσοδο για όλα*\n"
        "Μετρητά, παράγωγα, διεθνείς αγορές "
        "κάτω από τον ίδιο κωδικό πελάτη.\n\n"
        "*Πώς ανοίγετε μερίδα:*\n"
        "1. Αφήνετε τα στοιχεία σας\n"
        "2. Ταυτοποίηση με ταυτότητα και ΑΦΜ\n"
        "3. Κατάθεση και εκκίνηση\n\n"
        "_Μέλος ΧΑ και ΧΑΚ. Εποπτεία: "
        "Επιτροπή Κεφαλαιαγοράς._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "summary")
def summary(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.add(types.InlineKeyboardButton(text="📋 Θέματα ημέρας", callback_data="headlines"))
    markup.row(types.InlineKeyboardButton(text="📖 Γλωσσάριο", callback_data="glossary"), types.InlineKeyboardButton(text="❓ Ερωτήσεις", callback_data="faq"))
    markup.row(types.InlineKeyboardButton(text="✏️ Επικοινωνία", callback_data="contact"), types.InlineKeyboardButton(text="🏛 Πληροφορίες", callback_data="about"))
    text = ("🏛 *Περίληψη*\n\n"
        "Από αυτό το μενού μπορείτε:\n\n"
        "• Να διαβάσετε τα *θέματα ημέρας*.\n"
        "• Μετοχές, παράγωγα, διαχείριση.\n"
        "• Γλωσσάριο και συχνές ερωτήσεις.\n"
        "• Επικοινωνία και πληροφορίες.\n\n"
        "Για πλήρη πρόσβαση, πατήστε το κουμπί.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "glossary")
def glossary(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="📋 Θέματα ημέρας", callback_data="headlines"))
    markup.add(types.InlineKeyboardButton(text="🏛 Περίληψη", callback_data="summary"))
    text = ("📖 *Γλωσσάριο*\n\n"
        "*Μερίδα* — ο ατομικός λογαριασμός "
        "αξιογράφων στο Χρηματιστήριο.\n\n"
        "*Πινακίδιο* — η αναλυτική κατάσταση "
        "εκτέλεσης μιας εντολής.\n\n"
        "*Εκκαθάριση* — η ολοκλήρωση της "
        "συναλλαγής (Τ+2 εργάσιμες).\n\n"
        "*Περιθώριο* — το ποσό που απαιτείται "
        "ως εγγύηση για θέσεις σε παράγωγα.\n\n"
        "*Σ.Α.Τ.* — Σύστημα Αυλων Τίτλων, "
        "όπου καταγράφονται οι μετοχές σας.\n\n"
        "*Covered call* — πώληση δικαιώματος "
        "αγοράς πάνω σε μετοχές που κατέχετε.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "faq")
def faq(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="📋 Θέματα ημέρας", callback_data="headlines"))
    markup.add(types.InlineKeyboardButton(text="🏛 Περίληψη", callback_data="summary"))
    text = ("❓ *Συχνές ερωτήσεις*\n\n"
        "*Πώς ανοίγω μερίδα;*\n"
        "Αφήνετε στοιχεία, ταυτοποίηση με "
        "ταυτότητα και ΑΦΜ, κατάθεση. "
        "Έτοιμη την επόμενη συνεδρίαση.\n\n"
        "*Τι χρειάζεται;*\n"
        "Ταυτότητα, ΑΦΜ και αποδεικτικό "
        "διεύθυνσης.\n\n"
        "*Πόσο κοστίζει;*\n"
        "Προμήθεια, δικαιώματα και φόρος "
        "αναγράφονται πριν κάθε εντολή. "
        "Χωρίς κρυφές χρεώσεις.\n\n"
        "*Πού είναι τα χρήματα μου;*\n"
        "Σε διακριτό λογαριασμό πελατείας. "
        "Οι τίτλοι στη μερίδα σας στο Σ.Α.Τ.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "contact")
def contact(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.row(types.InlineKeyboardButton(text="🏛 Περίληψη", callback_data="summary"), types.InlineKeyboardButton(text="🏛 Πληροφορίες", callback_data="about"))
    text = ("✏️ *Επικοινωνία*\n\n"
        "Λ. Αλεξάνδρας 29 και Βράιλα\n"
        "114 73 Αθήνα\n\n"
        "Τηλ.: 210 6478900\n\n"
        "Ώρες λειτουργίας:\n"
        "Δευτέρα — Παρασκευή\n"
        "09:00 — 17:30\n"
        "(κατά τη διάρκεια της συνεδρίασης)\n\n"
        "Ελληνικά και αγγλικά.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "about")
def about(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="🏛 Περίληψη", callback_data="summary"), types.InlineKeyboardButton(text="✏️ Επικοινωνία", callback_data="contact"))
    text = ("🏛 *Πληροφορίες*\n\n"
        "Επενδυτική εταιρεία με έδρα την Αθήνα "
        "από το *1995*.\n\n"
        "30 χρόνια στην ελληνική κεφαλαιαγορά. "
        "60+ στελέχη και συνεργάτες.\n\n"
        "Μέλος Χρηματιστηρίου Αθηνών και "
        "Χρηματιστηρίου Αξιών Κύπρου.\n\n"
        "Εποπτεία: Επιτροπή Κεφαλαιαγοράς.\n\n"
        "Μετοχές, παράγωγα και διαχείριση "
        "χαρτοφυλακίου για θεσμικούς, "
        "family offices και ιδιώτες πελάτες.\n\n"
        "_Οι επενδύσεις υπόκεινται σε "
        "κινδύνους αγοράς._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_all(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.add(types.InlineKeyboardButton(text="📋 Θέματα ημέρας", callback_data="headlines"))
    bot.send_message(message.chat.id, "📊 Καλώς ήρθατε! Πατήστε *Θέματα ημέρας* για να ξεκινήσετε.", parse_mode="Markdown", reply_markup=markup)


print("Daily Topics Greece Bot is running...")
bot.infinity_polling()
