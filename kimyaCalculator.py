""""KIMYA CALCULATOR V1.0 
SIGNATURE:www.github.com/xleviathan/playground
Genel kimya hesaplamalari ve problemlerinde kullanilan ufak bir script.
Cok ileri problemler icin biraz bilek gucune ihtiyac duyabilirsiniz.
FONKSIYONLARIN GOREVLERI:Kendilerini aciklamalarinda belirtmislerdir.
h,c,r degiskenlerine dokunmayiniz.Onemli sabitlerdir.
Librarylere de dokunmayin.
GUI tasarimi yapmayi dusunuyorum.
@Date: 12.10,2017"""
from decimal import Decimal
h = 6.63*10**(-34)
c = 3*(10**8)
r = 2.18*10**(-18)
def delta_energy(atom,layer1,layer2):
    """"Katmanlar arasi enerji degisimi hesaplar."""
    global r,c,h
    return float('%.2E' % Decimal(str(r*((atom**2/layer1**2)-(atom**2/layer2**2)))))
def energy_atom(atom,layer):
    """"Tek katmanli enerji hesaplamalari yapar."""
    global r,c,h
    backval= r*((atom**2/layer**2))
    return float('%.2E' % Decimal(str(backval)))
def lightSpeed(waveLength,freq):
    """"Isik hizi formulunden yararlanarak frekans veya dalga boyu bulur."""
    global r,c,h
    getit = str(input("Dalga boyu ise d,frekans ise f girip entera basiniz.(direk isik hizi yok elimizde kalmamis."))
    if getit == "d":
        return float('%.2E' % Decimal(str(c / freq)))
    elif getit =="f":
        return float('%.2E' % Decimal(str(c/waveLength)))
    print("Yanlis girdi.Yeniden dene.")
    return lightSpeed(waveLength,freq)
def energy_Photon(freq=1.0,energy=0.0):
    """"Bir fotonun enerjisini hesaplar.Frekans da bulabilir."""
    global r,c,h
    if freq ==0:
        print("enerji yok...")
        return 0
    if energy != 0:
        energy =energy
    else:
        energy = h*freq
    getit =str(input("frekans bulmak istiyorsaniz f,yoksa bos gecin."))
    if getit =="f":
        return ('%.2E' % Decimal(str(energy/h)))
    return float('%.2E' % Decimal(str(energy)))
def energy_PhotonFormula(wave=1.0,energy=0.00):
    """"Bir fotonun enerjisini isik hizi formulunu kullanarak enerjisini hesaplar.Dalga boyu da bulabilir. """
    global r,c,h
    print("Enerji var ise lutfen giriniz.")
    if energy != 0:
        energy = energy
    else:
        energy=h*(c/wave)
    getit =str(input("Dalga boyunu istiyorsaniz d,enerji istiyorsaniz bos birakin."))
    if getit == 'd':
        return ('%.2E' % Decimal(str(energy/(h*c))))
    elif getit =="":
        ('%.2E' % Decimal(str(energy)))
    print("Yanlis girdi.Yeniden dene.")
    return energy_PhotonFormula(wave)
