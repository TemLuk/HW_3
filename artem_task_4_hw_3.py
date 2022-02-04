earth_days, earth_hours = int(input("Количество земных дней:")), int(input("Количество земных часов:"))
sol = 1.02595675
earth_days_1 = earth_hours / 24
mars_hours = (earth_days + earth_days_1) / sol
print('Количество марсианских сол:' + str(round(mars_hours, 2)))

