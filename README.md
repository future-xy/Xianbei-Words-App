# DatabaseProject_server
This a the server end of the final database project

# API Command
## Page1
### FrontPage

  Get
  
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
  
  
  Post
  
  None 

### TestPage

  Get
  
  todayTestWordList{
  userID
  testID
  listSize
  wordListName
  [
    wordId
	vocabId
    english
    chinese
	familiarDegree // 0(almost new) 1(just known) 2(familiar) 3(keep firmly in mind)
	options[A: ... B:... C:... D:...] 
	correctOption
	*partOfSpeech
	*pronounciation
	·············//  based on our dataset]
  }
  
  Post
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

### FinishPage

	Get 
	
	None
	
	Post 
	
	AGAIN // 是否来多一组
  
## Page2

### Information

	Get
	
	SevenDayData{
		[just known word count
		familiar word count 
		keep firmly in mind word count
		]*7
	}
	mastered word(keep firmly in mind or familiar word) total
	learned word(all word except new word) total
	
	.............// 还有啥你们想想

	Post
	
	getRecentInfo{
		userID
	}
## Page3

### record
	
	Get
	
	todayRecordWordList{} // same in page1 todayTestWordList
	totalRecordWordList{} // no options, all the words learned(familiar degree <> 0) will be on the list
	
	
	Post
	
	changeWordFamiliarDegree{
		userId
		wordId
		familiarDegree
	}
	
	

	
## Page4


### userInfoFull

	Get
	
	userID
	username
	userphone
	sex
	scholar
	wordListName // 当前正在背的单词书
	mastered word total 
	learned word total
	
### ChangeBookList

	Post
	
	ChangeBookList{
		wordListName
		wordListId
	} // 然后更新个人信息
	
### feedbackPage


	Post
	FeedBackInfo{
		feedbackId
		feedbackInfo
		UserId
	}
