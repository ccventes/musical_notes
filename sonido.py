from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_mp3("WOW_wrathgate.mp3")
sound2 = AudioSegment.from_mp3("WOW_wrathgate.mp3")
first_10_seconds = sound[:10000]

last_5_seconds = sound[-5000:]
#play(last_5_seconds)
#play(first_10_seconds)
mixed = last_5_seconds.overlay(first_10_seconds)
play(mixed)