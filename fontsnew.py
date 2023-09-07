# oreo


"""
✘ Commands Available -

• `{i}weeb <text>`
    turns text to 山乇乇乃 font

• `{i}tantext <text>`
    turns text to ᎿᎯᏁᎿᏋﾒᎿ font

• `{i}linetext <text>`
    turns text to 𝕃𝕀ℕ𝔼𝕋𝔼𝕏𝕋

• `{i}boxtext <text>`
    turns text to 🄱🄾🅇🅃🄴🅇🅃

• `{i}bubbletext <text>`
    turns text to ⒷⓊⒷⒷⓁⒺⓉⒺⓍⓉ

• `{i}cursive <text>`
    turns text to 𝓬𝓾𝓻𝓼𝓲𝓿𝓮 font

• `{i}greekify <text>`
    turns text to ϑгεεκιғψ font

• `{i}sorcify <text>`
    turns text to ֆօʀƈɛʀɛʀ font

• `{i}fraktify <text>`
    turns text to 𝖋𝖗𝖆𝖐𝖙𝖚𝖗𝖊 font

• `{i}rusify <text>`
    turns text to яц$їfч font
"""
from . import oreo_cmd

normiefont = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
weebyfont = [
    "卂",
    "乃",
    "匚",
    "刀",
    "乇",
    "下",
    "厶",
    "卄",
    "工",
    "丁",
    "长",
    "乚",
    "从",
    "𠘨",
    "口",
    "尸",
    "㔿",
    "尺",
    "丂",
    "丅",
    "凵",
    "リ",
    "山",
    "乂",
    "丫",
    "乙",
]
tantextfont = [
    "Ꭿ",
    "Ᏸ",
    "Ꮳ",
    "Ꮄ",
    "Ꮛ",
    "Ꮄ",
    "Ꮆ",
    "Ꮒ",
    "i",
    "Ꮰ",
    "Ꮶ",
    "l",
    "m",
    "Ꮑ",
    "Ꮻ",
    "Ꮅ",
    "Ꮔ",
    "ᖇ",
    "Ꭶ",
    "Ꮏ",
    "Ꮜ",
    "Ꮙ",
    "Ꮿ",
    "ﾒ",
    "Ꭹ",
    "Ꮓ",
]
linetextfont = [
    "𝔸",
    "𝔹",
    "ℂ",
    "𝔻",
    "𝔼",
    "𝔽",
    "𝔾",
    "ℍ",
    "𝕀",
    "𝕁",
    "𝕂",
    "𝕃",
    "𝕄",
    "ℕ",
    "𝕆",
    "ℙ",
    "ℚ",
    "ℝ",
    "𝕊",
    "𝕋",
    "𝕌",
    "𝕍",
    "𝕎",
    "𝕏",
    "𝕐",
    "ℤ",
]
boxtextfont = [
    "🄰",
    "🄱",
    "🄲",
    "🄳",
    "🄴",
    "🄵",
    "🄶",
    "🄷",
    "🄸",
    "🄹",
    "🄺",
    "🄻",
    "🄼",
    "🄽",
    "🄾",
    "🄿",
    "🅀",
    "🅁",
    "🅂",
    "🅃",
    "🅄",
    "🅅",
    "🅆",
    "🅇",
    "🅈",
    "🅉",
]
bubbletextfont = [
    "Ⓐ",
    "Ⓑ",
    "Ⓒ",
    "Ⓓ",
    "Ⓔ",
    "Ⓕ",
    "Ⓖ",
    "Ⓗ",
    "Ⓘ",
    "Ⓙ",
    "Ⓚ",
    "Ⓛ",
    "Ⓜ",
    "Ⓝ",
    "Ⓞ",
    "Ⓟ",
    "Ⓠ",
    "Ⓡ",
    "Ⓢ",
    "Ⓣ",
    "Ⓤ",
    "Ⓥ",
    "Ⓦ",
    "Ⓧ",
    "Ⓨ",
    "Ⓩ",
]
cursivefont = [
    "𝓪",
    "𝓫",
    "𝓬",
    "𝓭",
    "𝓮",
    "𝓯",
    "𝓰",
    "𝓱",
    "𝓲",
    "𝓳",
    "𝓴",
    "𝓵",
    "𝓶",
    "𝓷",
    "𝓸",
    "𝓹",
    "𝓺",
    "𝓻",
    "𝓼",
    "𝓽",
    "𝓾",
    "𝓿",
    "𝔀",
    "𝔁",
    "𝔂",
    "𝔃",
]
greekfont = [
    "λ",
    "ϐ",
    "ς",
    "d",
    "ε",
    "ғ",
    "ϑ",
    "н",
    "ι",
    "ϳ",
    "κ",
    "l",
    "ϻ",
    "π",
    "σ",
    "ρ",
    "φ",
    "г",
    "s",
    "τ",
    "υ",
    "v",
    "ш",
    "ϰ",
    "ψ",
    "z",
]
sorcererfont = [
    "ǟ",
    "ɮ",
    "ƈ",
    "ɖ",
    "ɛ",
    "ʄ",
    "ɢ",
    "ɦ",
    "ɨ",
    "ʝ",
    "ӄ",
    "ʟ",
    "ʍ",
    "ռ",
    "օ",
    "ք",
    "զ",
    "ʀ",
    "ֆ",
    "ȶ",
    "ʊ",
    "ʋ",
    "ա",
    "Ӽ",
    "ʏ",
    "ʐ",
]
frakturfont = [
    "𝖆",
    "𝖇",
    "𝖈",
    "𝖉",
    "𝖊",
    "𝖋",
    "𝖌",
    "𝖍",
    "𝖎",
    "𝖏",
    "𝖐",
    "𝖑",
    "𝖒",
    "𝖓",
    "𝖔",
    "𝖕",
    "𝖖",
    "𝖗",
    "𝖘",
    "𝖙",
    "𝖚",
    "𝖛",
    "𝖜",
    "𝖝",
    "𝖞",
    "𝖟",
]
rusifont = [
    "а",
    "б",
    "c",
    "д",
    "ё",
    "f",
    "g",
    "н",
    "ї",
    "j",
    "к",
    "г",
    "ѫ",
    "п",
    "ѳ",
    "p",
    "ф",
    "я",
    "$",
    "т",
    "ц",
    "ѵ",
    "щ",
    "ж",
    "ч",
    "з",
]


@oreo_cmd(pattern="weeb ?(.*)")
async def weebify(ore):
    args = ore.pattern_match.group(1)
    if not args and ore.is_reply:
        get = await ore.get_reply_message()
        args = get.text
    if not args:
        await ore.edit("What I am Supposed to Weebify? Please Give Text Sir")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)
    await ore.eor(string)


@oreo_cmd(pattern="tantext ?(.*)")
async def tantxt(ore):
    args = ore.pattern_match.group(1)
    if not args and ore.is_reply:
        get = await ore.get_reply_message()
        args = get.text
    if not args:
        await ore.edit("What I am Supposed to tanify? Please Give Text Sir")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            tanycharacter = tantextfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, tanycharacter)
    await ore.eor(string)


@oreo_cmd(pattern="linetext ?(.*)")
async def linetxt(ore):
    args = ore.pattern_match.group(1)
    if not args and ore.is_reply:
        get = await ore.get_reply_message()
        args = get.text
    if not args:
        await ore.edit("What I am Supposed to linefy? Please Give Text Sir")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            linecharacter = linetextfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, linecharacter)
    await ore.edit(string)


@oreo_cmd(pattern="boxtext ?(.*)")
async def boxtxt(ore):
    args = ore.pattern_match.group(1)
    if not args and ore.is_reply:
        get = await ore.get_reply_message()
        args = get.text
    if not args:
        return await ore.edit("What I am Supposed to boxify? Please Give Text Sir")
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            boxcharacter = boxtextfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, boxcharacter)
    await ore.eor(string)


@oreo_cmd(pattern="bubbletext ?(.*)")
async def bubbletxt(ore):
    args = ore.pattern_match.group(1)
    if not args and ore.is_reply:
        get = await ore.get_reply_message()
        args = get.text
    if not args:
        return await ore.edit("What I am Supposed to bubblify? Please Give Text Sir")
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            bubblecharacter = bubbletextfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, bubblecharacter)
    await ore.eor(string)


@oreo_cmd(pattern="cursive ?(.*)")
async def cursive(ore):
    args = ore.pattern_match.group(1)
    if not args and ore.is_reply:
        get = await ore.get_reply_message()
        args = get.text
    if not args:
        return await ore.edit(
            "What I am Supposed to write in cursive? Please Give Text Sir"
        )
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            cursivecharacter = cursivefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, cursivecharacter)
    await ore.eor(string)


@oreo_cmd(pattern="greekify ?(.*)")
async def greektext(ore):
    args = ore.pattern_match.group(1)
    if not args and ore.is_reply:
        get = await ore.get_reply_message()
        args = get.text
    if not args:
        return await ore.edit("What I am Supposed to greekify? Please Give Text Sir")
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            greekcharacter = greekfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, greekcharacter)
    await ore.eor(string)


@oreo_cmd(pattern="sorcify ?(.*)")
async def sorcerertext(ore):

    args = ore.pattern_match.group(1)
    if not args and ore.is_reply:
        get = await ore.get_reply_message()
        args = get.text
    if not args:
        await ore.edit("What I am Supposed to sorcify? Please Give Text Sir")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            sorcerercharacter = sorcererfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, sorcerercharacter)
    await ore.eor(string)


@oreo_cmd(pattern="fraktify ?(.*)")
async def frakturtext(ore):
    args = ore.pattern_match.group(1)
    if not args and ore.is_reply:
        get = await ore.get_reply_message()
        args = get.text
    if not args:
        await ore.edit("What I am Supposed to fraktify? Please Give Text Sir")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            frakturcharacter = frakturfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, frakturcharacter)
    await ore.eor(string)


@oreo_cmd(pattern="rusify ?(.*)")
async def rusitext(ore):
    args = ore.pattern_match.group(1)
    if not args and ore.is_reply:
        get = await ore.get_reply_message()
        args = get.text
    if not args:
        return await ore.edit("What I am Supposed to rusify? Please Give Text Sir")
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            rusicharacter = rusifont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, rusicharacter)
    await ore.eor(string)
