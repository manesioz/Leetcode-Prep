from collections import defaultdict 
def possible_encoding(original, encrypted): 
    char_map = defaultdict(list)
    if len(original) == len(encrypted): 
        for curr, new in zip(original, encrypted): 
            if char_map[curr]: 
                if new in char_map[curr]: 
                    continue 
                elif new not in char_map[curr]: 
                    return False 
            else: 
                char_map[curr] = new 
        return True 
    else: 
        return False
