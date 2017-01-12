
# coding: utf-8
# In[236]:

class Transformer:
    
    dict = {'Obama': 'entity', 'Facebook': 'entity', 'http://bit.ly/xyz': 'link', '@elversatile': 'username'}

    def __init__(self, options):
        self.__tweets = ''
        self.__processor = self.__buildProcessor()

    def __buildProcessor(self):
        return {
          'entity': self.__wrapEntity,
          'link': self.__wrapLink,
          'username': self.__wrapUsername
          # ...
        }

    def __getProcessor(self, wordType): 
        proc = self.__processor.get(wordType, False)
        if proc == False:
          return self.__wrapCommonWord
        else:
          return proc
    
    def extendProcessorMethod(self, mixin):
        self.__processor[mixin.wordType] = mixin.method

    def parseTweets(self, tweets):
        self.__tweets = tweets
        words = self.__tweets.split()
        outStr = ''
        for word in words:
            cTemp = self.dict.get(word, False)
            # print cTemp, word
            outStr += self.__getProcessor(cTemp)(word)
        return outStr

    def __wrapEntity(self, word):
        newWord = "<strong>" + word + "</strong>"
        return newWord
        
    def __wrapLink(self, word):
        newWord = r'<a href="' + word  + r'">' + word + r'</a>'
        return newWord
        
    def __wrapUsername(self, word):
        newWord = r'@<a href=' + '\"http://twitter.com/' + word +'\">' + word + r'</a>'
        return newWord
    
    def __wrapCommonWord(self, word):
        newWord = word
        return newWord
# In[237]:

example = Transformer({
  'configuration1': 'someConfig',
  'configuration2': 'someConfig'
#  ...
})

## Extend Transformer with hashTag method
#example.extendProcessorMethod({
#  'wordType': 'hashTag',
#  'method': someFunc
#  })
outSt = example.parseTweets("Obama visited Facebook headquarters: http://bit.ly/xyz @elversatile")

print outStr
