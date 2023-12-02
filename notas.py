from pydub import AudioSegment
from pydub.generators import Sine
from pydub.playback import play

def reproducir_nota(nota, duracion):
    # Frecuencia de la nota C5 (do)
    frecuencia_nota_c5 = 523.25

    # Calcular la frecuencia de la nota deseada
    frecuencia_nota = frecuencia_nota_c5 * (2 ** ((nota - 60) / 12.0))

    # Generar una onda senoidal para la nota
    onda_senoidal = Sine(frecuencia_nota).to_audio_segment(duration=duracion)

    # Reproducir la nota
    play(onda_senoidal)

# Duración en milisegundos
duracion_nota = 500

# Notas: do, re, mi, fa, sol, la, si
notas = [60, 62, 64, 65, 67, 69, 71]

def reproducir_nota_sample(sample_path, nota, duracion):
    # Cargar el sample de la guitarra con distorsión
    sample = AudioSegment.from_file(sample_path)

    # Frecuencia de la nota C5 (do)
    frecuencia_nota_c5 = 523.25

    # Calcular la relación de pitch para ajustar la frecuencia
    ratio_pitch = 2 ** ((nota - 60) / 12.0)

    # Ajustar la frecuencia del sample según la nota deseada
    sample_nota = sample._spawn(sample.raw_data, overrides={
        "frame_rate": int(sample.frame_rate * ratio_pitch)
    })

    # Ajustar la duración del sample
    sample_nota = sample_nota[:duracion]

    # Reproducir la nota
    play(sample_nota)

# Ruta al archivo del sample de la guitarra con distorsión
ruta_sample = 'mega/Bass-Synth.wav'

# Reproducir cada nota
for nota in notas:
    # Duración en milisegundos
    duracion_nota = 3000
    #reproducir_nota(nota, duracion_nota)
    reproducir_nota_sample(ruta_sample,nota, duracion_nota)