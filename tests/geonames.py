import pgeocode

nomi = pgeocode.Nominatim('es')
print(nomi.query_postal_code("28027"))
