def son():

    from grupkel import grupkel
    import random

    grupis=grupkel()

    cogul=['lar','lar','ler','ler']

    ekler=[['sız','suz','siz','süz'],
     ['cı','cu','ci','cü'],
     ['lık','luk','lik','lük'],
     ['sal','sal','sel','sel'],
     ['daş','daş','deş','deş'],
     ['ca','ca','ce','ce'],
     ['dan','dan','den','den'],
     ['da','da','de','de']]

    eklerfis=[['sız','suz','siz','süz'],
     ['çı','çu','çi','çü'],
     ['lık','luk','lik','lük'],
     ['sal','sal','sel','sel'],
     ['taş','taş','teş','teş'],
     ['ça','ça','çe','çe'],
     ['tan','tan','ten','ten'],
     ['ta','ta','te','te']]

    zar2=random.randint(0,7)
    zar3=random.randint(0,7)
    zar4=random.randint(0,7)


    if len(grupis) == 1:
        zar=random.randint(1, 100)
        zar2=random.randint(0,7)
        if grupis[0][2]==1:
            if zar>84:
                grupadi=grupis[0][0]+eklerfis[zar2][grupis[0][1]]+cogul[grupis[0][1]]

            elif zar<85 and zar>55:
                grupadi=grupis[0][0]+eklerfis[zar2][grupis[0][1]]

           
            elif zar<33:
                grupadi=grupis[0][0]+cogul[grupis[0][1]]

            else:
                grupadi='Grup'+' '+grupis[0][0]
        else:
            if zar>84:
                grupadi=grupis[0][0]+ekler[zar2][grupis[0][1]]+cogul[grupis[0][1]]

            elif zar<85 and zar>60:
                grupadi=grupis[0][0]+ekler[zar2][grupis[0][1]]

            elif zar<8:
                grupadi='Grup'+' '+grupis[0][0]

            elif zar>8 and zar<25:
                grupadi=grupis[0][0]+cogul[grupis[0][1]]
            else:
                grupadi=grupis[0][0]
            

    elif len(grupis) == 2:
        zar=random.randint(1, 100)
        zar2=random.randint(0,7)
        if zar>88:
            grupadi=grupis[0][0]+' '+grupis[1][0]+cogul[grupis[1][1]]

        elif zar<89 and zar>81:
            if grupis[0][2]==1:
                grupadi=grupis[0][0]+eklerfis[zar2][grupis[0][1]]+' '+grupis[1][0]
            else:
                grupadi=grupis[0][0]+eklerfis[zar2][grupis[0][1]]+' '+grupis[1][0]
        elif zar<82 and zar>77:
            if grupis[0][2]==1:
                grupadi=grupis[0][0]+eklerfis[zar2][grupis[0][1]]+' '+grupis[1][0]+cogul[grupis[1][1]]
            else:
                grupadi=grupis[0][0]+eklerfis[zar2][grupis[0][1]]+' '+grupis[1][0]+cogul[grupis[1][1]]
        elif zar<10:
             if grupis[0][2]==1:
                 if grupis[1][2]==1: 
                    grupadi=grupis[0][0]+eklerfis[zar2][grupis[0][1]]+' '+grupis[1][0]+eklerfis[zar2][grupis[1][1]]
                 else:
                     grupadi=grupis[0][0]+eklerfis[zar2][grupis[0][1]]+' '+grupis[1][0]+ekler[zar2][grupis[1][1]]
             else:
                 if grupis[1][2]==1: 
                    grupadi=grupis[0][0]+ekler[zar2][grupis[0][1]]+' '+grupis[1][0]+eklerfis[zar2][grupis[1][1]]
                 else:
                     grupadi=grupis[0][0]+ekler[zar2][grupis[0][1]]+' '+grupis[1][0]+ekler[zar2][grupis[1][1]]
        else:
            grupadi= grupadi=grupis[0][0]+' '+grupis[1][0]


    elif len(grupis) == 3:
        zar=random.randint(1, 100)
        
        if zar>78:
            if grupis[0][2]==1:
                grupadi=grupis[0][0]+eklerfis[zar2][grupis[0][1]]+' '+grupis[1][0]+' '+grupis[2][0]+cogul[grupis[2][1]]
            else:
                grupadi=grupis[0][0]+ekler[zar2][grupis[0][1]]+' '+grupis[1][0]+' '+grupis[2][0]+cogul[grupis[2][1]]

        elif zar<78 and zar>66:
            if grupis[0][2]==1:
                if grupis[1][2]==1:
                    grupadi=grupis[0][0]+eklerfis[zar2][grupis[0][1]]+' '+grupis[1][0]+eklerfis[zar3][grupis[1][1]]+' '+grupis[2][0]+cogul[grupis[2][1]]
                else:
                    grupadi=grupis[0][0]+eklerfis[zar2][grupis[0][1]]+' '+grupis[1][0]+ekler[zar3][grupis[1][1]]+' '+grupis[2][0]+cogul[grupis[2][1]]
            else:
                if grupis[1][2]==1:
                    grupadi=grupis[0][0]+ekler[zar2][grupis[0][1]]+' '+grupis[1][0]+eklerfis[zar3][grupis[1][1]]+' '+grupis[2][0]+cogul[grupis[2][1]]
                else:
                    grupadi=grupis[0][0]+ekler[zar2][grupis[0][1]]+' '+grupis[1][0]+ekler[zar3][grupis[1][1]]+' '+grupis[2][0]+cogul[grupis[2][1]]
        
        elif zar<66 and zar>60:
            if grupis[0][2]==1:
                if grupis[1][2]==1:
                    if grupis[2][2]==1:
                        grupadi=grupis[0][0]+eklerfis[zar2][grupis[0][1]]+' '+grupis[1][0]+eklerfis[zar3][grupis[1][1]]+' '+grupis[2][0]+eklerfis[zar4][grupis[2][1]]
                    else:
                        grupadi=grupis[0][0]+eklerfis[zar2][grupis[0][1]]+' '+grupis[1][0]+eklerfis[zar3][grupis[1][1]]+' '+grupis[2][0]+ekler[zar4][grupis[2][1]]
                else:
                    if grupis[2][2]==1:
                        grupadi=grupis[0][0]+eklerfis[zar2][grupis[0][1]]+' '+grupis[1][0]+ekler[zar3][grupis[1][1]]+' '+grupis[2][0]+eklerfis[zar4][grupis[2][1]]
                    else:
                        grupadi=grupis[0][0]+eklerfis[zar2][grupis[0][1]]+' '+grupis[1][0]+ekler[zar3][grupis[1][1]]+' '+grupis[2][0]+ekler[zar4][grupis[2][1]]
            else:
                if grupis[1][2]==1:
                    if grupis[2][2]==1:
                        grupadi=grupis[0][0]+ekler[zar2][grupis[0][1]]+' '+grupis[1][0]+eklerfis[zar3][grupis[1][1]]+' '+grupis[2][0]+eklerfis[zar4][grupis[2][1]]
                    else:
                        grupadi=grupis[0][0]+ekler[zar2][grupis[0][1]]+' '+grupis[1][0]+eklerfis[zar3][grupis[1][1]]+' '+grupis[2][0]+ekler[zar4][grupis[2][1]]
                else:
                    if grupis[2][2]==1:
                        grupadi=grupis[0][0]+ekler[zar2][grupis[0][1]]+' '+grupis[1][0]+ekler[zar3][grupis[1][1]]+' '+grupis[2][0]+eklerfis[zar4][grupis[2][1]]
                    else:
                        grupadi=grupis[0][0]+ekler[zar2][grupis[0][1]]+' '+grupis[1][0]+ekler[zar3][grupis[1][1]]+' '+grupis[2][0]+ekler[zar4][grupis[2][1]]


        elif zar<60 and zar>50:
            if grupis[0][2]==1:
                grupadi=grupis[0][0]+eklerfis[zar2][grupis[0][1]]+cogul[grupis[0][1]]+' '+grupis[1][0]+' '+grupis[2][0]
            else:
                grupadi=grupis[0][0]+ekler[zar2][grupis[0][1]]+cogul[grupis[0][1]]+' '+grupis[1][0]+' '+grupis[2][0]  
        else:
            if grupis[0][2]==1:
                grupadi=grupis[0][0]+eklerfis[zar2][grupis[0][1]]+' '+grupis[1][0]+' '+grupis[2][0]
            else:
                grupadi=grupis[0][0]+ekler[zar2][grupis[0][1]]+' '+grupis[1][0]+' '+grupis[2][0]     

    return grupadi
