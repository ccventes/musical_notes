from pydub import AudioSegment
from pydub.generators import Sine
from pydub.playback import play
import numpy as np
import pandas as pd

def reproducir_nota(nota, duracion,fg):
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

# Notas: do, re, mi, fa, sol, la, si,do
notas = [60, 62, 64, 65, 67,  69, 71,73,75,77,78, 80,82,84]

def reproducir_nota_sample(sample_path, nota, duracion):
    # Cargar el sample de la guitarra con distorsión
    sample = AudioSegment.from_file(sample_path)

    # Frecuencia de la nota C5 (do)
    frecuencia_nota_c5 = 523.25

    # Calcular la relación de pitch para ajustar la frecuencia
    ratio_pitch = 2 ** ((nota - 60) / 12.0)
    
    print("\n FRAME RATE: ", sample.frame_rate , " FRAME RATE * ratio_pitch ", sample.frame_rate * ratio_pitch, "nota: ",523.25 * ratio_pitch, "\n ")
    # Ajustar la frecuencia del sample según la nota deseada
    sample_nota = sample._spawn(sample.raw_data, overrides={
        "frame_rate": int(sample.frame_rate * ratio_pitch)
    })

    # Ajustar la duración del sample
    sample_nota = sample_nota[:duracion]

    # Reproducir la nota
    play(sample_nota)
    return ratio_pitch

# Ruta al archivo del sample de la guitarra con distorsión
ruta_sample = 'mega/Bass-Synth.wav'

frecuencias_generadas = []
# Reproducir cada nota

def get_note_name(note):
    note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    return note_names[note]


#for nota in notas:

reference_frequency =  16.3516

# Generar una tabla de frecuencias para las notas de la octava 0 a la octava 10
frequency_table = []
for octave in range(11):
    for note in range(12):
        # Fórmula para calcular la frecuencia
        frequency = reference_frequency * (2 ** ((octave - 4) + (note / 12)))

        # Agregar la frecuencia y la nota a la tabla
        frequency_table.append({
            'note': f"{get_note_name(note)}{octave}",
            'frequency': round(frequency, 2),
        })

n = np.arange(1,13)
octave = np.arange(1,11)
notes = np.zeros((11,12)) # 10 filas octavas , 12 columnas semitonos
#notes[0,0] = 16.3516
np.set_printoptions(linewidth=np.inf)
np.set_printoptions(suppress=True)
row_indices, col_indices = np.indices(notes.shape)
#notes = row_indices * col_indices
notes = reference_frequency * np.power(2, (( col_indices  ) + ( (row_indices * 12) ))/12 ) # generación matematica de las frecuencias de las notas
note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
#print(notes)
# Crear un DataFrame de pandas con las frecuencias
Data_frame_notas = pd.DataFrame(notes, index=['0', '1', '2','3', '4', '5','6', '7', '8','9', '10'], columns = note_names)
print(Data_frame_notas)
print(Data_frame_notas.loc['5','C'])


#print(col_indices)
#print(n)
#print(octave)

#print(np.power(2,3))

    
#for entry in frequency_table:
    #print(entry)
    # Duración en milisegundos
    #duracion_nota = 3000
    #reproducir_nota(nota, duracion_nota)
    #frecuencias_generadas.append(reproducir_nota_sample(ruta_sample,nota, duracion_nota))
    
    

    