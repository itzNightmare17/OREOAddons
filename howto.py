# oreo


"""
✘ Commands Available -

• `{i}htg <text>`
   How To Google.
   Some peoples don't know how to google so help them 🙃🙂.

• `{i}htd <text>`
   How to duck duck go...
"""


from . import oreo_cmd, async_searcher


API = {"g": "lmgtfy.com/?q={}%26iie=1", "d": "lmddgtfy.net/?q={}"}


@oreo_cmd(pattern="ht(g|d)( ?(.*)|$)")
async def _(e):
    key = e.pattern_match.group(1)
    text = e.pattern_match.group(2)
    if not text:
        return await e.eor("`Give some text`", time=5)
    url = "https://da.gd/s?url=https://" + API[key].format(text.replace(" ", "+"))
    response = await async_searcher(url)
    if response:
        return await e.eor(
            "[{}]({})\n`Thank me Later 🙃` ".format(text, response.rstrip()), time=8
        )
    await e.eor("`something is wrong. please try again later.`")
