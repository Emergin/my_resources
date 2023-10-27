from moviepy.editor import VideoFileClip

def video_to_audio(video_path, audio_path):
    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_path)
    
    video_clip.close()
    audio_clip.close()

if __name__ == "__main__":
    input_video_path = "/home/trubel/Pictures/2.mkv"   # Replace with the path to your input video
    output_audio_path = "/home/trubel/Pictures/2.mp3" # Replace with the desired output audio file format (e.g., .wav, .mp3)

    video_to_audio(input_video_path, output_audio_path)

