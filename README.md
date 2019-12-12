# Database Final Project_server
This a the server end of the final database project

###### Re:

*I can not understand what you mean below. Could you please add a few comments?*

*Besides, the GET method needs parameters to tell the server what you want.* 

*For example,*

*get(username="Lee")*

# API Command
## Page 1
### Front Page

##### Get

```
userInfo{
	username
    useremail
    userplan{
    	wordlistName
      	already recite
      	remained
      	today's learn
      	today's review
      	continuous //  连续多少天
    }
}
```



#####   Post

```
None 
```



### Test Page

#####   Get

```
todayTestWordList{
	userID
  	testID
  	listSize
  	wordListName
  	[
    	wid
		vid
    	English
    	Chinese
		familiarDegree 	 	// 0(almost new) 1(just known) 2(familiar) 3(keep firmly in mind)
		options[A,B,C,D]	//list 
		correctOption
		*partOfSpeech
		*pronounciation	
        //...
	]
}
```

#####   Post

```
getTestList{
	userID
}

todayTestResult{
	userID
	testID
	listSize
	[
		wordId
		vocabId
		familiarDegree
	]
	activeTime
}
```



### Finish Page

```
Get 

None

Post 

AGAIN // 是否来多一组
```

## Page 2

### Information

##### Get

```
SevenDayData{
	[
		just known word count
		familiar word count 
		keep firmly in mind word count
	]*7
}

mastered word(keep firmly in mind or familiar word) total
learned word(all word except new word) total

.............// 还有啥你们想想
```
##### Post

```
getRecentInfo{
	userID
}
```

## Page3

### record

##### Get

```
todayRecordWordList{} // same in page1 todayTestWordList
totalRecordWordList{} // no options, all the words learned(familiar degree <> 0) will be on the list
```

##### Post	

```
changeWordFamiliarDegree{
	userId
	wordId
	familiarDegree
}
```


​	


## Page4

### user Info Full

##### Get

```
userID
username
userphone
sex
scholar
wordListName // 当前正在背的单词书
mastered word total 
learned word total
```

### Change Book List

##### Post

```
ChangeBookList{
	wordListName
	wordListId
} // 然后更新个人信息
```

### Feedback Page

##### Post


```
FeedBackInfo{
	feedbackId
	feedbackInfo
	UserId
}
```
