import os
import asyncio
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from moviepy.editor import ImageSequenceClip, AudioFileClip, CompositeAudioClip

WIDTH, HEIGHT = 1080, 1920
FPS = 24
DURATION = 12
TOTAL_FRAMES = FPS * DURATION

# 1. AI Voiceover
VOICE_SCRIPT = "UGC NET Paper 1 preparation made easy with LearnThrill. Practice mock tests in real NTA exam interface and get complete study materials."

async def generate_voice():
    import edge_tts
    communicate = edge_tts.Communicate(VOICE_SCRIPT, "en-IN-PrabhatNeural")
    await communicate.save("voiceover.mp3")

asyncio.run(generate_voice())

# 2. ഫ്രെയിമുകൾ ജനറേറ്റ് ചെയ്യുന്നു (ImageMagick ആവശ്യമില്ല)
frames = []

for frame_idx in range(TOTAL_FRAMES):
    t = frame_idx / FPS
    
    # ബാക്ക്ഗ്രൗണ്ട് (Dark Slate Theme)
    img = Image.new("RGB", (WIDTH, HEIGHT), color=(15, 23, 42))
    draw = ImageDraw.Draw(img)

    # ടോപ്പ് ബാഡ്ജ്
    draw.text((WIDTH//2, 180), "LEARNTHRILL • UGC NET PAPER 1", fill=(148, 163, 184), anchor="mm")

    # Hook (0 - 3.5s)
    if t < 3.5:
        draw.text((WIDTH//2, 750), "Struggling with\nNTA Exam Interface?", fill=(239, 68, 68), anchor="mm", align="center")
        if t > 1.0:
            draw.text((WIDTH//2, 980), "Practice like the real exam!", fill=(248, 250, 252), anchor="mm")

    # Feature 1: NTA Mock Test (3.5 - 7.5s)
    elif 3.5 <= t < 7.5:
        draw.text((WIDTH//2, 700), "🖥️ Real NTA Exam Interface", fill=(56, 189, 248), anchor="mm")
        draw.text((WIDTH//2, 850), "Exact Question Palette, Timer & Marking!\nReal Exam Simulation", fill=(255, 255, 255), anchor="mm", align="center")

    # Feature 2: Complete Study Materials (7.5 - 12s)
    else:
        draw.text((WIDTH//2, 650), "📚 Complete Study Materials", fill=(250, 204, 21), anchor="mm")
        draw.text((WIDTH//2, 780), "All 10 Units Covered with PYQs!", fill=(255, 255, 255), anchor="mm")
        
        # Call To Action Box (8.5s മുതൽ അവസാനം വരെ)
        if t >= 8.5:
            draw.text((WIDTH//2, 1250), "👉 Try for Free Now!\nComment 'NET' Below", fill=(74, 222, 128), anchor="mm", align="center")
            draw.text((WIDTH//2, 1450), "learnthrill.com", fill=(226, 232, 240), anchor="mm")

    frames.append(np.array(img))

# 3. വീഡിയോ നിർമ്മിക്കുന്നു
video = ImageSequenceClip(frames, fps=FPS)

# 4. ഓഡിയോ ചേർക്കുന്നു
voice_clip = AudioFileClip("voiceover.mp3")
audio_tracks = [voice_clip]

if os.path.exists("bgm.mp3"):
    bgm_clip = AudioFileClip("bgm.mp3").subclip(0, DURATION).volumex(0.18)
    audio_tracks.append(bgm_clip)

video = video.set_audio(CompositeAudioClip(audio_tracks).set_duration(DURATION))
video.write_videofile("learnthrill_promo_reel.mp4", fps=FPS, codec="libx264", audio_codec="aac")
