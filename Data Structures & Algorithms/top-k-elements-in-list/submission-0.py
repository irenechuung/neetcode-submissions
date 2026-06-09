class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
            hashmap = dictionary 
            go through array:
                map every num to frequency 
            
            swap num and frequency so its dict[freq]=num
            sort hashmap by key
            get output array 
            go backwards from last key k number of times(append the number)
        
        '''
        numToFreq = dict()
        for n in nums:
            numToFreq[n] = numToFreq.get(n, 0) + 1
        
        freqToNum = dict()
        for num, freq in numToFreq.items():
            freqToNum[freq] = freqToNum.get(freq, []) + [num]
        
        s = dict(sorted(freqToNum.items()))
        sorted_keys = list(s.keys())
        
        output = []
        for i in range(1, k+1):
            output.extend(s[sorted_keys[-i]])
        return output

        