def find_closest_to_value(target, table):
    #table is the the 2xN table with value we are looking for in the first column.
    #The target is to find value which is closest to the one corresponing to the target (from the second column)
    #For now Second solumn goes from highest to lowest
    closest_value = 0
    
    found = False
    counter = 0
    for i in range(len(table)):
        counter = i
        if target == table[i][1]:
            return table[i][0]
        if target > table[i][1]:
            found = True
            break

    #approximating linearly
    if found == True and counter != 0:
        #d_target_down = target - table[counter][1]
        d_target_up = table[counter-1][1] - target
        difference = table[counter-1][1] - table[counter][1]
        d_value = table[counter][0] - table[counter-1][0]
        #print(d_value)
        d_ratio = d_target_up/(difference)
        #print(d_ratio)
        closest_value = table[counter-1][0] + d_value * d_ratio
    elif counter == 0:
        difference = table[0][1] - table[1][1]
        d_value = table[1][0] - table[0][0]
        slope = d_value / difference
        closest_value = table[0][0] - slope * (target-table[0][1])
    elif found == False:
        difference = table[-1][1] - table[-2][1]
        d_value = table[-2][0] - table[-1][0]
        slope = d_value / difference
        closest_value = table[-1][0] - slope * (target-table[-1][1])

    return closest_value