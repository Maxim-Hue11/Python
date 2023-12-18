#p_name = 'Солмир'
#e_name = 'Сепхиноропф'
 
 
#player = {'name': str(p_name), 'health': 100, 'damage': 15}
#enemy = {'name': str(e_name), 'health': 80, 'damage': 19}
 
#def attack(attacker, defender):
#    defender['health'] = round(defender['health'] - armour(attacker, defender),2)
#    print('Игрок {} атаковал {} и оставил ему {} здоровья'.format(attacker['name'], defender['name'],
#    defender['health']))
#    health_loss = defender['health']
#    return health_loss

#player['armour'] = 1.2
#enemy['armour'] = 1.15
 
#def armour(attacker, defender):
#    red_attack = round(attacker['damage'] / defender['armour'],2)
#    print('Атака уменьшена на {} и составляет {}'.format(defender['armour'], red_attack))
#    return red_attack

#f = open(p_name, 'w', encoding='UTF-8')
#for line in player:
#    f.write(str(line))
#    f.write(' - ')
#    f.write(str(player.get(line)))
#    f.write('\n')
#f.close()
 
#f = open(e_name, 'w', encoding='UTF-8')
#for line in enemy:
#    f.write(str(line))
#    f.write(' - ')
#    f.write(str(enemy.get(line)))
#    f.write('\n')
#f.close()

#f = open(p_name, 'r', encoding='UTF-8')
 
#p1 = {}
#for line in f:
#    x,y = line.strip().split(' - ')
#    p1[x]= y
 
#f.close()
 
#f = open(e_name, 'r', encoding='UTF-8')
 
#p2 = {}
#for line in f:
#    x,y = line.strip().split(' - ')
#    p2[x]= y
 
#f.close()
 
#print(p1,'\n', p2)

#p1['health'] = round(float(p1['health']),2)
#p1['damage'] = round(float(p1['damage']),2)
#p1['armour'] = round(float(p1['armour']),2)
 
#p2['health'] = round(float(p2['health']),2)
#p2['damage'] = round(float(p2['damage']),2)
#p2['armour'] = round(float(p2['armour']),2)
 
 
 
#while p1['health'] > 0 and p2['health'] > 0:
#    if p1['health'] > 0:
#        p2['health'] = attack(p1,p2)
#    if p2['health'] > 0:
#        p1['health'] = attack(p2,p1)
 
#print()
 
#if p2['health'] > 0:
#    print('Победеил {}, остаток здоровья {}'.format(p2['name'],p2['health']))
#else:
#    print('Победеил {}, остаток здоровья {}'.format( p1['name'], p1['health']))