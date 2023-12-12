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

def reproducir_nota_sample(sample_path, nota, duracion):
    # Cargar el sample de la guitarra con distorsión
    sample = AudioSegment.from_file(sample_path)

    # Frecuencia de la nota C5 (do)
    frecuencia_nota_c5 = 523.25

    # Calcular la relación de pitch para ajustar la frecuencia
    print("Nota que entra Dentro de la funcion", nota)
    ratio_pitch =   nota / frecuencia_nota_c5
    
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


ruta_sample = 'mega/Bass-Synth.wav'
#for nota in notas:

reference_frequency =  16.3516
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
print("Todas las frecuencias: ", Data_frame_notas,"\n")
print("C5: ",Data_frame_notas.loc['5','C'], "\n")
print("Frecuencias quinta octava:\n ", Data_frame_notas.loc['5'] , "\n")


#print(col_indices)
#print(n)
#print(octave)

#print(np.power(2,3))
# Notas: do, re, mi, fa, sol, la, si,do

#reproducir_nota_sample(ruta_sample,Data_frame_notas.loc['4','G'], duracion_nota)

#cumpleaños
#En quinta octava
# G4, G4, A4, G4, C5, ,B4
cancion = [['5','C'],['5','C'],['5','D'],['5','C'],['5','F'],['5','E']] #cumpleaños
#cancion = [['5','C'],['5','D'],['5','E'],['5','F'],['5','G'],['5','A'],['5','B']] # Do , remi ,fa,sol, la , si
print("----: ", cancion[0][0], "\n")
#print("consultando nota: ", ruta_sample,Data_frame_notas.loc[cancion[0][0],cancion[0][1]], "\n")
# Duración en milisegundos
duracion_nota = 20000
for nota in cancion:
    
    reproducir_nota_sample(ruta_sample,Data_frame_notas.loc[nota[0],nota[1]], duracion_nota)

    


    