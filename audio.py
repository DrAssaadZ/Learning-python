import pyaudio
import wave
import speech_recognition as sr
import subprocess


def say(txt):
    subprocess.call('echo ' + txt+'|ptts', shell=True)


def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )

    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()


r = sr.Recognizer()


def init_speech():
    print("Listening...")
    play_audio('audio/Begin.wav')

    with sr.Microphone() as source:
        print("Say something")
        audio = r.listen(source)

    play_audio('audio/End.wav')

    cmd = ""

    try:
        cmd = r.recognize_google(audio)
    except:
        print("Failed to understand")

    print("The command:")
    print(cmd)
    say('you said '+cmd)

init_speech()
