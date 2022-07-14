from itertools import combinations

def transform_string(s, marks):
    if not marks:
        return s    
    marks = set(marks)
    string_builder = []
    for i, c in enumerate(s):
        if i in marks:
            string_builder.append('{0}{0}'.format(c))
        else:
            string_builder.append(c)
    return ''.join(string_builder)

def solution(string):
    length_s = len(string)
    range_s = range(len(string))
    out_string = None
    #c = 0
    #answers = set()
    for i in range(length_s):
        comb = combinations(range_s, i)
        for markers in comb:
            candidate = transform_string(string, markers)
            #c += 1
            #answers.add(candidate)
            if out_string is None:
                out_string = candidate
            else:
                if candidate < out_string:
                    out_string = candidate
    return out_string


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        input_string = input()
        output_string = solution(input_string)
        print("Case #{}: {}".format(i+1, output_string))



