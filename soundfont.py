import sf2_loader as sf
loader = sf.sf2_loader("mega/Mega Man X1 Soundfont.sf2")
print(loader.sfid_list)
print(loader)
print(loader.get_all_instrument_names(sfid=None,
                               	bank=None,
                                max_num=128,
                                get_ind=False,
                                mode=0,
                                return_mode=0,
                                hide_warnings=True))

print("MOndá\n")
print(loader.get_all_instrument_names())
print("Todos los instrumentos\n")
print(loader.all_instruments())
loader.play_note('C5',
                 duration=2,
                 decay=1,
                 volume=100,
                 channel=0,
                 start_time=0,
                 sample_width=2,
                 channels=2,
                 frame_rate=44100,
                 name=None,
                 format='wav',
                 effects=None,
                 bpm=80,
                 export_args={},
                 wait=False)