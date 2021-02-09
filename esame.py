class ExamException(Exception): #eccezioni
  pass

class CSVTimeSeriesFile:
  
  def __init__(self, name =""): #inizializzare l’oggetto
      self.name = name

  def get_data(self): # metodo che restituisce la lista
    time_series=[]
    try: # provo aprire il file
        file = open(self.name, "r")
    except:
        raise ExamException ("il file è impossibile aprire\n")

    for line in file:
        unita = line.split(",") #splitare ogni linea quando incontra |,|
        if len(unita) >=2:
            if unita[0] != "epoch":
                timestamp = int(unita[0]) #converto in int e salvo in una timestamp
                if timestamp < 0:
                    raise ExamException("il numero non è valido")
                temperature = float(unita[1]) #converto in float e salvo in temperature
                time_series.append([timestamp, temperature])
                #salvo tutto in un vettore
        else:
            print('questa linea"{}"non è valida'.format(line))

    for i in range(0, len(time_series)-1): #controllo che sono tutte in ordine
            if time_series[i][0]>=time_series[i+1][0]:
                raise ExamException("ci sono errore di ordine :)")
    file.close()
    return time_series
"""
-*-*-*-*-*-*-*-*-*-*-*-
"""
def daily_stats(time_series):
  giornate =[] #aggiungo le giornate
  listes =[]   #aggiungo le temperature 
  tripletta_temperatura =[] #inserisco i risultati finali
  
  for epoch in time_series:
    day_start_epoch = epoch[0] - (epoch[0] % 86400)
    if day_start_epoch not in giornate:
      giornate.append(day_start_epoch) # controllo le giornate
      listes.append([]) #aggiungo una lista vuota
    listes[giornate.index(day_start_epoch)].append(epoch[1]) #aggiungo lista nella lista
  for indice in listes: #trovo il min/max e calcolo la media
    tripletta_temperatura.append([min(indice), max(indice), sum(indice)/len(indice)])
  
  return tripletta_temperatura
"""
-*-*-*-*-*-*-*-*-*-*-*-
"""
time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
print(daily_stats(time_series))
