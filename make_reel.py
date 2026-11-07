import subprocess
import os

WIDTH = 1080
HEIGHT = 1920
DURATION = 12

# 1. AI Voiceover ഉണ്ടാക്കുന്നു
VOICE_TEXT = "UGC NET Paper 1 preparation made easy with LearnThrill. Practice mock tests in real NTA exam interface and get complete study materials."
voice_cmd = f'edge-tts --text "{VOICE_TEXT}" --voice en-IN-PrabhatNeural --write-media voiceover.mp3'
subprocess.run(voice_cmd, shell=True, check=True)

# 2. ബാക്ക്ഗ്രൗണ്ട് ഓഡിയോ (BGM ഉണ്ടെങ്കിൽ മിക്സ് ചെയ്യുക, ഇല്ലെങ്കിൽ voiceover മാത്രം)
audio_input = "-i voiceover.mp3"
audio_filter = ""
if os.path.exists("bgm.mp3"):
    audio_input = "-i voiceover.mp3 -i bgm.mp3"
    audio_filter = '-filter_complex "[1:a]volume=0.15[bgm];[0:a][bgm]amix=inputs=2:duration=first[aout]" -map 0:v -map "[aout]"'
else:
    audio_filter = "-c:a aac"

# 3. FFmpeg ഉപയോഗിച്ച് നേരിട്ട് 1080x1920 വീഡിയോ നിർമ്മിക്കുന്നു
ffmpeg_cmd = f"""ffmpeg -y -f lavfi -i color=c=0x0f172a:s={WIDTH}x{HEIGHT}:d={DURATION}:r=30 {audio_input} \\
-vf "drawtext=text='LEARNTHRILL • UGC NET PAPER 1':fontcolor=0x94a3b8:fontsize=38:x=(w-text_w)/2:y=180, \\
     drawtext=text='Struggling with NTA Exam Interface?':fontcolor=0xef4444:fontsize=52:x=(w-text_w)/2:y=750:enable='between(t,0,3.5)', \\
     drawtext=text='Practice like the real exam!':fontcolor=0xf8fafc:fontsize=40:x=(w-text_w)/2:y=850:enable='between(t,1,3.5)', \\
     drawtext=text='Real NTA Exam Interface':fontcolor=0x38bdf8:fontsize=54:x=(w-text_w)/2:y=700:enable='between(t,3.5,7.5)', \\
     drawtext=text='Question Palette, Timer & Marking!':fontcolor=0xffffff:fontsize=42:x=(w-text_w)/2:y=800:enable='between(t,3.5,7.5)', \\
     drawtext=text='Complete Study Materials':fontcolor=0xfacc15:fontsize=54:x=(w-text_w)/2:y=650:enable='between(t,7.5,12)', \\
     drawtext=text='All 10 Units Covered with PYQs!':fontcolor=0xffffff:fontsize=42:x=(w-text_w)/2:y=750:enable='between(t,7.5,12)', \\
     drawtext=text='Try for Free Now! Comment NET':fontcolor=0x4ade80:fontsize=48:x=(w-text_w)/2:y=1250:enable='between(t,8.5,12)', \\
     drawtext=text='learnthrill.com':fontcolor=0xe2e8f0:fontsize=42:x=(w-text_w)/2:y=1380:enable='between(t,8.5,12)'" \\
{audio_filter} -pix_fmt yuv420p -shortest learnthrill_promo_reel.mp4"""

subprocess.run(ffmpeg_cmd, shell=True, check=True)
print("Video successfully generated!")
