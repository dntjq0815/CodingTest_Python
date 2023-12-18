def solution(rank, attendance):
    attnd_available_list = []
    for i in range(1, len(rank)+1):
        rank_idx = rank.index(i)

        if attendance[rank_idx] == False:
            continue
            
        elif attendance[rank_idx] == True:
            attnd_available_list.append(rank_idx)
            if len(attnd_available_list) == 3:
                break
                
    return 10000*attnd_available_list[0] + 100*attnd_available_list[1] + attnd_available_list[2]