import json
import urllib3
from datetime import datetime
now = datetime.now()
ts = str(now).split(' ')[0]

def get_transcript(timedtext_url):
    http = urllib3.PoolManager()
    handle = http.request('GET', timedtext_url)
    contents = handle.data.decode('utf-8')
    json_contents = json.loads(contents)

    events = json_contents['events']
    running_words = []

    for event in events:
        if 'segs' in event:
            segs = event['segs']
            if (len(segs)) > 0:
                for i in range(len(segs)):
                    # look thru segs list
                    running_words.append(segs[i]['utf8'])
            else:
                if (seg[0]['utf8'] == '\n'):
                    running_words.append(" ")
                else:
                    running_words.append(seg['utf8'])
    final_text = " ".join(running_words)
    # print(final_text)

    with open(f'results-{ts}.txt', 'w') as f:
        f.write(final_text)
    return


get_transcript('https://www.youtube.com/api/timedtext?v=K-9Si3w-AhE&caps=asr&xoaf=5&hl=en&ip=0.0.0.0&ipbits=0&expire=1650411614&sparams=ip%2Cipbits%2Cexpire%2Cv%2Ccaps%2Cxoaf&signature=EADD8DD1C4C066FD5A09BF64378E3C8456619E03.DC0FD58560539A73E8F92E34D3B818144F7A66FE&key=yt8&kind=asr&lang=en&fmt=json3&xorb=2&xobt=3&xovt=3')
