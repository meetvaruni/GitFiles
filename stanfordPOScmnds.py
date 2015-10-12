from nltk.tag import StanfordPOSTagger
st = StanfordPOSTagger("models\\english-bidirectional-distsim.tagger",path_to_jar="stanford-postagger.jar")
print(st.tag([u'paid', u'double', u'what', u'i', u'found', u'at', u'another', u'site', u'outside', u'of', u'amazon', u'/', u'this', u'store', u'-', u'never', u'again', u'!']))
print(st.tag("paid double what i found at another site outside of amazon/this store - NEVER AGAIN!".split()))