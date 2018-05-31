class Solution:
    def countOfAtoms(self, formula):
        res = ''
        c = self.f(formula)
        for element in sorted(c.keys()):
            res += element + (str(c[element]) if c[element] > 1 else '')
        return res

    def f(self, formula: str):
        from collections import Counter
        if not formula:
            return Counter()
        i = formula.find('(')
        if i >= 0:
            j, cnt = i + 1, 1
            while cnt > 0:
                cnt += {'(': 1, ')': -1}.get(formula[j], 0)
                j += 1
            k = j + 1
            while k < len(formula) and formula[k].isdigit():
                k += 1
            time = formula[j:k]
            time = int(time) if time else 1
            tmp = self.f(formula[i + 1:j - 1])
            for e in tmp:
                tmp[e] *= time
            return self.f(formula[:i]) + tmp + self.f(formula[k:])
        else:
            res = Counter()
            element = ''
            index = 0
            while index < len(formula):
                if element and (formula[index].isdigit() or formula[index].isupper()):
                    if formula[index].isupper():
                        res[element] += 1
                        element = formula[index]
                    else:
                        k = index
                        while index < len(formula) and formula[index].isdigit():
                            index += 1
                        time = int(formula[k:index])
                        res[element] += time
                        element = formula[index] if index < len(formula) else ''
                else:
                    element += formula[index]
                index += 1
            if element:
                res[element] += 1
            return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.countOfAtoms(
        "(((U42Se42Fe10Mc31Rh49Pu49Sb49)49V39Tm50Zr44Og6)33((W2Ga48Tm14Eu46Mt12)23(RuRnMn11)7(Yb15Lu34Ra19CuTb2)47(Md38BhCu48Db15Hf12Ir40)7CdNi21(Db40Zr24Tc27SrBk46Es41DsI37Np9Lu16)46(Zn49Ho19RhClF9Tb30SiCuYb16)15)37(Cr48(Ni31)25(La8Ti17Rn6Ce35)36(Sg42Ts32Ca)37Tl6Nb47Rh32NdGa18Cm10Pt49(Ar37RuSb30Cm32Rf28B39Re7F36In19Zn50)46)38(Rh19Md23No22PoTl35Pd35Hg)41)50"))
