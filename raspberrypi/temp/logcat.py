from datetime import datetime 

def logcat(message):
    now = datetime.now().strftime('[%d/%b/%Y %H:%M:%S]')
    print(f'{now} {message}')
