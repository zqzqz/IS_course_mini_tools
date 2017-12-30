from math import *

def p2b(p,n):
    assert(p>=0 and p<=1)
    result = ''
    for i in range(n):
        if p*2//1:
            result+='1'
        else:
            result+='0'
        p = p*2 - (p*2//1)
    return result

def shanon(x):
    leng = len(x)
    x.sort(reverse=True)
    sum_p = 0
    result = []
    for i in range(leng):
        n = (-log(x[i],2))
        if (-log(x[i],2))%1==0:
            n = int(-log(x[i],2))
        else:
            n = int(-log(x[i],2))+1
        result.append(p2b(sum_p, n))
        sum_p += x[i]
    return result
#print(2.0-2)

class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type word_list: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        word_list = words + [""]
        line_len = 0
        start, end = 0,-1
        result = []
        index=0
        while index < len(word_list):
            if line_len == 0:
                line_len += len(word_list[index])
            else:
                line_len += (len(word_list[index])+1)
            if line_len > maxWidth:
                line_len -= (len(word_list[index])+1)
                space = maxWidth-line_len
                if end>start:
                    each_space = [space//(end-start)+1 for j in range(space%(end-start))] + [space//(end-start) for k in range((end-start)-space%(end-start))]
                result_str = ""
                for i in range(start, end):
                    result_str += (word_list[i]+' '+' '*each_space[i-start])
                result_str += word_list[end]
                result_str += ' '*(maxWidth-len(result_str))
                result.append(result_str)
                line_len = 0
                start = end+1
                end = start-1
            elif word_list[index]=="" and line_len>0:
                result_str = ''
                for i in range(start, end):
                    result_str += (word_list[i]+' ')
                result_str += word_list[end]
                result_str += ' '*(maxWidth-len(result_str))
                result.append(result_str)
                break
            else:
                end += 1
                index += 1
        if len(result)==0:
            result.append(" "*maxWidth)
        return result

test = Solution()
print(test.fullJustify(['a'], 1))
print(test.fullJustify(["Fourscore","and","seven","years","ago","our","fathers","brought","forth","on","this","continent","a","new","nation,","conceived","in","liberty","and","dedicated","to","the","proposition","that","all","men","are","created","equal.","Now","we","are","engaged","in","a","great","civil","war,","testing","whether","that","nation","or","any","nation","so","conceived","and","so","dedicated","can","long","endure.","We","are","met","on","a","great","battlefield","of","that","war.","We","have","come","to","dedicate","a","portion","of","that","field","as","a","final","resting-place","for","those","who","here","gave","their","lives","that","that","nation","might","live.","It","is","altogether","fitting","and","proper","that","we","should","do","this.","But","in","a","larger","sense,","we","cannot","dedicate,","we","cannot","consecrate,","we","cannot","hallow","this","ground.","The","brave","men,","living","and","dead","who","struggled","here","have","consecrated","it","far","above","our","poor","power","to","add","or","detract.","The","world","will","little","note","nor","long","remember","what","we","say","here,","but","it","can","never","forget","what","they","did","here.","It","is","for","us","the","living","rather","to","be","dedicated","here","to","the","unfinished","work","which","they","who","fought","here","have","thus","far","so","nobly","advanced.","It","is","rather","for","us","to","be","here","dedicated","to","the","great","task","remaining","before","us--that","from","these","honored","dead","we","take","increased","devotion","to","that","cause","for","which","they","gave","the","last","full","measure","of","devotion--that","we","here","highly","resolve","that","these","dead","shall","not","have","died","in","vain,","that","this","nation","under","God","shall","have","a","new","birth","of","freedom,","and","that","government","of","the","people,","by","the","people,","for","the","people","shall","not","perish","from","the","earth."],80))
