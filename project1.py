import json
import operator
data = []
noofTweet = 0
noTweets = 0
hashCount = 0
nonhash = 0
twehash = {}
split = []
tif = []
sent = {}

tweethascount = 0
dist1 = {}
avg={}
sortAvg={}
with open('outputfinal.json') as f:
    tif = open("AFINN-111.txt", "r")
    for line in f:
        data.append(json.loads(line))
for line in tif:
  term, score  = line.split("\t") 
  sent[term] = int(score)  
#print len(data)
for i in data:
    sentimentCount = 0 
    if "text" in i.keys():
        tweet = i['text']
        noofTweet = noofTweet + 1
        split = tweet.split(" ")
        for values in split:
            if values in sent:
                sentimentCount += sent[values]
    else:
        noTweets = noTweets + 1

    if "entities" in i.keys():
        hashtags = i["entities"]["hashtags"]       
        for ht in hashtags:                        
            if ht != None:
                hashCount = hashCount + 1                                
                if ht["text"].encode("utf-8") in twehash.keys():
                    twehash[ht["text"].encode("utf-8")] += 1
                    tweethascount += 1
                    dist1[ht["text"].encode("utf-8")].append(sentimentCount) 
                else:
                    twehash[ht["text"].encode("utf-8")] = 1
                    dist1[ht["text"].encode("utf-8")] = [sentimentCount] 
for ke,val in dist1.iteritems():
   avg[ke]=float(sum(val))/float(len(val))
sortedavg = sorted(avg.items(),key=operator.itemgetter(1), reverse=False)[:10]
sortedsortAvg = sorted(avg.items(),key=operator.itemgetter(1), reverse=True)[:10]
sortedHashTags = dict(sorted(twehash.items(), key=operator.itemgetter(1), reverse=True)[:10])   
print("\n")                                                                                                 
for key,value in sorted(sortedHashTags.items(), key=lambda kv: (kv[1],kv[0]),reverse=True):         
  print("#%s -  %d  -  %f" % (key.decode("utf-8"), value, avg[key]))
max= float('-inf') 
min= float('inf')                                             
for ke,val in sortedHashTags.iteritems():
  val=avg[ke]
  if val>max:
    max=val
    maxkey=ke
  if val<min:
    min=val
    minkey=ke
   
print "Total Objects in the file: ",len(data)
print "Total Tweets in file: ",noofTweet
print "Total Hashtags with Tweets in file: ",tweethascount
print "Most Positive from the 10 popular tags: ",maxkey,":",avg[maxkey]
print "Most Negative from the 10 popular tags: ",minkey,":",avg[minkey],"\n"


		