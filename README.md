# Simple audio analizer

Simple analysis of wav audio. 
This analysis of audio files is similar to what we use in our ***Dapp*** **Music Central** , precisely to maintain an optimal range of audio quality.

### Project structure
The project contains a client-side and a server-side , so the side will take care of uploading the audio file and calling the server-side api that will parse the incoming file and respond to our client. 

&nbsp; - **root** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **server** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *app.py* <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *requirements.txt* <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**client** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *fileuplad.html* <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *style.css*

### Prerequisites
- ***python3***


### Step of installing useful dependencies
- First take care of setting up your environment , so install python.
- Clone repository.
- Once you clone the repository you will see 2 folders in the root, the **client** folder and the **server** folder. Access the server folder.
```powershell
cd server
```
- After going to the server folder install the dependencies useful for our python api
Then run the command below
```python
pip install -r requirements.txt
```

### Activate python server 
- Once you have installed the dependencies properly , make sure you are in the **server** folder where we have our **app.py** file and then run the command below.
```python
python -m flask run
```

- Now in your terminal you will see that the server is active on your local host and listening on port 5000, on your terminal you will see a message like the one below
```powershell
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```
- Well our server side is up , now open in the browser the fileupload.html located in the client folder.
Once open in the web perform the upload of the audio file , invoke the server side with the upload button and wait for the response.

- The subject of the response will be like the one below , obviously the values will depend on the audio file taken into analysis.
```json
{
  "sample_rate": 44100,
  "bits_per_sample": 16,
  "duration": 217.85095238095238,
  "num_channels": 2
}
```

## What is an Audio Sample Rate and What Sample Rate Should I Record At?

### Sample Rate: A Definition
Simply put, the sample rate is the number of times per second audio is sampled. For instance, at a sample rate of 44.1 kHz, the waveform is captured 44100 times per second.

### The Most Common Sample Rates
The higher the sampling rate, the more accurate the sound wave representation will be. Lower sampling rates mean fewer samples per second. With less audio data, the audio representation will be approximate, to some extent.

The most common sampling rate values are **44.1 kHz** and **48 kHz**. **44.1 kHz** is the standard rate for audio CDs. Generally, movies use **48 kHz** audio. Even though both sample rates can accurately capture the entire frequency spectrum of human hearing, music producers and engineers often choose to use higher sample rates to create hi-res recordings.

*Read the full article on the webpage* https://crumplepop.com/what-sample-rate-should-i-record-at/