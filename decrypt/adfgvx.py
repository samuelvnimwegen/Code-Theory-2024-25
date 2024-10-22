class ADFGVX:
    def __init__(self, morse_code: str):
        self.morse = morse_code

    def decrypt(self):
        # Convert the morse code to the corresponding characters.
        self.morse_decode()


    def morse_decode(self):
        # Map the morse code to the corresponding characters.
        morse = {'.-': 'A', '-..': 'D', '..-.': 'F', '--.': 'G', '...-' : 'V', '-..-': 'X'}

        # Split the morse code at every '/'.
        self.morse = self.morse.split('/')

        # Remove the last element ('/') if it exists.
        if self.morse[-1] == '':
            self.morse = self.morse[:-1]

        # Make sure the text is actually morse code.
        assert all([char in morse for char in self.morse]), 'Invalid morse code.'

        # Replace the morse code with the corresponding characters.
        self.morse = [morse[char] for char in self.morse]