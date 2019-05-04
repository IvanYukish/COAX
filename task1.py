s = 'string'
# method 1
print(''.join(list(reversed(s))))

# method 2
print(s[::-1])


# method 3
def reverse(word):
    string = ""
    for i in word:
        string = i + string
    return string


print(reverse(s))
