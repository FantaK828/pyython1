def mult_egyptienne(m,f):

        resultat=0

        while m!=0:

            if m%2==1:

                resultat+=f

            m>>=1

            f=f+f

        return resultat



var = mult_egyptienne(22,3)

print(var)