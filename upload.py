from pydub import AudioSegment
import os

def convert_to_wav(input_file):
    # Load the input audio file
    audio = AudioSegment.from_file(input_file)

    # Create the output file path with the .wav extension
    output_file = os.path.splitext(input_file)[0] + '.wav'

    # Convert to WAV format
    audio.export(output_file, format='wav')

def save_file(file):
    current_dir = os.getcwd()
    audio_dir = os.path.join(current_dir,"audio")
    # Join the current directory with the filename
    file_path = os.path.join(audio_dir, file.filename)
    # Save the file to the specified path
    file_path = os.path.join(audio_dir, file.filename)
    file.save(file_path)
    convert_to_wav(file_path)

    return 'File saved successfully'