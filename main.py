from aiogram.utils import executor
import logging

from config import dp

from handler import client, callback, extra, admin, fsm_anketa

client.reg_client(dp)
callback.reg_call_back(dp)
admin.reg_hand_admin(dp)
fsm_anketa.reg_hand_anketa(dp)
extra.reg_handler_extra(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
