def censor(text,word):
	return " ".join(w.replace(word,"*" * len(word) for w in text.split())
print censor("test test test","test")

