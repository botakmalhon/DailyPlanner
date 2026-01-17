from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from telegram.ext import  ContextTypes



# ====== VIEW ======
class TgBotView:
    def __init__(self, tg_bot):
        self.tg_bot = tg_bot
    
        
        
    def show_tasks(self, tasks):
        if not tasks:
            return "Задач нет."
        else:
            text = ""
            for i, t in enumerate(tasks, 1):
                text += f"{i}. {t.name} | aura: {t.aura} | done: {t.done}\n"
            return text
    
    def ask_task_name(self, message):
        return input(message)

    def ask_task_num(self, message):
        return int(input(message))

    def ask_task_aura(self):
        while True:
            try:
                return int(input("Введите ауру задачи: "))
            except ValueError:
                print("Введите число!")


    def ask_sort_order(self):
        print("\nКак сортировать по ауре?")
        print("1. По возрастанию")
        print("2. По убыванию")
        return input("Ваш выбор: ")

    def show_message(self, message):
        print(message)

    def show_menu(self):
        self.start()

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        keyboard = [
            [InlineKeyboardButton("➕ Добавить задачу", callback_data="add")],
            [InlineKeyboardButton("📋 Показать задачи", callback_data="show")],
            [InlineKeyboardButton("✅ Выполнить задачу", callback_data="do")],
            [InlineKeyboardButton("❌ Удалить задачу", callback_data="delete")],
            [InlineKeyboardButton("🔃 Сортировать", callback_data="sort")],
            [InlineKeyboardButton("💾 Сохранить", callback_data="save")]
        ]
        await update.message.reply_text(
            "📌 *Меню задач*",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
        )
