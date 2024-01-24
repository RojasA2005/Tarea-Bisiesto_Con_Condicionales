year = input("Ingrese un año entre 1900 y 2199 ")
year = int(year)
leap_year_count = 0


if year >= 1900 and year <= 2199:
    leap_year_count += (year - 1900) // 4
    if year >= 2100:
        leap_year_count += -1

print(leap_year_count)