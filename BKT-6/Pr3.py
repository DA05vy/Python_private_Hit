def decode_string(coded_str):
    stack = [] 
    cur_str = ""
    cur_num = 0 
    
    for char in coded_str:
        if char.isdigit():
            cur_num = int(char)
        
        elif char == '[':
            stack.append((cur_str, cur_num))
            cur_str = "" 
            cur_num = 0
        elif char == ']':
            prev_str, rep_count = stack.pop()
            cur_str = prev_str + cur_str * rep_count
        
        else:
            cur_str += char
    
    return cur_str


coded_str1 = "2[abc]3[cd]ef"
coded_str2 = "abc3[cd]xyz"

print(decode_string(coded_str1)) 
print(decode_string(coded_str2)) 
    
        