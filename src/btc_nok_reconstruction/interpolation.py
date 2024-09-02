def interpolate_zero_values(data):
    zero_indices = [i for i, (_, price, _) in enumerate(data) if price == 0]
    
    if zero_indices:
        start_idx = zero_indices[0]
        end_idx = zero_indices[-1]
        
        if start_idx > 0 and end_idx < len(data) - 1:
            start_value = data[start_idx - 1][1]
            end_value = data[end_idx + 1][1]
            
            # Linear interpolation
            step = (end_value - start_value) / (len(zero_indices) + 1)
            
            for i, idx in enumerate(zero_indices):
                interpolated_value = start_value + step * (i + 1)
                data[idx] = (data[idx][0], interpolated_value, 'Interpolated')
    
    return data