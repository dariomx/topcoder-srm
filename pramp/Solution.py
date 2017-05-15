def reverseWords(arr):
    def revStr(str, start, end):
        print("before " + "".join(str[start:start+end+1]))
        n = end - start + 1
        for i in xrange(start, start + n/2+1):
            str[i], str[n-i-1] = str[n-i-1], str[i]
            #
        print("after " + "".join(str[start:start+end+1]))
    n = len(arr)
    revStr(arr, 0, n-1)
    start = 0
    end = 0
    while end < n:
        if arr[end] == ' ':
            revStr(arr, start, end-1)
            start = end + 1
            end = start
        else:
            end += 1
    if end - start > 0:
        revStr(arr, start, end-1)
        print("".join(arr))
        pass # your code goes here

reverseWords(list("mama papa son"))

# "mama papa son" => "son papa mama"

