from pyrogram import filters

from bot.config import Config
from bot.screenshotbot import ScreenShotBot


@ScreenShotBot.on_callback_query(
    filters.create(lambda _, __, query: query.data.startswith("sts_bdct"))
    & filters.user(Config.AUTH_USERS)
)
async def sts_broadcast_(c, cb):

    _, broadcast_id = cb.data.split("+")

    if not c.broadcast_ids.get(broadcast_id):
        await cb.answer(
            text=f"No active broadcast with id {broadcast_id}", show_alert=True
        )
        return

    broadcast_handler = c.broadcast_ids[broadcast_id]
    broadcast_progress = broadcast_handler.get_progress()
    sts_txt = "".join(
        f"{key} = {value}\n" for key, value in broadcast_progress.items()
    )

    await cb.answer(
        text=f"Broadcast Status for {broadcast_id}\n\n{sts_txt}", show_alert=True
    )
