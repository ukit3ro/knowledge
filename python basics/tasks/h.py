#Дан список intervals, где каждый элемент кодирует интервал intervals[i] = [start, end]. 
# Выполните слияние всех интервалов, вернув 
# список непересекающихся интервалов, которые покрывают интервалы из intervals.

def merge(intervals):
    intervals.sort()
    
    m_begin, m_end = intervals[0]
    ans = []
    
    for begin, end in intervals:
        if begin < m_end:
            m_end = max(m_end, end)
        else:
            ans.append([m_begin, m_end])
            m_begin, m_end = begin, end
            
    ans.append([m_begin, m_end])
    
    return ans

print(merge([[1,3], [2,6], [8,10], [15,18]] ))
