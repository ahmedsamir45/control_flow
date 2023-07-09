peoples = ['Osama','Ahmed','Sayed','Ali']
skils = ['Html','Css','js']

for name in peoples: # outer loop
    print(f"{name} skils is: ")

    for skil in skils: # inner loop
        print(f'-{skil}')
