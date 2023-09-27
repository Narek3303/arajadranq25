# ex 1

# input = ["aba", "aa", "z", "advc", 'asdf','dsadgd', "vcd", "aba"]
# d = None
# for i in input:
#     if d is None:
#         d = list(i)
#     elif len(i) > len(d[0]):
#         d.clear()
#         d.append(i)
#     elif len(i) == len(d[0]):
#         d.append(i)
# print(d)


# ex 2

# c = [-10, 0, -2, 0]
# k = 0
# for i in range(1, len(c)):
#     if c[i] <= c[i - 1]:
#         d = c[i]
#         c[i] = c[i - 1] + 1
#         k += c[i] - d
# print(k, 'qaylov')


# ex 3

# def function(a, b):
#     return (a ** b) % 10
#
# print(function(122546456797845546458787878, 100))


'''
# print(ord('A'))   65
# print(ord('Z'))   90
# print(ord('a'))   97
# print(ord('z'))   122

'''
# ex Kesar

# def kesar(text: str, qayl = 3,  replace = True):
#     t = ''
#     if replace:
#        for i in text:
#           if 65 <= ord(i) <= 90:
#              d = ord(i) - ord('A')
#              i = (d + qayl) % 26
#              t += chr(i + ord('A'))
#           elif 97 <= ord(i) <= 122:
#               c = ord(i)  - ord('a')
#               i = (c + qayl) % 26
#               t += chr(i + ord('a'))
#           else:
#               t += i
#        return f'\033[32m{t}'
#     return f'\033[31m{text}'
#
# print(kesar('python', replace = False))