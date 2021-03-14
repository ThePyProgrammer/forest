# audio
from forest._importable import LazyImport


playsound = LazyImport('from playsound import playsound', "FUNCTION playsound.playsound('/path.to/a/sound/file/you/want/to/play.mp3 | URL', block=True) — Function to playing sound file with filetype WAVE and MP3, derived from 'from playsound import playsound', from https://github.com/TaylorSMarks/playsound")

sa = LazyImport('import simpleaudio as sa', "PACKAGE sa derived from simpleaudio — A cross-platform dependency-free asynchronous simple audio playback Python extension, derived from 'import simpleaudio as sa', from https://github.com/hamiltron/py-simple-audio, Documentation: https://simpleaudio.readthedocs.io/en/latest/")
simpleaudio = LazyImport('import simpleaudio', "PACKAGE simpleaudio — A cross-platform dependency-free asynchronous simple audio playback Python extension, derived from 'import simpleaudio', from https://github.com/hamiltron/py-simple-audio, Documentation: https://simpleaudio.readthedocs.io/en/latest/")
fc = LazyImport("from simpleaudio import functionchecks as fc", "SUBPACKAGE fc derived from simpleaudio.functionchecks — Quick Function Check for simpleaudio package, derived from 'import simpleaudio.functionchecks as fc', from https://github.com/hamiltron/py-simple-audio, Documentation: https://simpleaudio.readthedocs.io/en/latest/")

winsound = LazyImport('import winsound', "LIBRARY winsound — Sound-playing interface for Windows, derived from 'import winsound', from The Python Standard Library")
beep = LazyImport('from winsound import Beep as beep')

sd = LazyImport('import sounddevice as sd', "PACKAGE sd derived from sounddevice — Play and Record Sound with Python, derived from 'import sounddevice as sd', from https://github.com/spatialaudio/python-sounddevice, Documentation: https://python-sounddevice.readthedocs.io/en/0.3.15/")
sounddevice = LazyImport('import sounddevice', "PACKAGE sounddevice — Play and Record Sound with Python, derived from 'import sounddevice', from https://github.com/spatialaudio/python-sounddevice, Documentation: https://python-sounddevice.readthedocs.io/en/0.3.15/")

sf = LazyImport('import soundfile as sf', "PACKAGE sf derived from soundfile — SoundFile is an audio library based on libsndfile, CFFI and NumPy, derived from 'import soundfile as sf', from https://github.com/bastibe/SoundFile")
soundfile = LazyImport('import soundfile', "PACKAGE soundfile — SoundFile is an audio library based on libsndfile, CFFI and NumPy, derived from 'import soundfile', from https://github.com/bastibe/SoundFile")

AudioSegment = LazyImport('from pydub import AudioSegment', "CLASS pydub.AudioSegment — Classes that contain Audio Segments, derived from 'from pydub import AudioSegment', from https://github.com/jiaaro/pydub, Documentation: https://github.com/jiaaro/pydub/blob/master/API.markdown")
pydub = LazyImport('import pydub', "PACKAGE pydub — Manipulate audio with a simple and easy high level interface, derived from 'import pydub', from https://github.com/jiaaro/pydub, Documentation: https://github.com/jiaaro/pydub/blob/master/API.markdown")
playwav = LazyImport('from pydub.playback import play as playwav', "FUNCTION playwav derived from pydub.playback.play — Play WAV-based AudioSegment Objects, derived from 'from pydub.playback import play as playwav', from https://github.com/jiaaro/pydub, Documentation: https://github.com/jiaaro/pydub#playback")

wave = LazyImport('import wave', "LIBRARY wave — Read and write WAV files, derived from 'import wave', from The Python Standard Library")

pyaudio = LazyImport('import pyaudio', "PACKAGE pyaudio — Python Bindings for PortAudio, derived from 'import pyaudio', from https://github.com/jleb/pyaudio, Documentation: http://people.csail.mit.edu/hubert/pyaudio/docs/")
