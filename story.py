# Oreo


"""
✘ Commands Available
• `{i}story`
    Gives a story.
"""

import random
import re
from . import HELP


stories = [
    "`A man married a very beautiful girl, He admired her beauty and loved her very much.\nAfter few months the girl came to know she was suffering from a skin disease and gradually will lose her beauty.\nKnowing this she started to think 'what if I become ugly' my husband would hate me.\nOne day the husband lost his both eyes due to an unfortunate accident.\nDays passed and wife completely lost her beauty, it didn't bother her because her husband couldn't see, inspite of this their married life continued happily years passed and sadly wife passed away because of the disease, the man was hurt and on the funeral rites his neighbour saw him and asked him 'how will you be able to live without your wife's support, you cannot see'.\nHusband replied,'friend I'm not blind', I pretended to be blind these many years.\nBecause when my wife came to know about the disease she was bother by it and scared. \nIf my wife had known that I could see her ugliness, it would hurt her more than her illness.\nShe was a good wife to me and i wanted to keep her happy, thus pretended to be blind for years.`",

    "`A 16 year old boy ask his mother, 'Mom, what are you going to get me for my 18th birthday?',\nThe mother answered: 'son that's still a long way'....\nNow he is 17 years old and one day he faints, his mother takes him to the hospital and the doctor said, 'maam, your child has a bad heart''.\nBeing the guy on the stretcher the boy said: 'did he tell you I am going to die'?\nMother starts crying and boy finally recover on his 18th birthday, so he comes home where he found a letter on his bed which is left by his mother.\nThe letter said: 'son you are reading this it means everything went well, remember one day you asked me what was giving you for your 18th birthday and didn't know what to answer you....! gave you my heart.\nHappy Birthday son.`",
]


@oreo_cmd( pattern="story")
async def story(ore):
    rns = random.choice(stories)
    return await ore.edit(f"{rns}")
