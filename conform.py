"Junior Dev: YİĞİT"
def pleaseConform(caps):
    if len(caps) == 0:
        return

    f_intervals = []
    b_intervals = []
    
    i = 0
    n = len(caps)
    
    while i < n:
        current_cap = caps[i]
        
        if current_cap == 'F':
            start = i
            while i < n and caps[i] == 'F':
                i += 1
            f_intervals.append((start, i - 1))
            
        elif current_cap == 'B':
            start = i
            while i < n and caps[i] == 'B':
                i += 1
            b_intervals.append((start, i - 1))
            
        else:
            i += 1
            
    if len(f_intervals) < len(b_intervals):
        best_intervals = f_intervals
    else:
        best_intervals = b_intervals
        
    if len(best_intervals) == 0:
        return
        
    for interval in best_intervals:
        start_idx = interval[0]
        end_idx = interval[1]
        
        if start_idx == end_idx:
            print(f"Person in position {start_idx + 1} flip your cap!")
        else:
            print(f"People in positions {start_idx + 1} through {end_idx + 1} flip your caps!")

cap3 = ['B', 'B', 'B', 'H', 'B', 'F', 'B', 'B', 'B', 'F', 'H', 'F', 'F']
pleaseConform(cap3)