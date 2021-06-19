def addOperators(num, target):
    """
    :type num: str
    :type target: int
    :rtype: List[str]
    """
    def straightEval(lt):
        item = int(lt[0])
        i = 1
        while i < len(lt):
            op = lt[i]
            i+=1
            num = int(lt[i])
            if op == '+':
                item+=num
            elif op == '-':
                item-=num
            else:
                item*=num
            i+=1
        return item


    def eval(lt):
        if '' in lt:
            lt,isTrailing = evalBlank(lt)
            if isTrailing:
                return 0,True
        if '*' in lt:
            lt = evalStar(lt)
        return straightEval(lt),False

    def evalStar(lt):
        while '*' in lt:
            i = lt.index('*')
            el1 = int(lt[i-1])
            el2 = int(lt[i+1])
            lt[i] = str(el1*el2)
            del lt[i+1]
            del lt[i-1]
        return lt

    def evalBlank(lt):
        while '' in lt:
            i = lt.index('')
            el1 = lt[i-1]
            if el1 == '0':
                return lt,True
            el2 = lt[i+1]
            lt[i] = str(int(el1+el2))
            del lt[i+1]
            del lt[i-1]
        return lt, False




    def recur(i,n,nums,ops,target,lt,results):
        if i == n:
            xt = list(lt)
            val, isTrailing = eval(xt)
            if not isTrailing and val == target:
                    st = ''.join(lt)
                    if st not in results:
                        results.append(st)
        else:
            if i%2 == 0:
                if nums:
                    item = nums[0]
                    lt.append(item)
                    del nums[0]
                    recur(i+1,n,nums,ops,target,lt,results)
                    del lt[-1]
                    nums.insert(0,item)
            else:
                for j in range(len(ops)):
                    item = ops[j]
                    lt.append(item)
                    recur(i+1,n,nums,ops,target,lt,results)
                    del lt[-1]
    lt = []
    results = []
    ops = ['+','-','*','']
    nums = list(num)
    n = len(nums)*2
    n-=1
    recur(0,n,nums,ops,target,lt,results)
    results.sort()
    return results

num='123456789'
target = 45
print(addOperators(num, target))