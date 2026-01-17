import config
from app.models import TaskList
from app.views import TaskListView
# from app.controllers import TaskListController
from bot.tgbotctrl import TaskListControllerTG
from app.tg_bot_view import TgBotView

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters
)

TOKEN = config.TOKEN



model = TaskList()
Tg_bot_view = TgBotView()
# cliview = TaskListView()
# controller = TaskListController(model, view)
# controller.run()


app = ApplicationBuilder().token(TOKEN).build()

controller = TaskListControllerTG(model, Tg_bot_view)

app.add_handler(CommandHandler("start", controller.start))
app.add_handler(CallbackQueryHandler(controller.menu_handler))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, controller.text_handler))

app.run_polling()



#TODO
#Переписать модули по MVC (отделить UI от controller)
#Убрать кнопку сортировки (задачи должны быть отсортированы по умолчанию)
#Убрать кнопку сохранения (задачи должны быть сохранены при удалении/добавлении)
#Переделать вывод задач (Каждая задача отдельное сообщение)
#выводить все задачи в кнопках при удалении  
#unique list for each user 


#DONE
## Построить структуру проекта