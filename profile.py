# Oreo


"""
✘ Commands Available -

• `{i}setname <first name // last name>`
    Change your profile name.

• `{i}setbio <bio>`
    Change your profile bio.

• `{i}setpic <reply to pic>`
    Change your profile pic.

• `{i}delpfp <n>(optional)`
    Delete one profile pic, if no value given, else delete n number of pics.

• `{i}poto <username>/reply`
  `{i}poto <reply/upload-limit>/all`

  Ex: `{i}poto 10` - uploads starting 10 pfps of user.
    Upload the photo of Chat/User if Available.
"""
import os

from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import DeletePhotosRequest, UploadProfilePhotoRequest

from . import eod, eor, get_string, mediainfo, oreo_cmd

TMP_DOWNLOAD_DIRECTORY = "resources/downloads/"

# bio changer


@oreo_cmd(pattern="setbio( (.*)|$)", fullsudo=True)
async def _(ore):
    ok = await ore.eor("...")
    set = ore.pattern_match.group(1).strip()
    try:
        await ore.client(UpdateProfileRequest(about=set))
        await eod(ok, f"Profile bio changed to\n`{set}`")
    except Exception as ex:
        await eod(ok, f"Error occured.\n`{str(ex)}`")


# name changer


@oreo_cmd(pattern="setname ?((.|//)*)", fullsudo=True)
async def _(ore):
    ok = await ore.eor("...")
    names = first_name = ore.pattern_match.group(1).strip()
    last_name = ""
    if "//" in names:
        first_name, last_name = names.split("//", 1)
    try:
        await ore.client(
            UpdateProfileRequest(
                first_name=first_name,
                last_name=last_name,
            ),
        )
        await eod(ok, f"Name changed to `{names}`")
    except Exception as ex:
        await eod(ok, f"Error occured.\n`{str(ex)}`")


# profile pic


@oreo_cmd(pattern="setpic$", fullsudo=True)
async def _(ore):
    if not ore.is_reply:
        return await ore.eor("`Reply to a Media..`", time=5)
    reply_message = await ore.get_reply_message()
    ok = await ore.eor(get_string("com_1"))
    replfile = await reply_message.download_media()
    file = await ore.client.upload_file(replfile)
    try:
        if "pic" in mediainfo(reply_message.media):
            await ore.client(UploadProfilePhotoRequest(file))
        else:
            await ore.client(UploadProfilePhotoRequest(video=file))
        await eod(ok, "`My Profile Photo has Successfully Changed !`")
    except Exception as ex:
        await eod(ok, f"Error occured.\n`{str(ex)}`")
    os.remove(replfile)


# delete profile pic(s)


@oreo_cmd(pattern="delpfp( (.*)|$)", fullsudo=True)
async def remove_profilepic(delpfp):
    ok = await eor(delpfp, "`...`")
    group = delpfp.text[8:]
    if group == "all":
        lim = 0
    elif group.isdigit():
        lim = int(group)
    else:
        lim = 1
    pfplist = await delpfp.client.get_profile_photos("me", limit=lim)
    await delpfp.client(DeletePhotosRequest(pfplist))
    await eod(ok, f"`Successfully deleted {len(pfplist)} profile picture(s).`")


@oreo_cmd(pattern="poto( (.*)|$)")
async def gpoto(e):
    ore = e.pattern_match.group(1).strip()

    if e.is_reply:
        gs = await e.get_reply_message()
        user_id = gs.sender_id
    elif ore:
        split = ore.split()
        user_id = split[0]
        if len(ore) > 1:
            ore = ore[-1]
        else:
            ore = None
    else:
        user_id = e.chat_id

    a = await e.eor(get_string("com_1"))
    limit = None

    just_dl = ore in ["-dl", "--dl"]
    if just_dl:
        ore = None

    if ore and ore != "all":
        try:
            limit = int(ore)
        except ValueError:
            pass

    if not limit or e.client._bot:
        okla = await e.client.download_profile_photo(user_id)
    else:
        okla = []
        if limit == "all":
            limit = None
        async for photo in e.client.iter_profile_photos(user_id, limit=limit):
            photo_path = await e.client.download_media(photo)
            if photo.video_sizes:
                await e.respond(file=photo_path)
                os.remove(photo_path)
            else:
                okla.append(photo_path)
    if not okla:
        return await eor(a, "`Pfp Not Found...`")
    if not just_dl:
        await a.delete()
        await e.reply(file=okla)
        if not isinstance(okla, list):
            okla = [okla]
        for file in okla:
            os.remove(file)
        return
    if isinstance(okla, list):
        okla = "\n".join(okla)
    await a.edit(f"Downloaded pfp to [ `{okla}` ].")
