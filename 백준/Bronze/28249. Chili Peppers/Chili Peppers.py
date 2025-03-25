#28249 Chili Peppers

d  = {
    "Poblano" :	1500,
    "Mirasol" :	6000,
    "Serrano": 15500,
    "Cayenne" :	40000,
    "Thai" : 75000,
    "Habanero" : 125000
    }

N = int(input())
print(sum([d[input()] for i in range(N)]))