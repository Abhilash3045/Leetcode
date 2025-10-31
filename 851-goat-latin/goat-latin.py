class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        b = []
        c = 1
        vowels = 'AEIOUaeiou'
        sentence = list(sentence.split())
        for i in sentence:
            if i[0] not in vowels:
                b += [ i[1:] + i[0] + 'ma' + 'a'*c]
            else:
                b += [ i + 'ma' + 'a'*c]
            c += 1
        return " ".join(b)