import queue
import json
import sounddevice as sd
import vosk
import phrases
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from functions import *



q = queue.Queue()
model = vosk.Model('vosk_model')

device = sd.default.device
samplerate = int(sd.query_devices(device, 'input')['default_samplerate'])

def callback(indata, frames, time, status):
    q.put(bytes(indata))

def recognize(data, vectoriser, clf):
    name = phrases.NAME.intersection(data.split())
    if not name:
        return

    data.replace(list(name)[0], "")
    text_vector = vectoriser.transform([data]).toarray()[0]
    answer = clf.predict([text_vector])[0]

    func_name = answer.split()[0]
    voice.speaker(answer.replace(func_name, ""))
    exec(func_name + "()")



def main():
    vectoriser = CountVectorizer()
    vectors = vectoriser.fit_transform(list(phrases.data_set.keys()))

    clf = LogisticRegression()
    clf.fit(vectors, list(phrases.data_set.values()))
    del phrases.data_set

    with sd.RawInputStream(samplerate=samplerate, blocksize=16000, device=device[0],
                           dtype="int16", channels=1, callback=callback):
        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                data = json.loads(rec.Result())['text']
                recognize(data, vectoriser, clf)

if __name__ == "__main__":
    main()

