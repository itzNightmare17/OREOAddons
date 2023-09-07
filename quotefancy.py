# oreo


"""
✘ Commands Available

• `{i}qfancy`
    Gets random quotes from QuoteFancy.com.
"""

from telethon.errors import ChatSendMediaForbiddenError

from quotefancy import get_quote

from . import *


@oreo_cmd(pattern="qfancy$")
async def quotefancy(e):
    mes = await e.eor(get_string("com_1"))
    img = get_quote("img", download=True)
    try:
        await e.client.send_file(e.chat_id, img)
        os.remove(img)
        await mes.delete()
    except ChatSendMediaForbiddenError:
        quote = get_quote("text")
        await eor(mes, f"`{quote}`")
    except Exception as err:
        await eor(mes, f"**ERROR** - {err}")
