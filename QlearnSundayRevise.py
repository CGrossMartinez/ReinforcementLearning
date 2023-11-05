import numpy as np

def states (coordinates):

    if coordinates[0] == 0 and coordinates[1] == 0:
        state = "s0"
    elif coordinates[0] == 0 and coordinates[1] == 1:
        state = "s1"
    elif coordinates[0] == 1 and coordinates[1] == 0:
        state = "s2"
    else:
        state = "s3"

    return state

def possible_actions(current_state):

    #actions: up 1, down = 2, left = 3, right = 4
    if current_state == "s0":
        actions = (2, 4)
    elif current_state == "s1":
        actions = (2, 3)
    elif current_state == "s2":
        actions = (1, 4)
    else:
        current_state = (1, 3)
    
    return actions


def calc_next_state(act, cur_loc):

    temp = np.zeros(2)

    print(type(temp))
    print(temp.size)
    print(temp)

    #actions: up 1, down = 2, left = 3, right = 4
    if act == 1:
        if cur_loc[0] > 0:
            temp[1] = cur_loc[1]
            temp[0] = cur_loc[0] - 1

    elif act == 2:
        if cur_loc[0] < 1:

            temp[1] = cur_loc[1]
            temp[0] = cur_loc[0] + 1
            
    '''
    elif act == 3:
        if temp[1] > 0:
            temp[1] -= 1
    else:
        if temp[1] < 1:
            temp[1] += 1
    
    cur_loc = temp1
    '''
    return temp






        
def select_action(cur_cdnt, curr_st, poss_act, qSA, rewards):

    if np.random.uniform(0, 1) <= 0.3:
        return np.random.choice(poss_act)
    else:
        for actions in poss_act:

            print(cur_cdnt)

            next_state_coordinate = calc_next_state(actions, cur_cdnt)

            print(cur_cdnt)

        




start_coordinate = np.array([0,0])
goal_coordinate = np.array([1,1])

maze = np.zeros([2, 2])

rewards = (("s0", 0, 0, 0, 0),
           ("s1", 0, 1, 0, 0),
           ("s2", 0, 0, 0, 1),
           ("s3", 0, 0, 0, 0),
          )


qSA = [["s0", 0, 0, 0, 0],
       ["s1", 0, 0, 0, 0],
       ["s2", 0, 0, 0, 0],
       ["s3", 0, 0, 0, 0],
      ]

#print(type(start_coordinate))
#print(qSA[3][0])
#print(rewards)



current_coordinates = start_coordinate

#print(type(current_coordinates))

curr_st = states(current_coordinates)
poss_act = possible_actions(curr_st)
action = select_action(current_coordinates, curr_st, poss_act, qSA, rewards)

