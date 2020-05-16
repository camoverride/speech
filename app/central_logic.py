"""
This module contains the AI class, which is the central logic of the conversation system. All other
central logical functions should be added to this class. Functions that do miscellaneous processing
work should be added in the `utils` module.
"""
from tts_front_end import g2p
from tts_back_end import tts
from common import NLP

class AI:
    """
    This class contains contains several private methods that are critical for creating a conversational
    AI, such as Automatic Speech Recognition (ASR), response generation, and Text to Speech (TTS). These
    are encapsulated in the public method `get_response` which accepts a user input and produces an output.

    Parameters
    ----------

    Methods
    -------


    """
    def __init__(self, user_info: str, use_convo_log: bool):
        if use_convo_log:
            self._user = self._get_user(user_info)
            self._convo_log = self._get_convo_logs(self._user)
        else:
            self._convo_log = []


    def _get_user(self, user_info: str):
        """
        This function attempts to get the user ID in order to query the database for a chat history.

        Parameters
        ----------
        user_info: str
            A string that describes the user.
        
        Returns
        -------
        str
            The ID of the user in the database. Returns NULL if the user is not in the database.
        """
        user_id = "NULL" # TODO: this is dummy data

        return user_id


    def _get_convo_logs(self, user):
        """
        This function takes a user id and queries the database, looking up the user's chat history
        from the last 10 minutes.
        """
        if user == "NULL":
            return []

        convo_log = [] # TODO: This is dummy data.

        return convo_log


    def _speech_to_text(self, sound_file):
        """
        This function accepts an sound file as input and performs ASR to convert the sound file
        into the corresponding text. It then adds this to `_convo_log`.

        Parameters
        ----------
        sound_file

        Output
        ------
        str
            A string that represents the `sound_file` that was input.
        """
        message = "hi robot, I'm a human" # TODO: this is dummy data

        # Add the message to the conversation log for later processing.
        self._convo_log.append({"Human": message}) # also write to database
        
        return message


    def _text_to_response(self, message: str):
        """
        This function accepts a message from the [human] interlocuter and chooses an appropriate response.
        It also makes use of the `convo_history` when generating its reply.

        Parameters
        ----------
        message: str
            A string that represents the message sent from the conversation partner.
        
        Output
        ------
        str
            An appropriate response to the incoming message.
        """
        response = message # TODO: this is dummy data...
        
        return response


    def _text_to_speech(self, response: str):
        """
        This function performs TTS by producing the audio file that corresponds to a given sentence.
        It then adds this response to `_convo_log`.

        Parameters
        ----------
        response: str
            The text file that will be converted to audio.

        Output:
        -------
        (str, audio)
            A tuple containing the text of the response and the path to the audio file associated with it.
        """
        # Perform g2p to convert the graphemes to phonemes.
        phonemes = g2p(response)

        # Send the phonetics to the audio server.
        audio_path = tts(phonemes)

        self._convo_log.append({"AI": response}) # also write to database
        
        return (response, audio_path)


    def get_response(self, message):
        """
        This function performs ASR, response generation, and TTS to return an audio file that can be used as
        a response to the client. If the incoming response is typed, then ASR is skipped.
        """
        # NLP object for basic cleaning of text.
        nlp = NLP()

        # Check to see whether the incoming message is a string or an audio file.
        if type(message) != str:
            message = self._speech_to_text(message)
    
        message = nlp.clean_text(message)
        
        response = self._text_to_response(message)
        response = nlp.clean_text(response)

        response = "this is a test ;)  ... Heres $5!"

        # Perform TTS.
        text, audio_file = self._text_to_speech(response)

        return text, audio_file


message = "this is a test ;)  ... Hope you enjoy $$$%%!"

convo_AI = AI(user_info="Cameron", use_convo_log=False)

_, audio_file_path = convo_AI.get_response(message)

print(audio_file_path)
