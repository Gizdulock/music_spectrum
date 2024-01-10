**Installation**

To install the music generator application, follow these steps:

1. Make sure you have Python 3.6 or later installed on your computer.
2. Download the source code from GitHub.
3. Open a command prompt or Anaconda Prompt in the downloaded directory.
4. Type the following command:

```
pip install -r requirements.txt
```

This will install all of the dependencies required for the application.

**Usage**

To use the application, follow these steps:

1. Start a command prompt or Anaconda Prompt.
2. Navigate to the downloaded directory.
3. Type the following command:

```
python main.py
```

This will start the application.

After the application starts, follow these steps:

1. Type the music style you want to generate.
2. Press Enter.

The application will start generating the music. When the music is finished, the application will save it to a file called `music_and_gif.mp4`.

**Configuration**

To configure the application, follow these steps:

1. Create a file called `config.py` in the downloaded directory.
2. Type the following into the file:

```
# YouTube API key
YOUTUBE_API_KEY = "YOUR_API_KEY"

# Music generator algorithm settings
RANDOMNESS = 0.5
IMPROVISATION = 0.2
```

The `YOUTUBE_API_KEY` variable should contain your own YouTube API key. The `RANDOMNESS` and `IMPROVISATION` variables control the randomness and improvisation of the music generator algorithm.

**Additional information**

For more information, read the documentation: docs/README.md.

**Randomness**

The `RANDOMNESS` value controls the randomness of the music generator algorithm. A value of 0 means that the music generator algorithm is completely deterministic, and a value of 1 means that the music generator algorithm is completely random.

Increasing the `RANDOMNESS` value will make the generated music more varied and exciting. However, at too high a `RANDOMNESS` value, the generated music may become chaotic and difficult to understand.

**Improvisation**

The `IMPROVISATION` value controls the amount of improvisation used by the music generator algorithm. A value of 0 means that the music generator algorithm does not use improvisation, and a value of 1 means that the music generator algorithm completely improvises.

Increasing the `IMPROVISATION` value will make the generated music more creative and original. However, at too high an `IMPROVISATION` value, the generated music may become chaotic and difficult to understand.

**Examples**

Here are some examples of how the `RANDOMNESS` and `IMPROVISATION` values can affect the generated music:

* **RANDOMNESS = 0.0, IMPROVISATION = 0.0**

The generated music will be completely deterministic and repetitive.

* **RANDOMNESS = 0.5, IMPROVISATION = 0.0**

The generated music will be more varied and exciting, but still easy to understand.

* **RANDOMNESS = 0.5, IMPROVISATION = 0.5**

The generated music will be more creative and original, but still easy to understand.

* **RANDOMNESS = 1.0, IMPROVISATION = 1.0**

The generated music will be completely random and improvised. It will be difficult to understand what is happening.
