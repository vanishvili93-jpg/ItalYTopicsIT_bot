import os
import re
import telebot
from telebot import types

BOT_TOKEN = re.sub(r"\s+", "", os.environ["TELEGRAM_BOT_TOKEN"])
WEB_APP_URL = os.environ.get("WEB_APP_URL", "").strip()

bot = telebot.TeleBot(BOT_TOKEN)

try:
    if WEB_APP_URL:
        bot.set_chat_menu_button(
            menu_button=types.MenuButtonWebApp(
                type="web_app",
                text="Apri Italia Notizie",
                web_app=types.WebAppInfo(url=WEB_APP_URL)
            )
        )
except Exception as e:
    print("Menu button error: " + str(e))


def open_button():
    if WEB_APP_URL:
        return types.InlineKeyboardButton(
            text="📰 Apri Italia Notizie",
            web_app=types.WebAppInfo(url=WEB_APP_URL)
        )
    return types.InlineKeyboardButton(
        text="📰 Apri Italia Notizie",
        url="https://www.ansa.it"
    )


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(
        types.InlineKeyboardButton(
            text="📋 I titoli del giorno",
            callback_data="headlines"
        ),
        types.InlineKeyboardButton(
            text="🏛 Sommario",
            callback_data="sommario"
        )
    )
    text = (
        "📰 *Benvenuti su Italia Notizie.*\n\n"
        "_L informazione e un diritto di tutti._\n\n"
        "Ogni giorno una selezione di cultura, viaggi, "
        "cucina, scienza e sport, da leggere in chat "
        "con calma.\n\n"
        "Per cominciare, toccate *I titoli del giorno*."
    )
    bot.send_message(
        message.chat.id, text,
        parse_mode="Markdown", reply_markup=markup
    )


@bot.callback_query_handler(func=lambda call: call.data == "headlines")
def headlines(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(
            text="🎨 Cultura — mostre d autunno",
            callback_data="culture"
        ),
        types.InlineKeyboardButton(
            text="🍝 Cucina — ricette regionali",
            callback_data="cuisine"
        ),
        types.InlineKeyboardButton(
            text="🏠 Viaggi — cinque borghi",
            callback_data="travel"
        ),
        types.InlineKeyboardButton(
            text="🏛 Sommario",
            callback_data="sommario"
        )
    )
    text = (
        "📋 *I titoli del giorno*\n\n"
        "Tre letture scelte per oggi. "
        "Ognuna leggibile per intero in chat.\n\n"
        "*Cultura* — mostre d autunno: cinque appuntamenti "
        "da non perdere nei musei italiani.\n\n"
        "*Cucina* — ricette regionali: quattro piatti classici "
        "della tradizione italiana.\n\n"
        "*Viaggi* — cinque borghi italiani da scoprire "
        "nei fine settimana d autunno.\n\n"
        "Toccate un titolo per aprire l articolo completo."
    )
    bot.send_message(
        call.message.chat.id, text,
        parse_mode="Markdown", reply_markup=markup
    )


@bot.callback_query_handler(func=lambda call: call.data == "culture")
def culture(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(
        types.InlineKeyboardButton(
            text="📋 I titoli del giorno",
            callback_data="headlines"
        ),
        types.InlineKeyboardButton(
            text="🏛 Sommario",
            callback_data="sommario"
        )
    )
    text = (
        "🎨 *Mostre d autunno: cinque appuntamenti "
        "nei musei italiani*\n\n"
        "I musei riaprono con la nuova stagione. "
        "Cinque appuntamenti che meritano attenzione.\n\n"
        "*Roma — arte del Novecento*\n"
        "Una grande retrospettiva presso una delle gallerie "
        "nazionali raccoglie opere di alcuni fra i maggiori "
        "pittori italiani del secolo scorso. Accanto ai dipinti, "
        "materiali d archivio e fotografie inedite.\n\n"
        "*Milano — design e industria*\n"
        "Una mostra dedicata al design industriale italiano "
        "ripercorre sessant anni di oggetti quotidiani, "
        "dalla lampada da tavolo alla macchina da scrivere. "
        "Catalogo particolarmente curato.\n\n"
        "*Firenze — disegno rinascimentale*\n"
        "Fogli e taccuini di grandi maestri esposti in dialogo "
        "con opere contemporanee ispirate alla stessa tradizione. "
        "Occasione rara per vedere disegni normalmente "
        "conservati in deposito.\n\n"
        "*Napoli — fotografia del secondo dopoguerra*\n"
        "Un percorso di reportage in bianco e nero racconta "
        "la citta e il Sud negli anni della ricostruzione. "
        "Sguardo empatico e documentario insieme.\n\n"
        "*Torino — scultura contemporanea*\n"
        "Il museo cittadino ospita nuove installazioni "
        "negli spazi aperti del parco. Le opere, dedicate "
        "al tema dell acqua, dialogano particolarmente bene "
        "con la luce d autunno.\n\n"
        "_Date e orari vanno verificati sui siti ufficiali._"
    )
    bot.send_message(
        call.message.chat.id, text,
        parse_mode="Markdown", reply_markup=markup
    )


@bot.callback_query_handler(func=lambda call: call.data == "cuisine")
def cuisine(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(
        types.InlineKeyboardButton(
            text="📋 I titoli del giorno",
            callback_data="headlines"
        ),
        types.InlineKeyboardButton(
            text="🏛 Sommario",
            callback_data="sommario"
        )
    )
    text = (
        "🍝 *Ricette regionali: quattro piatti classici*\n\n"
        "La cucina italiana e un patrimonio di sapori regionali. "
        "Quattro ricette per riscoprire la tradizione.\n\n"
        "*Cacio e pepe (Lazio)*\n"
        "Tonnarelli, pecorino romano e pepe nero. La semplicita "
        "che richiede maestria: la crema si ottiene amalgamando "
        "il formaggio con l acqua di cottura. Nient altro.\n\n"
        "*Pesto alla genovese (Liguria)*\n"
        "Basilico di Pra, pinoli, aglio, parmigiano, pecorino "
        "e olio extravergine. Pestato nel mortaio, mai frullato. "
        "Servire con trofie o trenette.\n\n"
        "*Arancini (Sicilia)*\n"
        "Riso al ragu, impanato e fritto. La forma cambia "
        "da citta a citta — tonda a Palermo, a punta a Catania. "
        "Il cuore di mozzarella filante e obbligatorio.\n\n"
        "*Ribollita (Toscana)*\n"
        "Zuppa di pane raffermo, cavolo nero, fagioli cannellini "
        "e verdure dell orto. Si prepara il giorno prima e si "
        "ribollisce — da qui il nome. Comfort food toscano.\n\n"
        "_Dosi e tempi si adattano al gusto personale._"
    )
    bot.send_message(
        call.message.chat.id, text,
        parse_mode="Markdown", reply_markup=markup
    )


@bot.callback_query_handler(func=lambda call: call.data == "travel")
def travel(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(
        types.InlineKeyboardButton(
            text="📋 I titoli del giorno",
            callback_data="headlines"
        ),
        types.InlineKeyboardButton(
            text="🏛 Sommario",
            callback_data="sommario"
        )
    )
    text = (
        "🏠 *Cinque borghi italiani per l autunno*\n\n"
        "Lontano dalle mete piu affollate, cinque piccoli borghi "
        "che in autunno mostrano il loro lato migliore.\n\n"
        "*Civita di Bagnoregio (Lazio)*\n"
        "Il borgo sospeso sul tufo raggiunto solo tramite "
        "un lungo ponte pedonale. Le luci d autunno accentuano "
        "i colori della roccia. Meglio visitarlo in settimana.\n\n"
        "*Bobbio (Emilia-Romagna)*\n"
        "Sull antica via Francigena, con la sua abbazia e il ponte "
        "medievale detto del diavolo. Osterie tranquille per "
        "una sosta di mezza giornata.\n\n"
        "*Volpaia (Toscana)*\n"
        "Piccolo borgo del Chianti, quasi interamente restaurato. "
        "Le vigne intorno cambiano colore in fretta e le cantine "
        "offrono degustazioni discrete.\n\n"
        "*Castelmezzano (Basilicata)*\n"
        "Fra le Dolomiti Lucane, con le case appoggiate a picchi "
        "di roccia. Sentieri di crinale per gli amanti del trekking. "
        "Ottima cucina montana.\n\n"
        "*Erice (Sicilia)*\n"
        "Sospeso in alto sul mare, spesso avvolto nella nebbia "
        "autunnale. Pasticcerie storiche, chiese normanne e vicoli "
        "lastricati. Una tappa che rimane nella memoria.\n\n"
        "_Per il pernottamento si consiglia la prenotazione._"
    )
    bot.send_message(
        call.message.chat.id, text,
        parse_mode="Markdown", reply_markup=markup
    )


@bot.callback_query_handler(func=lambda call: call.data == "sommario")
def sommario(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.add(
        types.InlineKeyboardButton(
            text="📋 I titoli del giorno",
            callback_data="headlines"
        )
    )
    markup.row(
        types.InlineKeyboardButton(
            text="📖 Glossario",
            callback_data="glossario"
        ),
        types.InlineKeyboardButton(
            text="❓ Domande frequenti",
            callback_data="faq"
        )
    )
    markup.row(
        types.InlineKeyboardButton(
            text="✏️ Contatti",
            callback_data="contact"
        ),
        types.InlineKeyboardButton(
            text="🏛 Informazioni",
            callback_data="about"
        )
    )
    text = (
        "🏛 *Sommario*\n\n"
        "Da questo menu potete:\n\n"
        "• Leggere *i titoli del giorno* e i nostri articoli.\n"
        "• Consultare le rubriche: Cultura, Viaggi, Cucina, "
        "Scienza, Sport.\n"
        "• Sfogliare il glossario e le domande frequenti.\n"
        "• Conoscere Italia Notizie e contattare la redazione.\n\n"
        "Per l edizione integrale, usate il pulsante qui sotto."
    )
    bot.send_message(
        call.message.chat.id, text,
        parse_mode="Markdown", reply_markup=markup
    )


@bot.callback_query_handler(func=lambda call: call.data == "glossario")
def glossario(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(
            text="📋 I titoli del giorno",
            callback_data="headlines"
        )
    )
    markup.add(
        types.InlineKeyboardButton(
            text="🏛 Sommario",
            callback_data="sommario"
        )
    )
    text = (
        "📖 *Piccolo glossario*\n\n"
        "Alcuni termini ricorrenti in queste rubriche:\n\n"
        "*Redazione* — squadra che raccoglie, seleziona "
        "e prepara i testi per la pubblicazione.\n\n"
        "*Fondo* — articolo di riflessione, spesso firmato, "
        "che apre una sezione o una pagina.\n\n"
        "*Fotoreportage* — servizio giornalistico costruito "
        "attorno a una serie di fotografie.\n\n"
        "*Contenuto evergreen* — testo la cui attualita "
        "non dipende da una notizia del giorno.\n\n"
        "*Inviato* — giornalista che raccoglie notizie "
        "sul campo.\n\n"
        "*Rubrica* — sezione ricorrente dedicata a un "
        "tema specifico.\n\n"
        "_Termini usati secondo l uso corrente "
        "del giornalismo italiano._"
    )
    bot.send_message(
        call.message.chat.id, text,
        parse_mode="Markdown", reply_markup=markup
    )


@bot.callback_query_handler(func=lambda call: call.data == "faq")
def faq(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(
            text="📋 I titoli del giorno",
            callback_data="headlines"
        )
    )
    markup.add(
        types.InlineKeyboardButton(
            text="🏛 Sommario",
            callback_data="sommario"
        )
    )
    text = (
        "❓ *Domande frequenti*\n\n"
        "*Questo bot e ufficiale?*\n"
        "Italia Notizie e un progetto editoriale "
        "indipendente. I contenuti sono curati dalla "
        "redazione.\n\n"
        "*Con che frequenza si aggiorna?*\n"
        "La selezione in chat viene rinnovata "
        "stagionalmente. Per l edizione aggiornata "
        "usate il pulsante di apertura.\n\n"
        "*Come si silenziano le notifiche?*\n"
        "Dalle impostazioni della chat Telegram potete "
        "silenziare le notifiche di questo bot.\n\n"
        "*Posso condividere un articolo?*\n"
        "Si. Usate le opzioni di condivisione integrate "
        "in Telegram per inoltrare il messaggio."
    )
    bot.send_message(
        call.message.chat.id, text,
        parse_mode="Markdown", reply_markup=markup
    )


@bot.callback_query_handler(func=lambda call: call.data == "contact")
def contact(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.row(
        types.InlineKeyboardButton(
            text="🏛 Sommario",
            callback_data="sommario"
        ),
        types.InlineKeyboardButton(
            text="🏛 Informazioni",
            callback_data="about"
        )
    )
    text = (
        "✏️ *Contatti redazione*\n\n"
        "Per la corrispondenza editoriale:\n"
        "• E-mail: redazione@italianotizie.it\n\n"
        "*Editore*\n"
        "Italia Notizie S.r.l.\n"
        "Via della Conciliazione, 10\n"
        "00193 Roma\n"
        "Italia\n\n"
        "Segnalazioni e osservazioni dei lettori sono "
        "gestiti dalla redazione nei giorni lavorativi."
    )
    bot.send_message(
        call.message.chat.id, text,
        parse_mode="Markdown", reply_markup=markup
    )


@bot.callback_query_handler(func=lambda call: call.data == "about")
def about(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(
        types.InlineKeyboardButton(
            text="🏛 Sommario",
            callback_data="sommario"
        ),
        types.InlineKeyboardButton(
            text="✏️ Contatti",
            callback_data="contact"
        )
    )
    text = (
        "🏛 *Informazioni su Italia Notizie*\n\n"
        "Italia Notizie e un progetto editoriale "
        "indipendente dedicato alla cultura, ai viaggi, "
        "alla cucina e alla tecnologia italiana.\n\n"
        "La redazione seleziona ogni giorno contenuti "
        "di qualita per offrire ai lettori una pausa "
        "informata dalla routine quotidiana.\n\n"
        "Questa versione Telegram e pensata per rendere "
        "piu comoda la lettura dei contenuti evergreen "
        "dall interfaccia di chat."
    )
    bot.send_message(
        call.message.chat.id, text,
        parse_mode="Markdown", reply_markup=markup
    )


@bot.message_handler(func=lambda message: True)
def handle_all(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.add(
        types.InlineKeyboardButton(
            text="📋 I titoli del giorno",
            callback_data="headlines"
        )
    )
    bot.send_message(
        message.chat.id,
        "📰 Benvenuti! Toccate *I titoli del giorno* "
        "per cominciare.",
        parse_mode="Markdown",
        reply_markup=markup
    )


print("Italia Notizie Bot is running...")
bot.infinity_polling()
