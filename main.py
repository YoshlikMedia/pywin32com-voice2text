import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

while True:
    print('Matn kiriting!(Ingliz tilida):')
    s = input()
    if s == 'exit':
        break
    else:
        speaker.Speak(s)