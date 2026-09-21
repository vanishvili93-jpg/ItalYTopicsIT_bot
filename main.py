import os
import re
import telebot
from telebot import types

BOT_TOKEN = re.sub(r"\s+", "", os.environ["TELEGRAM_BOT_TOKEN"])
WEB_APP_URL = os.environ.get("WEB_APP_URL", "").strip()

bot = telebot.TeleBot(BOT_TOKEN)

try:
    if WEB_APP_URL:
        bot.set_chat_menu_button(menu_button=types.MenuButtonWebApp(type="web_app", text="Abrir", web_app=types.WebAppInfo(url=WEB_APP_URL)))
except Exception as e:
    print("Menu button error: " + str(e))


def open_button():
    if WEB_APP_URL:
        return types.InlineKeyboardButton(text="📰 Abrir Temas del Dia", web_app=types.WebAppInfo(url=WEB_APP_URL))
    return types.InlineKeyboardButton(text="📰 Abrir Temas del Dia", url="https://www.elpais.com")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Los temas del dia", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Resumen", callback_data="summary"))
    text = ("📰 *Bienvenidos a Temas del Dia.*\n\n"
        "_La informacion es un derecho de todos._\n\n"
        "Cada dia una seleccion de cultura, viajes, "
        "cocina, ciencia y deporte, para leer "
        "con calma en el chat.\n\n"
        "Para empezar, pulse *Los temas del dia*.")
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "headlines")
def headlines(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(text="🎨 Cultura — exposiciones de otono", callback_data="culture"),
        types.InlineKeyboardButton(text="🍳 Cocina — recetas regionales", callback_data="cuisine"),
        types.InlineKeyboardButton(text="🏠 Viajes — cinco pueblos", callback_data="travel"),
        types.InlineKeyboardButton(text="🏛 Resumen", callback_data="summary"))
    text = ("📋 *Los temas del dia*\n\n"
        "Tres lecturas elegidas para hoy. "
        "Cada una completa en el chat.\n\n"
        "*Cultura* — exposiciones de otono: cinco "
        "citas imprescindibles en los museos espanoles.\n\n"
        "*Cocina* — recetas regionales: cuatro platos "
        "clasicos de la tradicion espanola.\n\n"
        "*Viajes* — cinco pueblos espanoles para "
        "descubrir en un fin de semana de otono.\n\n"
        "Pulse un titulo para abrir el articulo completo.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "culture")
def culture(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Los temas del dia", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Resumen", callback_data="summary"))
    text = ("🎨 *Exposiciones de otono: cinco citas "
        "en los museos espanoles*\n\n"
        "Los museos reabren con nueva temporada.\n\n"
        "*Madrid — arte del siglo XX*\n"
        "Una gran retrospectiva en el Museo Reina Sofia "
        "reune obras de los principales pintores espanoles "
        "del siglo pasado. Material de archivo y "
        "fotografias ineditas.\n\n"
        "*Barcelona — diseno y arquitectura*\n"
        "El MACBA presenta una exposicion dedicada al "
        "diseno industrial catalan. Sesenta anos de objetos "
        "cotidianos. Catalogo especialmente cuidado.\n\n"
        "*Sevilla — fotografia del sur*\n"
        "El Centro Andaluz de Arte Contemporaneo exhibe "
        "reportajes en blanco y negro sobre Andalucia "
        "en la posguerra. Mirada empatica y documental.\n\n"
        "*Bilbao — escultura contemporanea*\n"
        "El Guggenheim acoge nuevas instalaciones "
        "en los espacios exteriores. Las obras dialogan "
        "con la luz del otono.\n\n"
        "*Valencia — arte fallero*\n"
        "El Museo Fallero muestra bocetos y ninots "
        "restaurados. Una tradicion unica vista "
        "desde el taller del artista.\n\n"
        "_Fechas y horarios en las webs oficiales._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "cuisine")
def cuisine(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Los temas del dia", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Resumen", callback_data="summary"))
    text = ("🍳 *Recetas regionales: cuatro platos clasicos*\n\n"
        "La cocina espanola es patrimonio de "
        "sabores regionales.\n\n"
        "*Paella valenciana*\n"
        "Arroz, pollo, conejo, garrofo, ferraura "
        "y romero. El fuego tiene que ser de lena "
        "y el socarrat es obligatorio. No lleva "
        "chorizo.\n\n"
        "*Pulpo a la gallega*\n"
        "Pulpo cocido, cortado con tijera, "
        "pimenton de la Vera, aceite de oliva "
        "y sal gorda. Se sirve en plato de "
        "madera. Sencillo y perfecto.\n\n"
        "*Gazpacho andaluz*\n"
        "Tomate, pepino, pimiento, ajo, pan "
        "duro, vinagre y aceite. Se tritura "
        "todo y se sirve muy frio. El plato "
        "del verano espanol.\n\n"
        "*Fabada asturiana*\n"
        "Fabes de la Granja, chorizo, morcilla "
        "y lacones. Coccion lenta durante horas. "
        "El plato de cuchara por excelencia.\n\n"
        "_Cantidades y tiempos al gusto personal._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "travel")
def travel(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Los temas del dia", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Resumen", callback_data="summary"))
    text = ("🏠 *Cinco pueblos espanoles para el otono*\n\n"
        "Lejos de los destinos mas concurridos, "
        "cinco pueblos que muestran su mejor "
        "cara en otono.\n\n"
        "*Albarracin (Teruel)*\n"
        "Murallas medievales, calles empinadas "
        "y casas colgadas sobre el rio Guadalaviar. "
        "Los colores del otono lo transforman.\n\n"
        "*Cudillero (Asturias)*\n"
        "Un anfiteatro de casas de colores sobre "
        "el Cantabrico. Sidra, pescado fresco "
        "y calma absoluta.\n\n"
        "*Frigiliana (Malaga)*\n"
        "Pueblo blanco en la Axarquia. Callejuelas "
        "estrechas, buganvillas y vistas al "
        "Mediterraneo. Otono sin frio.\n\n"
        "*Combarro (Pontevedra)*\n"
        "Horreos al borde del mar, cruceiros "
        "de piedra y marisco recien sacado "
        "de la ria. Galicia en estado puro.\n\n"
        "*Ainsa (Huesca)*\n"
        "Plaza Mayor medieval con el Pirineo "
        "de fondo. Senderismo, quesos artesanos "
        "y noches de cielo limpio.\n\n"
        "_Reserva con antelacion en temporada alta._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "summary")
def summary(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.add(types.InlineKeyboardButton(text="📋 Los temas del dia", callback_data="headlines"))
    markup.row(types.InlineKeyboardButton(text="📖 Glosario", callback_data="glossary"), types.InlineKeyboardButton(text="❓ Preguntas frecuentes", callback_data="faq"))
    markup.row(types.InlineKeyboardButton(text="✏️ Contacto", callback_data="contact"), types.InlineKeyboardButton(text="🏛 Informacion", callback_data="about"))
    text = ("🏛 *Resumen*\n\n"
        "Desde este menu puede:\n\n"
        "• Leer *los temas del dia* y nuestros articulos.\n"
        "• Consultar las secciones: Cultura, "
        "Viajes, Cocina, Ciencia.\n"
        "• Ver el glosario y las preguntas frecuentes.\n"
        "• Conocernos y contactar con la redaccion.\n\n"
        "Para la edicion completa, use el boton.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "glossary")
def glossary(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="📋 Los temas del dia", callback_data="headlines"))
    markup.add(types.InlineKeyboardButton(text="🏛 Resumen", callback_data="summary"))
    text = ("📖 *Pequeno glosario*\n\n"
        "*Redaccion* — el equipo que selecciona "
        "y prepara los textos.\n\n"
        "*Editorial* — articulo de opinion que "
        "abre una seccion.\n\n"
        "*Fotorreportaje* — relato periodistico "
        "construido con fotografias.\n\n"
        "*Contenido atemporal* — texto cuya "
        "actualidad no depende de la noticia "
        "del dia.\n\n"
        "*Corresponsal* — periodista que cubre "
        "noticias sobre el terreno.\n\n"
        "*Seccion* — apartado fijo dedicado "
        "a un tema concreto.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "faq")
def faq(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="📋 Los temas del dia", callback_data="headlines"))
    markup.add(types.InlineKeyboardButton(text="🏛 Resumen", callback_data="summary"))
    text = ("❓ *Preguntas frecuentes*\n\n"
        "*Es oficial este bot?*\n"
        "Temas del Dia es un proyecto editorial "
        "independiente.\n\n"
        "*Con que frecuencia se actualiza?*\n"
        "La seleccion se renueva cada temporada.\n\n"
        "*Como silencio las notificaciones?*\n"
        "Desde los ajustes del chat en Telegram.\n\n"
        "*Puedo compartir un articulo?*\n"
        "Si, usando las opciones de compartir "
        "de Telegram.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "contact")
def contact(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.row(types.InlineKeyboardButton(text="🏛 Resumen", callback_data="summary"), types.InlineKeyboardButton(text="🏛 Informacion", callback_data="about"))
    text = ("✏️ *Contacto*\n\n"
        "Para correspondencia editorial:\n"
        "• E-mail: redaccion@temasdeldia.es\n\n"
        "*Editor*\n"
        "Temas del Dia S.L.\n"
        "Gran Via, 32\n"
        "28013 Madrid\n"
        "Espana\n\n"
        "Comentarios y sugerencias de los lectores "
        "en dias laborables.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "about")
def about(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="🏛 Resumen", callback_data="summary"), types.InlineKeyboardButton(text="✏️ Contacto", callback_data="contact"))
    text = ("🏛 *Informacion sobre Temas del Dia*\n\n"
        "Temas del Dia es un proyecto editorial "
        "independiente dedicado a la cultura, "
        "los viajes, la cocina y la tecnologia.\n\n"
        "La redaccion selecciona cada dia contenidos "
        "de calidad para ofrecer a los lectores una "
        "pausa informada.\n\n"
        "Esta edicion de Telegram esta pensada para "
        "facilitar la lectura desde el chat.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_all(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.add(types.InlineKeyboardButton(text="📋 Los temas del dia", callback_data="headlines"))
    bot.send_message(message.chat.id, "📰 Bienvenidos! Pulse *Los temas del dia* para empezar.", parse_mode="Markdown", reply_markup=markup)


print("Temas del Dia Bot is running...")
bot.infinity_polling()
