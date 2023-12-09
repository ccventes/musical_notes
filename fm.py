from pydub import AudioSegment
import numpy as np
from pydub.generators import Sine
from pydub.playback import play

def fm_synth(note_freq, duration, modulator_freq, modulation_index=2.0):
    # Frecuencia de muestreo
    sample_rate = 44100

    # Generar tiempo
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

    # Generar la onda moduladora
    modulator = np.sin(2 * np.pi * modulator_freq * t)

    # Generar la onda portadora
    carrier = np.sin(2 * np.pi * note_freq * t + modulation_index * np.sin(2 * np.pi * modulator_freq * t))

    # Normalizar y escalar la onda
    envelope = np.exp(-5.0 * t)  # Envelope exponencial para simular la caída del tono
    envelope /= np.max(envelope)

    # Combinar portadora, moduladora y aplicar el envelope
    output_wave = (0.3 * carrier * envelope).astype(np.int16)

    return output_wave

def play_wave(wave):
    audio = AudioSegment(wave.tobytes(), frame_rate=44100, sample_width=wave.dtype.itemsize, channels=1)
    audio.export("piano_note.wav", format="wav")
    audio.export("piano_note.mp3", format="mp3")
    play(audio)

if __name__ == "__main__":
    # Frecuencia de la nota de piano (por ejemplo, A4)
    note_frequency = 440.0

    # Frecuencia de la onda moduladora (ajustar según sea necesario)
    modulator_frequency = 5.0

    # Duración de la nota en segundos
    note_duration = 2.0

    # Sintetizar la nota
    piano_note = fm_synth(note_frequency, note_duration, modulator_frequency)

    # Reproducir o exportar la nota
    play_wave(piano_note)