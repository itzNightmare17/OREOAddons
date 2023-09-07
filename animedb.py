# Oreo


"""
Search animes and manga from anilist.co using @animedb_bot

✘ Commands Available

• `{i}manga <keyword>`
    To get manga info
"""


from . import *


@oreo_cmd(
    pattern="manga ?(.*)",
)
async def manga(ore):
    msg = await ore.eor("`Searching ...`")
    keyword = ore.pattern_match.group(1)
    if keyword is None:
        return await msg.edit("`Provide a Keyword to search`")
    try:
        animes = await ore.client.inline_query("animedb_bot", f"<m> {keyword}")
        await animes[0].click(
            ore.chat_id,
            reply_to=ore.reply_to_msg_id,
            silent=True if ore.is_reply else False,
            hide_via=True,
        )
        return await msg.delete()
    except Exception:
        return await msg.edit("`No Results Found ...`")
