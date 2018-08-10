import json

with open('pu_data.json') as json_data:
    pu_save = json.load(json_data)

pu_value_total = 0.0

pu_inactive_count = 0.0
pu_active_count = 0.0
pu_inactive_value_total = 0.0
pu_active_value_total = 0.0

pu_nonpremium_count = 0.0
pu_premium_count = 0.0
pu_nonpremium_value_total = 0.0
pu_premium_value_total = 0.0

pu_premium_inactive_count = 0.0
pu_premium_inactive_value_total = 0.0

pu_premium_active_count = 0.0
pu_premium_active_value_total = 0.0


pu_country_dict = {}



for i in pu_save:
    
    pu_value_total += pu_save[i]['value']
    
    if pu_save[i]['country'] in pu_country_dict:
        if pu_save[i]['failed'] == 1:
            pu_country_dict[pu_save[i]['country']]['inactive'] += 1
        else:
            pu_country_dict[pu_save[i]['country']]['active'] += 1
    else:
        if pu_save[i]['failed'] == 1:
            pu_country_dict[pu_save[i]['country']] = {'active': 0,
                                                    'inactive': 1}
        else:
            pu_country_dict[pu_save[i]['country']] = {'active': 1,
                                                    'inactive': 0}



    
    if pu_save[i]['failed'] == 1:
        pu_inactive_count += 1
        pu_inactive_value_total += pu_save[i]['value']
        
    else:
        pu_active_count += 1
        pu_active_value_total += pu_save[i]['value']

    if pu_save[i]['premium'] == 1:
        pu_premium_count += 1
        pu_premium_value_total += pu_save[i]['value']
        
    else:
        pu_nonpremium_count += 1
        pu_nonpremium_value_total += pu_save[i]['value']

    if pu_save[i]['premium'] == 1 and pu_save[i]['failed'] == 1:
        pu_premium_inactive_count += 1
        pu_premium_inactive_value_total += pu_save[i]['value']



    if pu_save[i]['premium'] == 1 and pu_save[i]['failed'] == 0:
        pu_premium_active_count += 1
        pu_premium_active_value_total += pu_save[i]['value']


        
        
        

pu_user_count_total = len(pu_save)

print("Total users randomly sampled: %i" % (pu_user_count_total))
print("")

pu_active_user_percentage = 100*(pu_active_count/(pu_active_count+pu_inactive_count))
        
pu_active_value_percentage = 100*(pu_active_value_total/(pu_active_value_total + pu_inactive_value_total))

pu_premium_user_percentage = 100*(pu_premium_count/(pu_premium_count+pu_nonpremium_count))

pu_premium_value_percentage = 100*(pu_premium_value_total/(pu_premium_value_total + pu_nonpremium_value_total))

pu_average_active_points = pu_active_value_total/pu_active_count

pu_average_inactive_points = pu_inactive_value_total/pu_inactive_count

pu_average_premium_points = pu_premium_value_total/pu_premium_count

pu_average_nonpremium_points = pu_nonpremium_value_total/pu_nonpremium_count

pu_average_points = (pu_active_value_total+pu_inactive_value_total)/(pu_active_count+pu_inactive_count)

pu_premium_inactive_user_percentage = 100*(pu_premium_inactive_count/pu_user_count_total)

pu_average_premium_inactive_points = pu_premium_inactive_value_total/pu_premium_inactive_count

pu_premium_active_user_percentage = 100*(pu_premium_active_count/pu_user_count_total)

pu_average_premium_active_points = pu_premium_active_value_total/pu_premium_active_count

print("Active users represent %s%% of all PucaTrade users" % str(round(pu_active_user_percentage,2)))
print("Active users have %s%% of all PucaPoints not in escrow in their accounts" % str(round(pu_active_value_percentage,2)))
print("")

print("The average user has %s PucaPoints in their account" % str(round(pu_average_points,1)))
print("The average inactive user has %s PucaPoints in their account" % str(round(pu_average_inactive_points,1)))
print("The average active user has %s PucaPoints in their account" % str(round(pu_average_active_points,1)))
print("")

print("Premium users represent %s%% of all PucaTrade users" % str(round(pu_premium_user_percentage,2)))
print("Premium users have %s%% of all PucaPoints not in escrow in their accounts" % str(round(pu_premium_value_percentage,2)))
print("")

print("The average nonpremium user has %s PucaPoints in their account" % str(round(pu_average_nonpremium_points,1)))
print("The average premium user has %s PucaPoints in their account" % str(round(pu_average_premium_points,1)))
print("")

print("Premium inactive users represent %s%% of all PucaTrade users" % str(round(pu_premium_inactive_user_percentage,2)))
print("The average premium inactive user has %s PucaPoints in their account" % str(round(pu_average_premium_inactive_points,1)))

print("")

print("Premium active users represent %s%% of all PucaTrade users" % str(round(pu_premium_active_user_percentage,2)))
print("The average premium active user has %s PucaPoints in their account" % str(round(pu_average_premium_active_points,1)))

print("")

##for i in pu_country_dict:
##    if  pu_country_dict[i]['active'] > 0:
##        print('%s is %i active users and %i inactive users' % (i, pu_country_dict[i]['active'], pu_country_dict[i]['inactive']))
##        pu_country_active_user_percentage = 100 *(float(pu_country_dict[i]['active'])/float( pu_country_dict[i]['active'] +  pu_country_dict[i]['inactive']))
##
##        print('%f %% of its users are active.' % pu_country_active_user_percentage )
##
##        pu_country_as_percent_total_userbase = 100*float(pu_country_dict[i]['active'] + pu_country_dict[i]['inactive'])/(pu_active_count+pu_inactive_count)
##        print('Its users represent %f %% of the total userbase.' % pu_country_as_percent_total_userbase)
##
##        pu_country_as_percent_active_userbase = 100*float(pu_country_dict[i]['active'])/pu_active_count
##        print('Its active users represent %f %% of the active userbase.' % pu_country_as_percent_active_userbase)
##
##        print('')

##print('-----------------------------------------------------------------')
