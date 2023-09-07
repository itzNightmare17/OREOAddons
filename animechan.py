# OreO

"""
Fetch Random anime quotes

Command : `{i}aniquote`
"""

from . import oreo_cmd, async_searcher


@oreo_cmd(pattern="aniquote")
async def _(ore):
    u = await ore.eor("...")
    try:
        resp = await async_searcher(
            "https://animechan.vercel.app/api/random", re_json=True
        )
        results = f"**{resp['quote']}**\n"
        results += f" — __{resp['character']} ({resp['anime']})__"
        return await u.edit(results)
    except Exception:
        await u.edit("`Something went wrong LOL ...`")
