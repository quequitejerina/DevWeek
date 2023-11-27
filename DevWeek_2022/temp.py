import requests
  
# Making a get request
response = requests.get('https://dev-challenge-22.eastus.cloudapp.azure.com/assets/temperatures001.json')
  
temp_list = response.json()['temperatures']
date = ''
biggest_temp_dif = 0
last_temp_f = int(temp_list[0]['temperature'])
last_temp_dif = 0
for day in temp_list:
    if day['unit'] == 'fahrenheit':
        temp = (int(day['temperature']) - 32) * 0.555
    else:
        temp = int(day['temperature'])
    temp_dif = temp - last_temp_f
    print(temp_dif)
    print(last_temp_dif)
    if temp_dif > biggest_temp_dif:
        date = day['date']
        biggest_temp_dif = temp_dif
    print(date)
    last_temp_dif = temp_dif