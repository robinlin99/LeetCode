class Solution:
    def fullJustify(self, words, maxWidth):
        length = len(words)
        output = []
        pointer = 0
        inner = 0
        while pointer < length and inner < length:
            sentencelength = len(words[pointer])
            count = 1
            inner = pointer + 1
            while inner < length:
                if sentencelength + len(words[inner]) > maxWidth - count:
                    break
                else:
                    count += 1   
                    sentencelength += len(words[inner])
                inner += 1

            accum = ""
            candidates = words[pointer:inner]
            spaces = maxWidth - sentencelength
            space_list = gen_space(spaces,count)
            if pointer == length - 1 or inner == length:
                for j,i in enumerate(candidates):
                    accum += i
                    if j != len(candidates)-1:
                        accum += " "
                accum += " "*(maxWidth - len(accum))
            else:
                wordindex = 0
                spaceindex = 0
                while wordindex < len(candidates) or spaceindex < len(space_list):
                    if wordindex < len(candidates):
                        accum += candidates[wordindex]
                        wordindex += 1
                    if spaceindex < len(space_list):
                        accum += space_list[spaceindex]*" "
                        spaceindex += 1
            output.append(accum)
            pointer = inner
        return output
    
def gen_space(spaces,words):
    if words == 1:
        return [spaces]
    base = spaces // (words-1)
    space_list = [base] * (words-1)
    remainder = spaces % (words-1)
    counter = 0
    index = 0
    while counter < remainder:
        if index == len(space_list) - 1:
            index = 0  
        space_list[index] += 1
        counter += 1
        index += 1
    return space_list
        