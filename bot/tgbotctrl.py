from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from telegram.ext import  ContextTypes



# ====== TELEGRAM CONTROLLER ======
class TaskListControllerTG:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.model.load_from_file(filename="../data/tasks.json")

    # ---------- MENU ----------
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

    # ---------- BUTTON HANDLER ----------
    async def menu_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        await query.answer()

        action = query.data

        if action == "add":
            context.user_data["state"] = "add_name"
            await query.message.reply_text("Введите название задачи:")

        elif action == "show":
            tasks = self.model.get_all_tasks()
            await query.message.reply_text(self.view.show_tasks(tasks))

        elif action == "do":
            context.user_data["state"] = "do"
            await query.message.reply_text("Введите номер задачи:")

        elif action == "delete":
            context.user_data["state"] = "delete"
            await query.message.reply_text("Введите название задачи:")

        elif action == "sort":
            keyboard = [
                [InlineKeyboardButton("⬆ По возрастанию", callback_data="sort_up")],
                [InlineKeyboardButton("⬇ По убыванию", callback_data="sort_down")]
            ]
            await query.message.reply_text(
                "Выберите сортировку:",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )

        elif action == "save":
            self.model.save_to_file(filename="../data/tasks.json")
            await query.message.reply_text("💾 Задачи сохранены.")

        elif action == "sort_up":
            self.model.sort_by_aura(False)
            await query.message.reply_text("Отсортировано по возрастанию.")

        elif action == "sort_down":
            self.model.sort_by_aura(True)
            await query.message.reply_text("Отсортировано по убыванию.")

    # ---------- TEXT INPUT ----------
    async def text_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        state = context.user_data.get("state")
        text = update.message.text

        if state == "add_name":
            context.user_data["task_name"] = text
            context.user_data["state"] = "add_aura"
            await update.message.reply_text("Введите aura задачи:")

        elif state == "add_aura":
            name = context.user_data["task_name"]
            aura = int(text)
            self.model.add_task(name, aura)
            context.user_data.clear()
            await update.message.reply_text("✅ Задача добавлена!")

        elif state == "do":
            if self.model.DoTask(int(text)):
                await update.message.reply_text("✅ Задача выполнена!")
            else:
                await update.message.reply_text("❌ Задача не найдена!")
            context.user_data.clear()

        elif state == "delete":
            if self.model.delete_task(text):
                await update.message.reply_text("❌ Задача удалена!")
            else:
                await update.message.reply_text("Задача не найдена!")
            context.user_data.clear()



