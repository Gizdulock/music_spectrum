import generate_music
import create_spectrum_gif

from config import YOUTUBE_API_KEY

def main():
  # A zenestílus beolvasása.
  style = input("Kérem, adja meg a zene stílusát: ")

  # A zene generálása.
  audio = generate_music.generate_music(style)

  # A spectrum gif létrehozása.
  gif = create_spectrum_gif.create_spectrum_gif(audio)

  # A zene és a gif egyben történő elmentése.
  with open("music_and_gif.mp4", "wb") as f:
    f.write(audio)
    f.write(gif.getvalue())

if __name__ == "__main__":
  main()
