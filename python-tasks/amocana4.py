def counter(n, dic):
    if n in dic:
        return dic[n]
    else:
        ans = counter(n-1, dic) + counter(n-2, dic)
        dic[n] = ans
        return ans
dic = {1:1, 2:2}

print(counter(3,dic))