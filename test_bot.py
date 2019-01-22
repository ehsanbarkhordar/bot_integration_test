import asyncio

from balebot.models.messages import TemplateMessageButton, TextMessage, TemplateMessage
from balebot.updater import Updater
from balebot.utils.logger import Logger

updater = Updater(token="token", loop=asyncio.get_event_loop())
dispatcher = updater.dispatcher
my_logger = Logger.get_logger()


# =================================== Call Backs =======================================================
def success_send_message(response, user_data):
    kwargs = user_data['kwargs']
    update = kwargs["update"]
    user_peer = update.get_effective_user()
    my_logger.info("success", extra={"user_id": user_peer.peer_id, "tag": "info"})


def failure_send_message(response, user_data):
    kwargs = user_data['kwargs']
    bot = kwargs["bot"]
    message = kwargs["message"]
    update = kwargs["update"]
    try_times = int(kwargs["try_times"])
    if try_times < 5:
        try_times += 1
        user_peer = update.get_effective_user()
        my_logger.error("failure", extra={"user_id": user_peer.peer_id, "tag": "error"})
        kwargs = {"message": message, "update": update, "bot": bot, "try_times": try_times}
        bot.respond(update=update, message=message, success_callback=success_send_message,
                    failure_callback=failure_send_message, kwargs=kwargs)
    else:
        my_logger.error("max tried", extra={"tag": "error"})


@dispatcher.default_handler()
def main_menu(bot, update):
    user_peer = update.get_effective_user()
    btn_list = [TemplateMessageButton(text="a", value="a", action=0),
                TemplateMessageButton(text="b", value="b", action=0),
                TemplateMessageButton(text="c", value="c", action=0)]
    general_message = TextMessage("hahahahahah")
    template_message = TemplateMessage(general_message=general_message, btn_list=btn_list)
    second_kwargs = {"message": template_message, "update": update, "bot": bot, "try_times": 1}
    bot.send_message(template_message, user_peer, success_callback=success_send_message,
                     failure_callback=failure_send_message, kwargs=second_kwargs)


updater.run()
