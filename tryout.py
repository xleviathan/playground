holderarr={'ch':0.02,'math':0.1,'phy':0.1,'bio':0.02}
mathget=int(input('Matematik sorusu sayisi: '))
chemget=int(input('Kimya sorusu sayisi: '))
phyget=int(input('Fizik sorusu sayisi: '))
bioget=int(input('Biyolji soru sayisi: '))
counter=mathget+phyget+bioget+chemget
def calculator():
    math=mathget*holderarr['math']
    ch=chemget*holderarr['ch']
    phy=phyget*holderarr['phy']
    bio=bioget*holderarr['bio']
    sum=math+ch+phy+bio
    return sum
if  counter >=150:
   print('Borcunuz:',calculator(),'TL')
else:
    print('Yetersiz soru sayisi.')