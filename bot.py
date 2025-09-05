from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler

# 🔑 Token bot Telegram
TOKEN = "8436775076:AAF1rXBlNXCCL0yhip79me45VKOQrF7vDl8"

# 📸 Link ảnh (Dropbox raw link)
IMAGE_URL = "https://www.dropbox.com/scl/fi/zkxacjzn9q2abhmg7jtgt/Photo-5-9-25-08-37-27.jpg?rlkey=x9cmfiazizn217abne1owbpqe&st=zbad83e7&raw=1"


# /start command
def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id

    message = (
        "*Chào mừng bạn đến với BOT bán chứng chỉ tự động!*\n\n"
        "*Thông tin liên hệ hỗ trợ - bảo hành:*\n"
        "• Admin: @lemontree_16\n"
        "• Group Chat: @ipasharing\n\n"
        "*Chấp nhận thanh toán:*\n"
        "• Ngân hàng, momo\n"
        "• Mua bằng thẻ cào nhắn trực tiếp Admin\n\n"
        "Sử dụng các nút trong khung chat bên dưới để tương tác"
    )

    keyboard = [
        [InlineKeyboardButton("Bảng giá chứng chỉ", callback_data="banggia")],
        [InlineKeyboardButton("Khuyến mãi", callback_data="khuyenmai")],
        [InlineKeyboardButton("Hướng dẫn mua hàng", callback_data="huongdan")],
        [InlineKeyboardButton("Tra cứu đơn hàng", callback_data="tracuu")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    context.bot.send_photo(
        chat_id=chat_id,
        photo=IMAGE_URL,
        caption=message,
        parse_mode="Markdown",
        reply_markup=reply_markup,
    )


# Xử lý khi người dùng bấm nút
def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    if query.data == "banggia":
        text = (
            "*Gói 72h - 60K*\n"
            "• Chờ duyệt: 72 - 73h\n"
            "• Hạn sử dụng: 11 - 12 tháng\n"
            "• Bảo hành: Full time\n"
            "Dùng cho ip XS trở lên và iOS 12 trở lên\n\n"
            "*Gói 24h - 120K*\n"
            "• Chờ duyệt: 12 - 24h\n"
            "• Hạn sử dụng: 11 - 12 tháng\n"
            "• Bảo hành: Full time"
        )
        query.edit_message_caption(caption=text, parse_mode="Markdown")

    elif query.data == "khuyenmai":
        query.edit_message_caption(caption="🎁 Hiện chưa có khuyến mãi!", parse_mode="Markdown")

    elif query.data == "huongdan":
        query.edit_message_caption(caption="📌 Hướng dẫn mua hàng sẽ được cập nhật sau.", parse_mode="Markdown")

    elif query.data == "tracuu":
        query.edit_message_caption(caption="🔎 Nhập UDID đơn hàng bạn muốn tra cứu:", parse_mode="Markdown")


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
