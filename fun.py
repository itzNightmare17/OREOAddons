# oreo


"""
✘ Commands Available

• `{i}joke`
    To get joke.

• `{i}url <long url>`
    To get a shorten link of long link.

• `{i}phlogo <first_name> <last_name>`
    Make a phub based logo.

• `{i}decide`
    Decide something.

• `{i}xo`
    Opens tic tac game only where using inline mode is allowed.

• `{i}wordi`
    Opens word game only where using inline mode is allowed.

• `{i}gps <name of place>`
    Shows the desired place in the map.
"""

import random, os

import requests
from bs4 import BeautifulSoup as bs
from pyjokes import get_joke
from telethon.errors import ChatSendMediaForbiddenError
from phlogo import generate

from . import oreo_cmd, get_string, HNDLR, async_searcher


@oreo_cmd(pattern="joke$")
async def _(ore):
    await ore.eor(get_joke())


@oreo_cmd(pattern="url ?(.*)")
async def _(event):
    input_str = event.pattern_match.group(1)
    if not input_str:
        await event.eor("`Give some url`")
        return
    sample_url = "https://da.gd/s?url={}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await event.eor(
            "**Shortened url**==> {}\n**Given url**==> {}.".format(
                response_api, input_str
            ),
        )
    else:
        await event.eor("`Something went wrong. Please try again Later.`")


@oreo_cmd(pattern="decide$")
async def _(event):
    hm = await event.eor("`Deciding`")
    r = await async_searcher("https://yesno.wtf/api", re_json=True)
    try:
        await event.reply(r["answer"], file=r["image"])
        await hm.delete()
    except ChatSendMediaForbiddenError:
        await event.eor(r["answer"])


@oreo_cmd(pattern="xo$")
async def xo(ore):
    xox = await ore.client.inline_query("xobot", "play")
    await xox[random.randrange(0, len(xox) - 1)].click(
        ore.chat_id, reply_to=ore.reply_to_msg_id, silent=True, hide_via=True
    )
    await ore.delete()


@oreo_cmd(pattern="phlogo( (.*)|$)")
async def make_logog(ore):
    msg = await ore.eor(get_string("com_1"))
    match = ore.pattern_match.group(1).strip()
    reply = await ore.get_reply_message()
    if not match and (reply and reply.text):
        match = reply.text
    else:
        return await msg.edit(f"`Provide a name to make logo...`")
    first, last = "", ""
    if len(match.split()) >= 2:
        first, last = match.split()[:2]
    else:
        last = match
    logo = generate(first, last)
    name = f"{ore.id}.png"
    logo.save(name)
    await ore.client.send_message(
        ore.chat_id, file=name, reply_to=ore.reply_to_msg_id or ore.id
    )
    os.remove(name)
    await msg.delete()


Bot = {"gps":"openmap_bot", "wordi":"wordibot"}

@oreo_cmd(pattern="(gps|wordi) (.*)")
async def _map(ore):
    cmd = ore.pattern_match.group(1)
    get = ore.pattern_match.group(2)
    if not get:
        return await ore.eor(f"Use this command as `{HNDLR}{cmd} <query>`")
    quer = await ore.client.inline_query(Bot[cmd], get)
    await quer[0].click(
        ore.chat_id, reply_to=ore.reply_to_msg_id, silent=True, hide_via=True
    )
    await ore.delete()
