from winsound import PlaySound
from  gtts import gTTS
from PlaySound import playsound
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
text = '안녕하세요 마이크로소프트 에이아이 스쿨에 오신 것을 환영합니다.'
tts = gTTS(text = text, lang='ok')

current_file_path = os.getcwd() + "/h1.mp3"
tts.save(current_file_path)

playsound(current_file_path)