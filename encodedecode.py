# OreO


"""
✘ Commands Available -

• {i}encode <text/reply to message>
    encode the text

 • {i}decode <text/reply to message>
    decode the text
"""

import base64

from . import oreo_cmd


@oreo_cmd(pattern="encode ?(.*)")
async def encod(e):
    match = e.pattern_match.group(1)
    if not match and e.is_reply:
        gt = await e.get_reply_message()
        if gt.text:
            match = gt.text
    if not (match or e.is_reply):
        return await e.eor("`Give me Something to Encode..`")
    byt = match.encode("ascii")
    et = base64.b64encode(byt)
    atc = et.decode("ascii")
    await e.eor(f"**=>> Encoded Text :** `{match}`\n\n**=>> OUTPUT :**\n`{atc}`")


@oreo_cmd(pattern="decode ?(.*)")
async def encod(e):
    match = e.pattern_match.group(1)
    if not match and e.is_reply:
        gt = await e.get_reply_message()
        if gt.text:
            match = gt.text
    if not (match or e.is_reply):
        return await e.eor("`Give me Something to Decode..`")
    byt = match.encode("ascii")
    try:
        et = base64.b64decode(byt)
        atc = et.decode("ascii")
        await e.eor(f"**=>> Decoded Text :** `{match}`\n\n**=>> OUTPUT :**\n`{atc}`")
    except Exception as p:
        await e.eor("**ERROR :** " + str(p))
