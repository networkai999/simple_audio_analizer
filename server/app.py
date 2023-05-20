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

# initialize flask api
app = Flask(__name__)
CORS(app)


# object that will be returned to the client
class FileAnalized:
  def __init__(self, sample_rate, bits_per_sample,duration,num_channels):
    self.sample_rate = sample_rate
    self.bits_per_sample = bits_per_sample
    self.duration = duration
    self.num_channels = num_channels





@app.route('/upload', methods=['POST'])
def upload():
  # Check if there is a WAV file in the POST request
  if 'audio' not in request.files:
    return {'error': 'No WAV files received.'}, 400

  file = request.files['audio']

  # Check the file extension
  if file.filename == '' or not file.filename.endswith('.wav'):
    return {'error': 'Invalid WAV file.'}, 400

  # Save the WAV file to disk
  filename = f'{str(uuid.uuid4())}_audio.wav'
  file.save(filename)
  file.close()

  resultJson = analizeFile(filename)

  # return response to client
  return resultJson
 


# function that takes care 
# of analyzing the wav audio 
# file and returning its specifications
def analizeFile(filename):

  f = wavfile.open(filename,'r')

  # create the final object
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



