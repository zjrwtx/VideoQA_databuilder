import openai
from openai import OpenAI
from dotenv import load_dotenv
import os

import time
import random
from youtube_transcript_api import YouTubeTranscriptApi


# Replace 'YOUR_VIDEO_ID' with the ID of the YouTube video you want to download subtitles for
video_url = input("请输入你要生成视频问题的youtube视频地址: e.g. https://www.youtube.com/watch?v=CjTTSa33axg")
video_id = video_url.split("=")[1]
language_video = input("字幕语言: en, fr, de,zh-Hans, etc. ")
question_num=input("要生成的问题的个数:")
question_language=input("生成的问题的语言: 中文，English, etc. ")
"""
(TRANSLATION LANGUAGES)
 - af ("Afrikaans")
 - ak ("Akan")
 - sq ("Albanian")
 - am ("Amharic")
 - ar ("Arabic")
 - hy ("Armenian")
 - as ("Assamese")
 - ay ("Aymara")
 - az ("Azerbaijani")
 - bn ("Bangla")
 - eu ("Basque")
 - be ("Belarusian")
 - bho ("Bhojpuri")
 - bs ("Bosnian")
 - bg ("Bulgarian")
 - my ("Burmese")
 - ca ("Catalan")
 - ceb ("Cebuano")
 - zh-Hans ("Chinese (Simplified)")
 - zh-Hant ("Chinese (Traditional)")
 - co ("Corsican")
 - hr ("Croatian")
 - cs ("Czech")
 - da ("Danish")
 - dv ("Divehi")
 - nl ("Dutch")
 - en ("English")
 - eo ("Esperanto")
 - et ("Estonian")
 - ee ("Ewe")
 - fil ("Filipino")
 - fi ("Finnish")
 - fr ("French")
 - gl ("Galician")
 - lg ("Ganda")
 - ka ("Georgian")
 - de ("German")
 - el ("Greek")
 - gn ("Guarani")
 - gu ("Gujarati")
 - ht ("Haitian Creole")
 - ha ("Hausa")
 - haw ("Hawaiian")
 - iw ("Hebrew")
 - hi ("Hindi")
 - hmn ("Hmong")
 - hu ("Hungarian")
 - is ("Icelandic")
 - ig ("Igbo")
 - id ("Indonesian")
 - ga ("Irish")
 - it ("Italian")
 - ja ("Japanese")
 - jv ("Javanese")
 - kn ("Kannada")
 - kk ("Kazakh")
 - km ("Khmer")
 - rw ("Kinyarwanda")
 - ko ("Korean")
 - kri ("Krio")
 - ku ("Kurdish")
 - ky ("Kyrgyz")
 - lo ("Lao")
 - la ("Latin")
 - lv ("Latvian")
 - ln ("Lingala")
 - lt ("Lithuanian")
 - lb ("Luxembourgish")
 - mk ("Macedonian")
 - mg ("Malagasy")
 - ms ("Malay")
 - ml ("Malayalam")
 - mt ("Maltese")
 - mi ("Māori")
 - mr ("Marathi")
 - mn ("Mongolian")
 - ne ("Nepali")
 - nso ("Northern Sotho")
 - no ("Norwegian")
 - ny ("Nyanja")
 - or ("Odia")
 - om ("Oromo")
 - ps ("Pashto")
 - fa ("Persian")
 - pl ("Polish")
 - pt ("Portuguese")
 - pa ("Punjabi")
 - qu ("Quechua")
 - ro ("Romanian")
 - ru ("Russian")
 - sm ("Samoan")
 - sa ("Sanskrit")
 - gd ("Scottish Gaelic")
 - sr ("Serbian")
 - sn ("Shona")
 - sd ("Sindhi")
 - si ("Sinhala")
 - sk ("Slovak")
 - sl ("Slovenian")
 - so ("Somali")
 - st ("Southern Sotho")
 - es ("Spanish")
 - su ("Sundanese")
 - sw ("Swahili")
 - sv ("Swedish")
 - tg ("Tajik")
 - ta ("Tamil")
 - tt ("Tatar")
 - te ("Telugu")
 - th ("Thai")
 - ti ("Tigrinya")
 - ts ("Tsonga")
 - tr ("Turkish")
 - tk ("Turkmen")
 - uk ("Ukrainian")
 - ur ("Urdu")
 - ug ("Uyghur")
 - uz ("Uzbek")
 - vi ("Vietnamese")
 - cy ("Welsh")
 - fy ("Western Frisian")
 - xh ("Xhosa")
 - yi ("Yiddish")
 - yo ("Yoruba")
 - zu ("Zulu")
"""



try:
    # Fetch the transcript
    print(video_id)
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language_video])

except Exception as e:
    print(f"An error occurred: {e}")

#merge all the text in one string
text = ""
for i in transcript:
    text += i['text'] + " "
with open('srt.txt', 'w', encoding='utf-8') as file:
    file.write(text)

print("视频字幕已保存到srt.txt文件中。")

# 在使用API密钥和基础URL之前加载.env文件
load_dotenv()

# 现在可以通过os.environ访问这些值
API_BASE = os.environ.get("API_BASE")
API_KEY = os.environ.get("API_KEY")


client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=API_KEY,
    base_url=API_BASE
)
completion = client.chat.completions.create(
    model="yi-34b-chat-200k",
    messages=[{"role": "system", "content":"你是一个QA问答对构建专家，专门根据用户视频的内容构建"+question_num+"个高质量的"+question_language+"问题："},
              {"role":"user","content":"生成"+question_num+"个高质量的问题："+text+";并每个问题输出显示都要换行"},
              ],
    max_tokens=6000,
    top_p=0.8,
    # stream=True,
)
outputtext=completion.choices[0].message.content
print(outputtext)
with open('questions.txt', 'w', encoding='utf-8') as file:
    file.write(outputtext)

print("输出内容已保存到questions.txt文件中。")
# for chunk in completion:
#     # print(chunk) 
#     print(chunk.choices[0].delta.content or "", end="", flush=True)


# https://www.youtube.com/watch?v=CjTTSa33axg