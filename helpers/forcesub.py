# (c) @AbirHasan2005

import asyncio
from configs import Config
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


async def ForceSub(bot: Client, cmd: Message):
    try:
        invite_link = await bot.create_chat_invite_link(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL))
    except FloodWait as e:
        await asyncio.sleep(e.x)
        invite_link = await bot.create_chat_invite_link(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL))
    except Exception as err:
        print(f"Unable to do Force Subscribe to {Config.UPDATES_CHANNEL}\n\nError: {err}")
        return 200
    try:
        user = await bot.get_chat_member(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL), user_id=cmd.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=cmd.from_user.id,
                text="ѕσяяу ѕση, уσυ αяє вαηηє∂ тσ υѕє мє. Contact my [ѕυρρσят gяσυρ](https://t.me/Dads_links).",
                parse_mode="markdown",
                disable_web_page_preview=True
            )
            return 400
    except UserNotParticipant:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="**ρℓєαѕє ʝσιη му υρ∂αтєѕ ¢нαηηєℓ тσ υѕє тнιѕ вσт!**\n\nDue to Overload, Only Channel Subscribers can use the Bot!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🤖 ʝσιη υρ∂αтєѕ ¢нαηηєℓ", url=invite_link.invite_link)
                    ],
                    [
                        InlineKeyboardButton("🔄 яєƒяєѕн 🔄", callback_data="refreshFsub")
                    ]
                ]
            ),
            parse_mode="markdown"
        )
        return 400
    except Exception:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="ѕσмєтнιηg ωєηт ωяσηg. Contact my [ѕυρρσят gяσυρ](https://t.me/Dads_links).",
            parse_mode="markdown",
            disable_web_page_preview=True
        )
        return 400
    return 200
