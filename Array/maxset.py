def maxset( A):
        fin_max = 0
        fin_out = []
        seg_max =0
        seg_out = []
        for i in A:
            if i >= 0:
                seg_max += i
                seg_out.append(i)
            else:
                if seg_max >= fin_max:
                    fin_max = seg_max
                    fin_out = seg_out
                seg_max = 0
                seg_out =[]
        if seg_max > fin_max:
            fin_max = seg_max
            fin_out = seg_out
        return fin_out

A = [ 0, 0, -1, 0 ]
print(maxset(A))