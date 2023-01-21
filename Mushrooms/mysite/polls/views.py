from django.shortcuts import render, redirect
import pandas as pd
import pickle

def index_func(request):
    res = 0
    if request.method == 'POST':
        capShape = request.POST['capShape']
        CapSurface = request.POST['CapSurface']
        capColor = request.POST['capColor']
        bruises = request.POST['bruises']
        odor = request.POST['odor']
        gillAttach = request.POST['gillAttach']
        gillSpace = request.POST['gillSpace']
        gillSize = request.POST['gillSize']
        gillColor = request.POST['gillColor']
        stalkShape = request.POST['stalkShape']
        stalkRoot = request.POST['stalkRoot']
        stalkARing = request.POST['stalkARing']
        stalkBRing = request.POST['stalkBRing']
        stalkCARing = request.POST['stalkCARing']
        stalkCBRing = request.POST['stalkCBRing']
        veilType = request.POST['veilType']
        veilColor = request.POST['veilColor']
        ringNumber = request.POST['ringNumber']
        ringType = request.POST['ringType']
        sporePrintColor = request.POST['sporePrintColor']
        pop = request.POST['pop']
        hab = request.POST['hab']

        if capShape != "":
            df = pd.DataFrame(columns=['cap-shape','cap-surface','cap-color','bruises','odor',
                                       'gill-attachment','gill-spacing','gill-size','gill-color',
                                       'stalk-shape','stalk-root','stalk-surface-above-ring',
                                       'stalk-surface-below-ring','stalk-color-above-ring',
                                       'stalk-color-below-ring','veil-type','veil-color','ring-number',
                                       'ring-type','spore-print-color','population','habitat'])

            df2 = {'cap-shape': int(capShape),'cap-surface': int(CapSurface),'cap-color': int(capColor),
                   'bruises': int(bruises),'odor': int(odor),'gill-attachment': int(gillAttach),
                   'gill-spacing': int(gillSpace),'gill-size': int(gillSize),'gill-color': int(gillColor),
                    'stalk-shape': int(stalkShape),'stalk-root': int(stalkRoot),'stalk-surface-above-ring':
                    int(stalkARing),'stalk-surface-below-ring': int(stalkBRing),'stalk-color-above-ring':
                    int(stalkCARing),'stalk-color-below-ring': int(stalkCBRing),'veil-type': int(veilType),
                   'veil-color': int(veilColor),'ring-number': int(ringNumber),'ring-type': int(ringType),
                   'spore-print-color': int(sporePrintColor),'population': int(pop),'habitat': int(hab)}

            df = df.append(df2, ignore_index=True)
            # load the model from disk
            filename = 'polls/MushsPCA.pickle'
            pca = pickle.load(open(filename, 'rb'))
            data = pca.transform(df)
            filename1 = 'polls/Mushs.pickle'
            loaded_model = pickle.load(open(filename1, 'rb'))

            res = loaded_model.predict(data)
            print(res) # ['e' 'p'] -> [0, 1] -> (classes: edible=e, poisonous=p)

            if res[0] == 0:
                res = 'edible'
            else:
                res = 'poisonous'
        else:
            return redirect('homepage')
    else:
        pass

    return render(request, "index.html", {'response': res})
