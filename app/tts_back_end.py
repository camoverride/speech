"""
Utilities relating to Text-to-Speech Front-End. The FE is responsible for
producing a phoneme that can be interpreted by the Back-End and converted into
a waveform.
"""

import os


def tts(phonemes: str, audio_path: str="tmp_data/audio.aiff"):
    """
    Takes a list of phonemes and writes a sound file.

    Parameters
    ----------
    phonemes: str
        Phonemes encoded using TODO: decide which encoding.
    
    audio_location: str
        A path to write the audio file to, including the filename. i.e. `tmp/audio.wav`
    
    Returns
    -------
    str
        The path to the audio file.
    """
    os.system(f"say {phonemes} --output-file={audio_path}")

    return audio_path
