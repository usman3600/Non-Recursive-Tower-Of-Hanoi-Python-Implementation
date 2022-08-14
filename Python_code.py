conditions = {
    1:{"numbers":0, "disks":[]},
    2:{"numbers":0, "disks":[]},
    3:{"numbers":0, "disks":[]},
    "visited":[-1]
}
last_peg = 2
def non_recur_tower_of_hanoi(disks, A, B, C):
    number_of_moves = (2**disks)-1
    conditions[1]["numbers"] = disks
    conditions[1]["disks"] = [_ for _ in range(1, disks+1)]
    for _ in range(number_of_moves):
        disks, peg = find_disk(conditions)
        if disks % 2 == 0:
            if peg == 1 and check_pegs_disk(2, disks):
                show_movement(disks, A, B)
                change_condition_number(1, 2)
                change_condition_disks(1, 2, disks)
                
            elif peg == 2 and check_pegs_disk(3, disks):
                show_movement(disks, B, C)
                change_condition_number(2, 3)
                change_condition_disks(2, 3, disks)

            else:
                show_movement(disks, C, A)
                change_condition_number(3, 1)
                change_condition_disks(3, 1, disks)

        else:
            if peg == 1 and check_pegs_disk(3, disks):
                show_movement(disks, A, C)
                change_condition_number(1, 3)
                change_condition_disks(1, 3, disks)
                
            elif peg == 3 and check_pegs_disk(2, disks):
                show_movement(disks, C, B)
                change_condition_number(3, 2)
                change_condition_disks(3, 2, disks)
                
            else:
                show_movement(disks, B, A)
                change_condition_number(2, 1)
                change_condition_disks(2, 1, disks)

def find_disk(Condions):
    pegs = {1, 2, 3}
    for peg in range(1, 4):
        avail_pegs = list(pegs-{peg})
        #print(conditions)
        if conditions[peg]["numbers"]:
            disks = conditions[peg]["disks"][0]
            if check_pegs_disk(avail_pegs[0], disks) and disks != conditions["visited"][-1]:
                conditions["visited"][0] = disks
                return disks, peg
            elif check_pegs_disk(avail_pegs[1], disks) and disks != conditions["visited"][-1]:
                conditions["visited"][0] = disks
                return disks, peg
        
        
def check_pegs_disk(peg_name, disks):
        if  conditions[peg_name]["disks"] == []:
            return True
        else:
            if disks < conditions[peg_name]["disks"][0]:
                return True
            else:
                return False
    
def show_movement(disks, A, B):
    print(f"Move {disks} from peg {A} to peg {B}")

def change_condition_number(from_peg, to_peg):
    conditions[from_peg]["numbers"] -=1
    conditions[to_peg]["numbers"] +=1

def change_condition_disks(from_peg, to_peg, change):
    conditions[from_peg]["disks"].remove(change)
    conditions[to_peg]["disks"].insert(0, change)


non_recur_tower_of_hanoi(15, "A", "B", "C")
