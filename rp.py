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