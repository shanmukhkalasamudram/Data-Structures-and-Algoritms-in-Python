b = int(input())


def avg(days):
    a = []
    for i in range(days):
        a.append(int(input()))

    avg = round(sum(a)/len(a),2)
    print(avg)
    count = 0
    for i in range(len(a)):
        if(avg < a[i]):
            count += 1
    return (avg,count)

print(avg(b))


def count_word_frequency(words):
    di = {}
    for i in range(len(words)):
        if(words[i] in di):
            di[words[i]] += 1
        else:
            di[words[i]] = 1
    print(di)
    return di

count_word_frequency(['apple', 'orange', 'banana', 'apple', 'orange', 'apple'])

def max_value_key(my_dict):
    max = 0
    key = {}
    for i in my_dict:
        if(my_dict[i] > max):
            max = my_dict[i]
            key = {i: my_dict[i]}
    print(list(key.keys())[0])
    return list(key.keys())[0]

my_dict = {'a': 5, 'b': 9, 'c': 2}
max_value_key(my_dict)