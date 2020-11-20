def woerter(text):
    text = text.lower()
    for p in '.,!?:-_;':
        text.replace(p)

    woerter = text.split()
    
    woerterbuch = []

    for i in len(woerter):
        for woert in woerter:
            