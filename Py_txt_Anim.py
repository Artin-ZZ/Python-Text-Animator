import pyfiglet
from moviepy.editor import *
import os

def generate_animation(text):
    # Convert text to fancy text using pyfiglet
    fancy_text = pyfiglet.figlet_format(text, font="3d_diagonal")

    # Define function to create animation clip
    def make_animation(t):
        # Calculate position for text animation
        x = int(100*t)
        txt_clip = TextClip(fancy_text, fontsize=70, color='white').set_duration(5)
        return txt_clip

    # Create video clip with animation
    animation_clip = CompositeVideoClip([make_animation(0)]).set_duration(5)

    # Set audio file path
    audio_path = "D:/Currently-Working/Py_Tricks/Jaeger - Heaven Tonight.mp3"

    # Check if audio file exists
    if os.path.exists(audio_path):
        # Load audio file
        audio_clip = AudioFileClip(audio_path)
        # Add audio to animation clip
        animation_with_audio = animation_clip.set_audio(audio_clip)
        return animation_with_audio
    else:
        return animation_clip

def main():
    # Take user's name as input
    name = input("Enter your name: ")

    # Generate animation for the name
    animation = generate_animation(name)

    # Export animation to a file
    animation.write_videofile("animated_name.mp4", fps=24, codec='libx264', audio_codec='aac', temp_audiofile='temp-audio.m4a', remove_temp=True)

    print("Animation created successfully!")

if __name__ == "__main__":
    main()