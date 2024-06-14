def find_poisoned_duration(time_series, duration):
    damage=0
    poisoned_state=time_series[0]+duration
    for i in range (1,len(time_series))  :
        if time_series[i]>poisoned_state:
            damage=damage+duration
        else:
            damage=abs(time_series[i-1]-time_series[i])-1+damage
        if(i==(len(time_series)-1)):
            damage=damage+duration
        poisoned_state=time_series[i]+duration
    return damage

time_series = [1,3,100]
damage = find_poisoned_duration(time_series, 3)
print(damage)
