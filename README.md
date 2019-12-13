# Database Final Project_server
This a the server end of the final database project

###### NOTE: You should not trust theses APIs yet.

# API Command

## Login page

### Sign up

##### Post

```
{
	"username":""
	"phonenumber":""
	"mail":""
	"password":""
}

return {
	"errorcode":int	//([0:success,1:phone number error,2:mail error]
	"UID": ""
}
```

### Sign in

##### Post

```
{
	"type":int //([0:UID,1:phone number,2:mail])
	"info":""
	"password":""
}

return {
	"errorcode":int //[0:success,1:fail]
	"username":""
	"phonenumber":""
	"mail":""
	"UID": ""
}
```



## Page 1

### Front Page

##### Get("./user/UID/overview")

```
return {
    "wordlistName":""		//用户选择的单词本
    "alreadyRecite":int		//总共背（浏览过）的单词数
    "remained":int			//剩余单词数
    "today's learn":int		//今天要学的单词数
    "today's review":int	//今天需要复习的单词数
    "continuous":int		//连续多少天背单词
}
```



#####   Post

```
None 
```



### Test Page

#####   Get("./plan/UID/\<int\>")

```
return{
	"todayLearn":[
		("TID",
		"WID",
		"熟练度",
		"options"//[A,B,C,D]
		)
	]
	"todayReview"[
		("TID",
		"WID",
		"熟练度",
		"options"//[A,B,C,D]
		)
	]
}
```

##### GET("./word/WID")

```
return{
	"word":""
	"Chinese":""
	"音标":""
	"词性":""
}
```



#####   Post

```
{
	"result":[
		("WID":""
		"熟练度":int//(0,1,2,3)
		//"":"")
	]
	"start":"2019-12-01-10-30-12"
	"end":"2019-12-01-10-40-02"
}

return bool
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

##### Get(./info/UID)

```
return{
	"info":[
		(1,	
		2,
		3,
		active time,//int 
		)
	]
	"active":[
		active degree:int
	]//(24,1)
}
```
##### Post

## Page 3

### record

##### Get("./plan/UID")

```
return{
	"plan":[
		("WID",
		"English",
		"Chinese",
		"熟练度")
	]
}
```

##### Post	

```
{
	"newplan":[
		("WID",
		"熟练度")
	]
}
```


​	


## Page4

### user Info Full

##### Get("./user/UID/info")

```
return{
	"avatar":"base64"//default='0'
	"sex":""
	"scholar":""
	"grade":""
}
```

##### Post

```
{
	"username":""
	"avatar":"base64"//default='0'
	"sex":""
	"scholar":""
	"grade":""
}
```



### Change Book List

##### Post

```
{
	"wordListName"
	"wordListId"
} // 然后更新个人信息
```

### Feedback Page

##### Post


```
{
	"feedbackInfo":""
	"UId":""
}
```
