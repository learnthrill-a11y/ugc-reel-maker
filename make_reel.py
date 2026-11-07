import os
import asyncio
from moviepy.editor import ColorClip, TextClip, CompositeVideoClip, AudioFileClip, CompositeAudioClip

WIDTH, HEIGHT = 1080, 1920
FPS = 30
DURATION = 12

# 1. AI വോയ്‌സ് ഓവർ ഉണ്ടാക്കുന്നു
VOICE_SCRIPT = "UGC NET Paper 1 preparation made easy with LearnThrill. Practice mock tests in real NTA exam interface and get complete study materials."

async def generate_voice():
    import edge_tts
    # Indian English voice
    communicate = edge_tts.Communicate(VOICE_SCRIPT, "en-IN-PrabhatNeural")
    await communicate.save("voiceover.mp3")

asyncio.run(generate_voice())

# 2. വിഷ്വൽ ലെയറുകൾ
bg = ColorClip(size=(WIDTH, HEIGHT), color=(10, 15, 30), duration=DURATION)

brand_badge = (TextClip("LEARNTHRILL • UGC NET PAPER 1", fontsize=38, color="#94A3B8", font="DejaVu-Sans-Bold")
               .set_position(('center', 180)).set_start(0).set_duration(DURATION))

hook = (TextClip("Struggling with\nNTA Exam Interface?", fontsize=64, color="#EF4444", font="DejaVu-Sans-Bold", align="center")
        .set_position(('center', 750)).set_start(0).set_duration(3.5).crossfadein(0.3))

subhook = (TextClip("Practice like the real exam!", fontsize=42, color="#F8FAFC", font="DejaVu-Sans", align="center")
           .set_position(('center', 980)).set_start(1).set_duration(2.5))

f1_title = (TextClip("Real NTA Exam Interface", fontsize=58, color="#38BDF8", font="DejaVu-Sans-Bold", align="center")
            .set_position(('center', 700)).set_start(3.5).set_duration(4))

f1_desc = (TextClip("Question Palette, Timer, Marking\nExact exam simulation!", fontsize=44, color="#FFFFFF", font="DejaVu-Sans", align="center")
           .set_position(('center', 840)).set_start(4).set_duration(3.5))

f2_title = (TextClip("Complete Study Materials", fontsize=56, color="#FACC15", font="DejaVu-Sans-Bold", align="center")
            .set_position(('center', 650)).set_start(7.5).set_duration(4.5))

f2_desc = (TextClip("All 10 Units Covered with PYQs!", fontsize=44, color="#FFFFFF", font="DejaVu-Sans", align="center")
           .set_position(('center', 780)).set_start(8).set_duration(4))

cta_box = (TextClip("Try for Free Now!\nComment: 'NET'", fontsize=52, color="#4ADE80", font="DejaVu-Sans-Bold", align="center")
           .set_position(('center', 1250)).set_start(8.5).set_duration(3.5).crossfadein(0.4))

url_text = (TextClip("learnthrill.com", fontsize=44, color="#E2E8F0", font="DejaVu-Sans-Bold")
            .set_position(('center', 1450)).set_start(9).set_duration(3))

video = CompositeVideoClip([bg, brand_badge, hook, subhook, f1_title, f1_desc, f2_title, f2_desc, cta_box, url_text])

# 3. ഓഡിയോ മിക്സിങ്
voice_clip = AudioFileClip("voiceover.mp3").volumex(1.2)
audio_tracks = [voice_clip]

if os.path.exists("bgm.mp3"):
    bgm_clip = AudioFileClip("bgm.mp3").subclip(0, DURATION).volumex(0.18)
    audio_tracks.append(bgm_clip)

final_audio = CompositeAudioClip(audio_tracks).set_duration(DURATION)
final_video = video.set_audio(final_audio)

final_video.write_videofile("learnthrill_promo_reel.mp4", fps=FPS, codec="libx264", audio_codec="aac")
