def find_str(self,s, char):
        index = 0

        if char in s:
            c = char[0]
            for ch in s:
                if ch == c:
                    if s[index:index+len(char)] == char:
                        return index

                index += 1

        return -1
