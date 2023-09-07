# oreo


"""
✘ Commands Available -

• `{i}limited`
   Check you are limited or not !
"""

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from . import oreo_cmd


@oreo_cmd(pattern="limited$")
async def demn(ore):
    chat = "@SpamBot"
    msg = await ore.eor("Checking If You Are Limited...")
    async with ore.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=178220800)
            )
            await conv.send_message("/start")
            response = await response
            await ore.client.send_read_acknowledge(chat)
        except YouBlockedUserError:
            await msg.edit("Boss! Please Unblock @SpamBot ")
            return
        await msg.edit(f"~ {response.message.message}")
