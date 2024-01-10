import librosa

def create_spectrum_gif(audio):
  """Létrehozza a megadott hangból a spectrum gifet.

  Args:
    audio: A hang, amelyből a spectrum gifet kell létrehozni.

  Returns:
    A spectrum gif.
  """

  # A hangból a spectrum ábra létrehozása.
  spectrum = librosa.core.stft(audio)

  # A spectrum ábra gif-be konvertálása.
  gif = io.BytesIO()
  plt.plot(spectrum)
  plt.savefig(gif, format='gif', dpi=100, frameon=False)
  gif.seek(0)

  # Visszatérés a spectrum gif-fel.
  return gif
