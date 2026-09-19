import os
import re
import telebot
from telebot import types

BOT_TOKEN = re.sub(r"\s+", "", os.environ["TELEGRAM_BOT_TOKEN"])
WEB_APP_URL = os.environ.get("WEB_APP_URL", "").strip()

bot = telebot.TeleBot(BOT_TOKEN)

    # ============================================
    # ЭКРАН 1 — START (Welcome)
    # ============================================
    @bot.message_handler(commands=['start'])
    def start(message):
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn_open = types.InlineKeyboardButton(
            text="📰 Ανοίξτε το SKAI",
            web_app=types.WebAppInfo(url=WEB_APP_URL)
        )
        btn_headlines = types.InlineKeyboardButton(
            text="📋 Τα νέα της ημέρας",
            callback_data="headlines"
        )
        btn_sommario = types.InlineKeyboardButton(
            text="🏛 Περίληψη",
            callback_data="sommario"
        )
        markup.add(btn_open)
        markup.row(btn_headlines, btn_sommario)

        text = (
            "📰 **Καλώς ήρθατε στο SKAI.**\n\n"
            "_«Η ενημέρωση είναι ο καθημερινός διάλογος με τους αναγνώστες μας.»_\n\n"
            "Από το **1993**, αυτός ο διάλογος συνεχίζεται — στην τηλεόραση, στο διαδίκτυο, "
            "και σήμερα εδώ στο Telegram. Κάθε εποχή μια μικρή επιλογή από πολιτισμό, "
            "ταξίδια, κουζίνα, επιστήμη και αθλητικά, για ανάγνωση με ηρεμία στο chat.\n\n"
            "Για να ξεκινήσετε, πατήστε **Τα νέα της ημέρας**."
        )

        bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


    # ============================================
    # ЭКРАН 2 — HEADLINES (Τα νέα της ημέρας)
    # ============================================
    @bot.callback_query_handler(func=lambda call: call.data == "headlines")
    def headlines(call):
        bot.answer_callback_query(call.id)
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text="🎨 Πολιτισμός — εκθέσεις φθινοπώρου", callback_data="culture")
        btn2 = types.InlineKeyboardButton(text="🍳 Κουζίνα — συνταγές με κυδώνι", callback_data="cuisine")
        btn3 = types.InlineKeyboardButton(text="🏠 Ταξίδια — πέντε χωριά", callback_data="travel")
        btn4 = types.InlineKeyboardButton(text="🏛 Περίληψη", callback_data="sommario")
        markup.add(btn1, btn2, btn3, btn4)

        text = (
            "📋 **Τα νέα της ημέρας**\n\n"
            "Τρία κείμενα επιλεγμένα για σήμερα. Κάθε ένα ολόκληρο στο chat.\n\n"
            "**Πολιτισμός** — εκθέσεις φθινοπώρου: πέντε ραντεβού που αξίζουν "
            "στα ελληνικά μουσεία.\n\n"
            "**Κουζίνα** — η εποχή του κυδωνιού: τέσσερις κλασικές "
            "συνταγές της ελληνικής παράδοσης.\n\n"
            "**Ταξίδια** — πέντε ελληνικά χωριά για να ανακαλύψετε "
            "τα φθινοπωρινά Σαββατοκύριακα.\n\n"
            "Πατήστε έναν τίτλο για να ανοίξετε το πλήρες κείμενο."
        )

        bot.send_message(call.message.chat.id, text,
                         parse_mode="Markdown", reply_markup=markup)


    # ============================================
    # ЭКРАН 3 — CULTURE (Πολιτισμός)
    # ============================================
    @bot.callback_query_handler(func=lambda call: call.data == "culture")
    def culture(call):
        bot.answer_callback_query(call.id)
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn_open = types.InlineKeyboardButton(
            text="📰 Ανοίξτε το SKAI",
            web_app=types.WebAppInfo(url=WEB_APP_URL)
        )
        btn_headlines = types.InlineKeyboardButton(text="📋 Τα νέα της ημέρας", callback_data="headlines")
        btn_sommario = types.InlineKeyboardButton(text="🏛 Περίληψη", callback_data="sommario")
        markup.add(btn_open)
        markup.row(btn_headlines, btn_sommario)

        text = (
            "🎨 **Εκθέσεις φθινοπώρου: πέντε ραντεβού στα ελληνικά μουσεία**\n\n"
            "Τα μουσεία ανοίγουν ξανά με νέα σεζόν. Πέντε ραντεβού "
            "που αξίζουν την προσοχή σας αυτό το φθινόπωρο.\n\n"
            "**Αθήνα — τέχνη του 20ού αιώνα**\n"
            "Μια μεγάλη αναδρομική στην Εθνική Πινακοθήκη συγκεντρώνει "
            "έργα κορυφαίων Ελλήνων ζωγράφων. Δίπλα στους πίνακες, "
            "αρχειακό υλικό και αδημοσίευτες φωτογραφίες.\n\n"
            "**Θεσσαλονίκη — βυζαντινή κληρονομιά**\n"
            "Το Μουσείο Βυζαντινού Πολιτισμού παρουσιάζει ψηφιδωτά "
            "και εικόνες σε έναν διάλογο ανάμεσα στο παλιό και το νέο. "
            "Μοναδική ευκαιρία.\n\n"
            "**Ηράκλειο — μινωικός πολιτισμός**\n"
            "Νέα ευρήματα από τις ανασκαφές στην Κνωσό εκτίθενται "
            "για πρώτη φορά. Η έκθεση αποκαλύπτει πτυχές της "
            "καθημερινής ζωής πριν 3.500 χρόνια.\n\n"
            "**Ναύπλιο — φωτογραφία νεοελληνικής ιστορίας**\n"
            "Ασπρόμαυρα ρεπορτάζ αφηγούνται την πόλη και την Πελοπόννησο "
            "στα χρόνια της ανασυγκρότησης. Ντοκουμεντάρικο και ποιητικό.\n\n"
            "**Ιωάννινα — σύγχρονη γλυπτική**\n"
            "Το Δημοτικό Μουσείο φιλοξενεί νέες εγκαταστάσεις στους "
            "υπαίθριους χώρους δίπλα στη λίμνη. Τα έργα, αφιερωμένα "
            "στο νερό, αρμονούν με το φθινοπωρινό φως.\n\n"
            "_Ημερομηνίες και ωράρια στους επίσημους ιστότοπους των μουσείων._"
        )

        bot.send_message(call.message.chat.id, text,
                         parse_mode="Markdown", reply_markup=markup)


    # ============================================
    # ЭКРАН 4 — CUISINE (Κουζίνα)
    # ============================================
    @bot.callback_query_handler(func=lambda call: call.data == "cuisine")
    def cuisine(call):
        bot.answer_callback_query(call.id)
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn_open = types.InlineKeyboardButton(
            text="📰 Ανοίξτε το SKAI",
            web_app=types.WebAppInfo(url=WEB_APP_URL)
        )
        btn_headlines = types.InlineKeyboardButton(text="📋 Τα νέα της ημέρας", callback_data="headlines")
        btn_sommario = types.InlineKeyboardButton(text="🏛 Περίληψη", callback_data="sommario")
        markup.add(btn_open)
        markup.row(btn_headlines, btn_sommario)

        text = (
            "🍳 **Η εποχή του κυδωνιού: τέσσερις κλασικές συνταγές**\n\n"
            "Το κυδώνι είναι ένα από τα πιο χαρακτηριστικά φρούτα "
            "του ελληνικού φθινοπώρου. Τέσσερις συνταγές για να "
            "αξιοποιήσετε τα καλύτερα.\n\n"
            "**Κυδώνι ψητό στον φούρνο**\n"
            "Κόβετε τα κυδώνια στα τέσσερα, τα βάζετε σε ταψί με ζάχαρη, "
            "κανέλα και γαρίφαλο. Ψήνετε στους 180° για μία ώρα. "
            "Τρώγονται ζεστά ή κρύα.\n\n"
            "**Κυδωνόπαστο**\n"
            "Βράζετε τα κυδώνια μέχρι να μαλακώσουν, τα πολτοποιείτε "
            "με ζάχαρη και χυμό λεμονιού. Στεγνώνει σε χαμηλή θερμοκρασία. "
            "Το κλασικό γλυκό κουταλιού.\n\n"
            "**Κυδώνι με κρέας**\n"
            "Μοσχάρι ή χοιρινό κοκκινιστό με κυδώνια. Κρεμμύδι, "
            "ντομάτα, κανέλα — σιγοβράζει για δύο ώρες. Κλασική "
            "συνταγή της ελληνικής κουζίνας.\n\n"
            "**Μαρμελάδα κυδώνι**\n"
            "Κυδώνια τριμμένα με ζάχαρη, χυμό λεμονιού και βανίλια. "
            "Βράζει μέχρι να πήξει. Ιδανική για πρωινό με βούτυρο και ψωμί.\n\n"
            "_Δοσολογίες και χρόνοι προσαρμόζονται κατά βούληση._"
        )

        bot.send_message(call.message.chat.id, text,
                         parse_mode="Markdown", reply_markup=markup)


    # ============================================
    # ЭКРАН 5 — TRAVEL (Ταξίδια)
    # ============================================
    @bot.callback_query_handler(func=lambda call: call.data == "travel")
    def travel(call):
        bot.answer_callback_query(call.id)
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn_open = types.InlineKeyboardButton(
            text="📰 Ανοίξτε το SKAI",
            web_app=types.WebAppInfo(url=WEB_APP_URL)
        )
        btn_headlines = types.InlineKeyboardButton(text="📋 Τα νέα της ημέρας", callback_data="headlines")
        btn_sommario = types.InlineKeyboardButton(text="🏛 Περίληψη", callback_data="sommario")
        markup.add(btn_open)
        markup.row(btn_headlines, btn_sommario)

        text = (
            "🏠 **Πέντε ελληνικά χωριά για το φθινόπωρο**\n\n"
            "Μακριά από τους δημοφιλείς προορισμούς, πέντε μικρά "
            "χωριά που δείχνουν τον καλύτερο εαυτό τους το φθινόπωρο.\n\n"
            "**Ζαγοροχώρια (Ήπειρος)**\n"
            "Πέτρινα γεφύρια, μονοπάτια μέσα σε φαράγγια και "
            "παραδοσιακοί ξενώνες. Τα χρώματα του φθινοπώρου "
            "κάνουν τη Βίκο αξέχαστη. Καλύτερα τις καθημερινές.\n\n"
            "**Δημητσάνα (Πελοπόννησος)**\n"
            "Χτισμένη σε βουνοπλαγιά πάνω από το φαράγγι του Λούσιου. "
            "Υπαίθριο Μουσείο Υδροκίνησης και ήσυχα καφενεία "
            "με θέα τα πεύκα.\n\n"
            "**Μέτσοβο (Ήπειρος)**\n"
            "Ορεινό κεφαλοχώρι με τυροκομικά και κρασιά. Η πλατεία "
            "ζωντανεύει τα απογεύματα. Το φθινόπωρο η ομίχλη "
            "χαρίζει στο Μέτσοβο ιδιαίτερη ατμόσφαιρα.\n\n"
            "**Μονεμβασιά (Πελοπόννησος)**\n"
            "Η βυζαντινή καστροπολιτεία κρυμμένη πίσω από τον βράχο. "
            "Πλακόστρωτα δρομάκια, εκκλησάκια και θάλασσα. "
            "Το φθινόπωρο χωρίς πλήθη — μαγεία.\n\n"
            "**Νυμφαίο (Μακεδονία)**\n"
            "Ψηλά στο Βίτσι, ένα χωριό που αναστηλώθηκε με σεβασμό. "
            "Αρχοντικά, το καταφύγιο αρκούδων του Αρκτούρου "
            "και απόλυτη ησυχία.\n\n"
            "_Για διαμονή συνιστάται κράτηση εντός εβδομάδας._"
        )

        bot.send_message(call.message.chat.id, text,
                         parse_mode="Markdown", reply_markup=markup)


    # ============================================
    # ЭКРАН 6 — SOMMARIO (Περίληψη)
    # ============================================
    @bot.callback_query_handler(func=lambda call: call.data == "sommario")
    def sommario(call):
        bot.answer_callback_query(call.id)
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn_open = types.InlineKeyboardButton(
            text="📰 Ανοίξτε το SKAI",
            web_app=types.WebAppInfo(url=WEB_APP_URL)
        )
        btn_headlines = types.InlineKeyboardButton(text="📋 Τα νέα της ημέρας", callback_data="headlines")
        btn_glossary = types.InlineKeyboardButton(text="📖 Γλωσσάριο", callback_data="glossary")
        btn_faq = types.InlineKeyboardButton(text="❓ Συχνές ερωτήσεις", callback_data="faq")
        btn_contact = types.InlineKeyboardButton(text="✏️ Επικοινωνία", callback_data="contact")
        btn_about = types.InlineKeyboardButton(text="🏛 Σχετικά με το SKAI", callback_data="about")
        markup.add(btn_open)
        markup.add(btn_headlines)
        markup.row(btn_glossary, btn_faq)
        markup.row(btn_contact, btn_about)

        text = (
            "🏛 **Περίληψη**\n\n"
            "Από αυτό το μενού μπορείτε:\n\n"
            "• Να διαβάσετε **τα νέα της ημέρας** και τα άρθρα μας, "
            "απευθείας εδώ.\n"
            "• Να συμβουλευτείτε τις στήλες: Πολιτισμός, Ταξίδια, "
            "Κουζίνα, Επιστήμη, Αθλητικά, Πρακτική Οικονομία.\n"
            "• Να δείτε το γλωσσάριο και τις συχνές ερωτήσεις.\n"
            "• Να μάθετε την ιστορία του SKAI και να επικοινωνήσετε "
            "με τη σύνταξη.\n\n"
            "Για την πλήρη έκδοση, χρησιμοποιήστε το κουμπί ανοίγματος."
        )

        bot.send_message(call.message.chat.id, text,
                         parse_mode="Markdown", reply_markup=markup)


    # ============================================
    # ЭКРАН 7 — GLOSSARY (Γλωσσάριο)
    # ============================================
    @bot.callback_query_handler(func=lambda call: call.data == "glossary")
    def glossary(call):
        bot.answer_callback_query(call.id)
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn_headlines = types.InlineKeyboardButton(text="📋 Τα νέα της ημέρας", callback_data="headlines")
        btn_sommario = types.InlineKeyboardButton(text="🏛 Περίληψη", callback_data="sommario")
        markup.add(btn_headlines)
        markup.add(btn_sommario)

        text = (
            "📖 **Μικρό γλωσσάριο**\n\n"
            "Ορισμένοι όροι που συναντώνται συχνά στις στήλες μας:\n\n"
            "**Σύνταξη** — η ομάδα που συλλέγει, επιλέγει και "
            "προετοιμάζει τα κείμενα για δημοσίευση.\n\n"
            "**Κύριο άρθρο** — άρθρο γνώμης, συχνά υπογεγραμμένο, "
            "που ανοίγει μια ενότητα ή σελίδα.\n\n"
            "**Φωτορεπορτάζ** — δημοσιογραφικό κείμενο χτισμένο "
            "γύρω από μια σειρά φωτογραφιών.\n\n"
            "**Διαχρονικό περιεχόμενο** — κείμενο που δεν εξαρτάται "
            "από μια είδηση της ημέρας: πολιτισμός, ταξίδια, κουζίνα.\n\n"
            "**Απεσταλμένος** — δημοσιογράφος που καλύπτει ειδήσεις "
            "επί τόπου.\n\n"
            "**Στήλη** — μόνιμη ενότητα αφιερωμένη σε ένα "
            "συγκεκριμένο θέμα.\n\n"
            "_Οι όροι χρησιμοποιούνται σύμφωνα με την τρέχουσα "
            "πρακτική της ελληνικής δημοσιογραφίας._"
        )

        bot.send_message(call.message.chat.id, text,
                         parse_mode="Markdown", reply_markup=markup)


    # ============================================
    # ЭКРАН 8 — FAQ (Συχνές ερωτήσεις)
    # ============================================
    @bot.callback_query_handler(func=lambda call: call.data == "faq")
    def faq(call):
        bot.answer_callback_query(call.id)
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn_headlines = types.InlineKeyboardButton(text="📋 Τα νέα της ημέρας", callback_data="headlines")
        btn_sommario = types.InlineKeyboardButton(text="🏛 Περίληψη", callback_data="sommario")
        markup.add(btn_headlines)
        markup.add(btn_sommario)

        text = (
            "❓ **Συχνές ερωτήσεις**\n\n"
            "**Αυτό το bot είναι επίσημο;**\n"
            "Αυτή η έκδοση Telegram σας επιτρέπει να διαβάζετε "
            "στο chat τα διαχρονικά περιεχόμενα του SKAI. "
            "Η επιμέλεια γίνεται από τη σύνταξη· τα στοιχεία "
            "επικοινωνίας βρίσκονται στην ενότητα Επικοινωνία.\n\n"
            "**Πόσο συχνά ενημερώνεται;**\n"
            "Η επιλογή στο chat ανανεώνεται εποχιακά. Για την "
            "ενημερωμένη έκδοση χρησιμοποιήστε το κουμπί ανοίγματος.\n\n"
            "**Πώς σιγάζω τις ειδοποιήσεις;**\n"
            "Από τις ρυθμίσεις του chat στο Telegram μπορείτε να "
            "σιγάσετε ή να απενεργοποιήσετε εντελώς τις ειδοποιήσεις.\n\n"
            "**Μπορώ να μοιραστώ ένα άρθρο;**\n"
            "Ναι. Χρησιμοποιήστε τις επιλογές κοινής χρήσης "
            "του Telegram για να προωθήσετε το μήνυμα σε "
            "άλλο chat ή εφαρμογή."
        )

        bot.send_message(call.message.chat.id, text,
                         parse_mode="Markdown", reply_markup=markup)


    # ============================================
    # ЭКРАН 9 — CONTACT (Επικοινωνία)
    # ============================================
    @bot.callback_query_handler(func=lambda call: call.data == "contact")
    def contact(call):
        bot.answer_callback_query(call.id)
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn_sommario = types.InlineKeyboardButton(text="🏛 Περίληψη", callback_data="sommario")
        btn_about = types.InlineKeyboardButton(text="🏛 Σχετικά με το SKAI", callback_data="about")
        markup.row(btn_sommario, btn_about)

        text = (
            "✏️ **Επικοινωνία σύνταξης**\n\n"
            "Για εκδοτική αλληλογραφία:\n"
            "• E-mail: info@skai.gr\n"
            "• Υπηρεσία αναγνωστών: skai.gr/contact\n\n"
            "**Εκδότης**\n"
            "ΣΚΑΪ Μ.Α.Ε.\n"
            "Φαληρέας & Εθνάρχου Μακαρίου\n"
            "18547 Νέο Φάληρο\n\n"
            "Παρατηρήσεις, διευκρινίσεις και σχόλια αναγνωστών "
            "διαχειρίζεται η υπηρεσία αναγνωστών τις εργάσιμες ημέρες."
        )

        bot.send_message(call.message.chat.id, text,
                         parse_mode="Markdown", reply_markup=markup)


    # ============================================
    # ЭКРАН 10 — ABOUT (Σχετικά με το SKAI)
    # ============================================
    @bot.callback_query_handler(func=lambda call: call.data == "about")
    def about(call):
        bot.answer_callback_query(call.id)
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn_open = types.InlineKeyboardButton(
            text="📰 Ανοίξτε το SKAI",
            web_app=types.WebAppInfo(url=WEB_APP_URL)
        )
        btn_sommario = types.InlineKeyboardButton(text="🏛 Περίληψη", callback_data="sommario")
        btn_contact = types.InlineKeyboardButton(text="✏️ Επικοινωνία", callback_data="contact")
        markup.add(btn_open)
        markup.row(btn_sommario, btn_contact)

        text = (
            "🏛 **Σχετικά με το SKAI**\n\n"
            "_Ο ΣΚΑΪ_ ιδρύθηκε στην Αθήνα το **1993** ως ραδιοφωνικός "
            "σταθμός, και γρήγορα εξελίχθηκε σε ένα από τα μεγαλύτερα "
            "ΜΜΕ στην Ελλάδα. Από την αρχή, ο ΣΚΑΪ καθιερώθηκε ως "
            "ένα αξιόπιστο μέσο ενημέρωσης με ευρεία κάλυψη.\n\n"
            "Σήμερα ο ΣΚΑΪ ανήκει στον **Όμιλο ΣΚΑΪ**, που περιλαμβάνει "
            "τηλεοπτικό κανάλι, ραδιόφωνο και ψηφιακά μέσα. Συνεχίζει "
            "να παράγει περιεχόμενο σε πολιτισμό, ταξίδια, κουζίνα, "
            "επιστήμη, αθλητικά και πρακτική οικονομία.\n\n"
            "Ανάμεσα σε τηλεόραση, ιστοσελίδα και εφαρμογή, ο ΣΚΑΪ "
            "φτάνει καθημερινά εκατομμύρια αναγνώστες. Η έδρα είναι "
            "στο Νέο Φάληρο· ο ιστότοπος είναι skai.gr.\n\n"
            "Αυτή η έκδοση Telegram σχεδιάστηκε για να κάνει πιο "
            "βολική την ανάγνωση διαχρονικών περιεχομένων μέσα "
            "από το chat."
        )

        bot.send_message(call.message.chat.id, text,
                         parse_mode="Markdown", reply_markup=markup)


    # ============================================
    # ЗАПУСК
    # ============================================
    print("SKAI Bot is running...")
    bot.infinity_polling()
