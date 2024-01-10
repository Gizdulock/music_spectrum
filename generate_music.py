import requests
import numpy as np
import librosa

from config import YOUTUBE_API_KEY

def generate_music(style):
  """Generálja a megadott zenei stílusú zenét.

  Args:
    style: A zene stílusa.

  Returns:
    A generált zene.
  """

  # Az mesterséges intelligencia modell inicializálása.
  model = nsynth.Model()

  # A YouTube-on történő keresés.
  query = "zene stílus: " + style
  response = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&q=" + query + "&type=video&maxResults=10")
  results = response.json()["items"]

  # A keresési eredményekből a zenestílus jellemzőinek kiválasztása.
  features = []
  for result in results:
    features.append(
      [
        result["snippet"]["channelTitle"],
        result["snippet"]["description"],
        result["snippet"]["title"],
        result["snippet"]["tags"],
      ]
    )

  # A zenegenerálási algoritmus beállítása.
  model.set_features(features)

  # A zenegenerálási algoritmus további beállításai.
  model.set_randomness(RANDOMNESS)
  model.set_improvisation(IMPROVISATION)

  # A zene generálása.
  audio = model.generate()

  # Visszatérés a generált zenével.
  return audio
