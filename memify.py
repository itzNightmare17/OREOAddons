# oreo
# Ported Nd Modified For OreO ub
# Ported From DarkCobra (Modified by @ProgrammingError)


"""
✘ Commands Available -

• `{i}mmf <upper text> ; <lower text> <reply to media>`
    To create memes as sticker,
    for trying different fonts use (.mmf <text>_1)(u can use 1 to 10).

• `{i}mms <upper text> ; <lower text> <reply to media>`
    To create memes as pic,
    for trying different fonts use (.mms <text>_1)(u can use 1 to 10).

"""

import asyncio
import os
import textwrap

import cv2
from PIL import Image, ImageDraw, ImageFont

from . import *


@oreo_cmd(pattern="mmf ?(.*)")
async def ored(event):
    ureply = await event.get_reply_message()
    msg = event.pattern_match.group(1)
    if not (ureply and (ureply.media)):
        xx = await event.eor("`Reply to any media`")
        return
    if not msg:
        xx = await event.eor("`Give me something text to write...`")
        return
    oret = await ureply.download_media()
    if oret.endswith((".tgs")):
        xx = await event.eor("`Ooo Animated Sticker 👀...`")
        cmd = ["lottie_convert.py", oret, "ore.png"]
        file = "ore.png"
        process = await asyncio.create_subprocess_exec(
            *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    elif oret.endswith((".webp", ".png")):
        xx = await event.eor("`Processing`")
        im = Image.open(oret)
        im.save("ore.png", format="PNG", optimize=True)
        file = "ore.png"
    else:
        xx = await event.eor("`Processing`")
        img = cv2.VideoCapture(oret)
        heh, lol = img.read()
        cv2.imwrite("ore.png", lol)
        file = "ore.png"
    stick = await draw_meme_text(file, msg)
    await event.client.send_file(
        event.chat_id, stick, force_document=False, reply_to=event.reply_to_msg_id
    )
    await xx.delete()
    try:
        os.remove(oret)
        os.remove(file)
        os.remove(stick)
    except BaseException:
        pass


async def draw_meme_text(image_path, msg):
    img = Image.open(image_path)
    os.remove(image_path)
    i_width, i_height = img.size
    if "_" in msg:
        text, font = msg.split("_")
    else:
        text = msg
        font = "default"
    if ";" in text:
        upper_text, lower_text = text.split(";")
    else:
        upper_text = text
        lower_text = ""
    draw = ImageDraw.Draw(img)
    m_font = ImageFont.truetype(
        f"resources/fonts/{font}.ttf", int((70 / 640) * i_width)
    )
    current_h, pad = 10, 5
    if upper_text:
        for u_text in textwrap.wrap(upper_text, width=15):
            u_width, u_height = draw.textsize(u_text, font=m_font)
            draw.text(
                xy=(((i_width - u_width) / 2) - 1, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(((i_width - u_width) / 2) + 1, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=((i_width - u_width) / 2, int(((current_h / 640) * i_width)) - 1),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(((i_width - u_width) / 2), int(((current_h / 640) * i_width)) + 1),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=((i_width - u_width) / 2, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(255, 255, 255),
            )
            current_h += u_height + pad
    if lower_text:
        for l_text in textwrap.wrap(lower_text, width=15):
            u_width, u_height = draw.textsize(l_text, font=m_font)
            draw.text(
                xy=(
                    ((i_width - u_width) / 2) - 1,
                    i_height - u_height - int((80 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    ((i_width - u_width) / 2) + 1,
                    i_height - u_height - int((80 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    (i_height - u_height - int((80 / 640) * i_width)) - 1,
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    (i_height - u_height - int((80 / 640) * i_width)) + 1,
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    i_height - u_height - int((80 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(255, 255, 255),
            )
            current_h += u_height + pad
    imag = "oret.webp"
    img.save(imag, "WebP")
    return imag


@oreo_cmd(pattern="mms ?(.*)")
async def mms(event):
    ureply = await event.get_reply_message()
    msg = event.pattern_match.group(1)
    if not (ureply and (ureply.media)):
        xx = await event.eor("`Reply to any media`")
        return
    if not msg:
        xx = await event.eor("`Give me something text to write 😑`")
        return
    oret = await ureply.download_media()
    if oret.endswith((".tgs")):
        xx = await event.eor("`Ooo Animated Sticker 👀...`")
        cmd = ["lottie_convert.py", oret, "ore.png"]
        file = "ore.png"
        process = await asyncio.create_subprocess_exec(
            *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    elif oret.endswith((".webp", ".png")):
        xx = await event.eor("`Processing`")
        im = Image.open(oret)
        im.save("ore.png", format="PNG", optimize=True)
        file = "ore.png"
    else:
        xx = await event.eor("`Processing`")
        img = cv2.VideoCapture(oret)
        heh, lol = img.read()
        cv2.imwrite("ore.png", lol)
        file = "ore.png"
    pic = await draw_meme(file, msg)
    await event.client.send_file(
        event.chat_id, pic, force_document=False, reply_to=event.reply_to_msg_id
    )
    await xx.delete()
    try:
        os.remove(oret)
        os.remove(file)
    except BaseException:
        pass
    os.remove(pic)


async def draw_meme(image_path, msg):
    img = Image.open(image_path)
    os.remove(image_path)
    i_width, i_height = img.size
    if "_" in msg:
        text, font = msg.split("_")
    else:
        text = msg
        font = "default"
    if ";" in text:
        upper_text, lower_text = text.split(";")
    else:
        upper_text = text
        lower_text = ""
    draw = ImageDraw.Draw(img)
    m_font = ImageFont.truetype(
        f"resources/fonts/{font}.ttf", int((70 / 640) * i_width)
    )
    current_h, pad = 10, 5
    if upper_text:
        for u_text in textwrap.wrap(upper_text, width=15):
            u_width, u_height = draw.textsize(u_text, font=m_font)
            draw.text(
                xy=(((i_width - u_width) / 2) - 1, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(((i_width - u_width) / 2) + 1, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=((i_width - u_width) / 2, int(((current_h / 640) * i_width)) - 1),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(((i_width - u_width) / 2), int(((current_h / 640) * i_width)) + 1),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=((i_width - u_width) / 2, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(255, 255, 255),
            )
            current_h += u_height + pad
    if lower_text:
        for l_text in textwrap.wrap(lower_text, width=15):
            u_width, u_height = draw.textsize(l_text, font=m_font)
            draw.text(
                xy=(
                    ((i_width - u_width) / 2) - 1,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    ((i_width - u_width) / 2) + 1,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    (i_height - u_height - int((20 / 640) * i_width)) - 1,
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    (i_height - u_height - int((20 / 640) * i_width)) + 1,
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(255, 255, 255),
            )
            current_h += u_height + pad
    pics = "oret.png"
    img.save(pics, "png")
    return pics
