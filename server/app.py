from functools import wraps
import wavfile
import json
import base64
from PIL import Image
from flask import Flask, abort, jsonify, request
import uuid
from flask_cors import CORS
import os
import secrets


app = Flask(__name__)
CORS(app)

class FileAnalized:
  def __init__(self, sample_rate, bits_per_sample,duration,num_channels):
    self.sample_rate = sample_rate
    self.bits_per_sample = bits_per_sample
    self.duration = duration
    self.num_channels = num_channels





@app.route('/upload', methods=['POST'])
def upload():
  # Verifica se è presente un file WAV nella richiesta POST
  if 'audio' not in request.files:
    return {'error': 'Nessun file WAV ricevuto.'}, 400

  file = request.files['audio']

  # Verifica l'estensione del file
  if file.filename == '' or not file.filename.endswith('.wav'):
    return {'error': 'File WAV non valido.'}, 400

  # Salva il file WAV su disco
  filename = f'{str(uuid.uuid4())}_audio.wav'
  file.save(filename)
  file.close()

  resultJson = analizeFile(filename)

  # return response to client
  return resultJson
 



def analizeFile(filename):

  f = wavfile.open(filename,'r')


  _fileanalized = FileAnalized(f.sample_rate,f.bits_per_sample,f.duration,f.num_channels)

  f.close()

  jsonStr = json.dumps(_fileanalized.__dict__)
  json_object = json.loads(jsonStr)
  json_formatted_str = json.dumps(json_object, indent=2)

  if _fileanalized.sample_rate >= 44100:
    print("good quality!")

  print(json_formatted_str)

  try:
    os.remove(filename)
    print("File deleted successfully.")
  except OSError as e:
      print(f"Error deleting the file: {e}")

  return json_formatted_str




if __name__ == '__main__':
  app.run()



