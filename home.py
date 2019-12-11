#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Name    : home.py
# Time    : 2019/12/11 9:34
# Author  : Fu Yao
# Mail    : fy38607203@163.com

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return """
<!doctype html>
<html class="expanded">
<head>

<!--STATUS OK-->
<meta http-equiv=Content-Type content="text/html;charset=utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1">
<link rel="icon" href="//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/common/img/favicon.ico" mce_href="../static/img/favicon.ico" type="image/x-icon">

<title>百度新闻——海量中文资讯平台</title>
<meta name="description" content="百度新闻是包含海量资讯的新闻服务平台，真实反映每时每刻的新闻热点。您可以搜索新闻事件、热点话题、人物动态、产品资讯等，快速了解它们的最新进展。" >
<script type="text/javascript">
		document.write("<script  type='text/javascript' src='//news-bos.cdn.bcebos.com/mvideo/pcconf_2019.js?"+new Date().getTime()+"'><\/script>");
	</script>
<script type="text/javascript"> window.NEWSLOGURL = 'https://log.news.baidu.com/v.gif'; window.HUNTERLOGURL = '//log.news.baidu.com/u.gif'; window._hmt = window._hmt || [];</script>
<script type="text/javascript" src="//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/common/resource/js/usermonitor_88a158c.js?v=1.2"></script>

<script src="//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/news/js/jquery-1.8.3.min_a6ffa58.js" type="text/javascript"></script>



<link rel="stylesheet" type="text/css" href="//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/common/module_static_include/module_static_include_6cb6a04.css"/><link rel="stylesheet" type="text/css" href="//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/news/focustop/focustop_830e2e5.css"/></head>
<body>
<div id="header-wrapper" class="clearfix">
<div id="usrbar" alog-group="userbar" alog-alias="hunter-userbar-start"></div>
<ul id="header-link-wrapper" class="clearfix">
<li><a href="https://www.baidu.com/" data-path="s?wd=">网页</a></li>
<li style="margin-left:21px;"><span>新闻</span></li>
<li><a href="http://tieba.baidu.com/" data-path="f?kw=">贴吧</a></li>
<li><a href="https://zhidao.baidu.com/" data-path="search?ct=17&pn=0&tn=ikaslist&rn=10&lm=0&word=">知道</a></li>
<li><a href="http://music.baidu.com/" data-path="search?fr=news&ie=utf-8&key=">音乐</a></li>
<li><a href="http://image.baidu.com/" data-path="search/index?ct=201326592&cl=2&lm=-1&tn=baiduimage&istype=2&fm=&pv=&z=0&word=">图片</a></li>
<li><a href="http://v.baidu.com/" data-path="v?ct=3019898888&ie=utf-8&s=2&word=">视频</a></li>
<li><a href="http://map.baidu.com/" data-path="?newmap=1&ie=utf-8&s=s%26wd%3D">地图</a></li>
<li><a href="http://wenku.baidu.com/" data-path="search?ie=utf-8&word=">文库</a></li>
<div class="header-divider"></div>
</ul>
</div>
<div id="app_tooltip_qrcode">
<img src="//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/common/img/sidebar/newErweima_9fa03e0.png">
</div>
<div id="headerwrapper">
<div id="header" alog-group="header" alog-alias="hunter-header-start">

<table class="sbox" id="sbox" alog-group="search-box">
<tr>
<td class="logo">
<div class="logo">
<a href="http://news.baidu.com/">
<!--[if !IE]><!--><img src="https://box.bdimg.com/static/fisp_static/common/img/searchbox/logo_news_276_88_1f9876a.png" alt="百度新闻" height="46px" width="137px"><!--<![endif]-->
<!--[if IE 6]><img src="https://box.bdimg.com/static/fisp_static/common/img/searchbox/logo_news_276_88_for_ie6_1597c18.png" alt="百度新闻" height="46px" width="137px"><![endif]-->
<!--[if gt IE 6]><img src="https://box.bdimg.com/static/fisp_static/common/img/searchbox/logo_news_276_88_1f9876a.png" alt="百度新闻" height="46px" width="137px"><![endif]-->
</a>
</div>
<div class="date"></div>
</td>
<td class="search">
<table>
<tr>
<td class="box"><div id="sugarea"><span class="s_ipt_wr" id="s_ipt_wr"><input class="word" id="ww" name="word" size="42"  maxlength="100" tabindex="1"></span><span class="s_btn_wr"><input class="btn" id="s_btn_wr" type="button" value="百度一下" onmousedown="this.className='btn s_btn_h'" onmouseout="this.className='btn'"></span></div></td>
<td class="help"><a href="//help.baidu.com">帮助</a></td>
</tr>
</table>
<p class="search-radios">
<input type="radio" name="tn" value="news" checked="checked" id="news">
<label for="news" class="checked">新闻全文</label>
<input type="radio" name="tn" value="newstitle" id="newstitle">
<label for="newstitle" class="not-checked">新闻标题</label>
</p>
<input type="hidden" name="from" id="from" value="news">
<input type="hidden" name="cl" id="cl" value="2">
<input type="hidden" name="rn" id="rn" value="20">
<input type="hidden" name="ct" id="ct" value="1">
</td>
</tr>
</table>

</div>

<div id="menu" class="mod-navbar" alog-group="home-menu">
<div id="channel-shanghai" class="channel-shanghai clearfix"  style="display:none" >
<div class="menu-list">
<ul class="clearfix">
<li class="navitem-index current active"><a href="/">首页</a></li>
<li ><a href="/guonei">国内</a></li>
<li ><a href="/guoji">国际</a></li>
<li ><a href="/mil">军事</a></li>
<li ><a href="/finance">财经</a></li>
<li ><a href="/ent">娱乐</a></li>
<li ><a href="/sports">体育</a></li>
<li ><a href="/internet">互联网</a></li>
<li ><a href="/tech">科技</a></li>
<li ><a href="/game">游戏</a></li>
<li ><a href="/lady">女人</a></li>
<li ><a href="/auto">汽车</a></li>
<li ><a href="/house">房产</a></li>
</ul>
</div>
<i class="slogan"></i>
</div>
<div id="channel-all" class="channel-all clearfix" >
<div class="menu-list">
<ul class="clearfix">
<li class="navitem-index current active"><a href="/">首页</a></li>
<li ><a href="/guonei">国内</a></li>
<li ><a href="/guoji">国际</a></li>
<li ><a href="/mil">军事</a></li>
<li ><a href="/finance">财经</a></li>
<li ><a href="/ent">娱乐</a></li>
<li ><a href="/sports">体育</a></li>
<li ><a href="/internet">互联网</a></li>
<li ><a href="/tech">科技</a></li>
<li ><a href="/game">游戏</a></li>
<li ><a href="/lady">女人</a></li>
<li ><a href="/auto">汽车</a></li>
<li ><a href="/house">房产</a></li>
</ul>
</div>
<i class="slogan"></i>
</div>
</div>

</div>
<div id="body" alog-alias="b">

<div class="top-banner" id="topbanner"></div>
<div class="column clearfix" id="focus-top" style="margin-top: 12px; margin-bottom: 31px;">
<div class="l-left-col" alog-group="focus-top-left">
<div id="left-col-wrapper">
<div class="recommend-tip-wrapper">
<div class="tip-wrapper">
<div class="background-wrapper">
<a id="tip-float" class="mod-headline-tip" href="javascript:void(0);">
<div class="content-wrapper">
<i class="tip-logo"></i>
<div class="tip-content">点击刷新，将会有未读推荐</div>
</div>
</a>
</div>
</div>
</div>
<div id="headline-tabs" class="mod-headline-tab">
<ul class="clearfix">
<li class="active"><a href="javascript:void(0);" data-control="pane-news">热点要闻</a></li>
</ul>
<a id="tab-login" class="tab-login" href="javascript:void(0);" onclick="return false" mon="m=53&a=3"></a>
</div>
<div class="mod-tab-content">
<div id="pane-news" class="mod-tab-pane active">
<div class="hotnews" alog-group="focustop-hotnews">
<ul><li class="hdline0">
<i class="dot"></i>
<strong>
<a href="http://news.cctv.com/2019/12/10/ARTISVPiNSCB6N4xWZjRPkNV191210.shtml" target="_blank" class="a3" mon="ct=1&a=1&c=top&pn=0">疾风知劲草 中国经济坚定前行</a></strong>
</li>
<li class="hdline1">
<i class="dot"></i>
<strong>
<a href="http://m.news.cctv.com/2019/12/09/ARTIg9xqa0YMEvjSOv26pT2l191209.shtml" target="_blank"  mon="r=1"><b>打造高质量发展新引擎，习近平心中有“数”</b></a>
</strong>
</li>
<li class="hdline2">
<i class="dot"></i>
<strong>
<a href="http://www.xinhuanet.com//gangao/2019-12/10/c_1125331147.htm" target="_blank" class="a3" mon="ct=1&a=1&c=top&pn=1">访澳门特区立法会主席高开贤</a><i style="font-size: 12px">&nbsp;</i><a href="http://news.china.com.cn/node_8015554.html" target="_blank" class="a3" mon="ct=1&a=1&c=top&pn=1">澳门回归20周年</a>
</strong>
</li>
<li class="hdline3">
<i class="dot"></i>
<strong>
<a href="http://economy.southcn.com/e/2019-12/10/content_189760169.htm" target="_blank"  mon="r=1">庆祝澳门回归祖国20周年网络主题采访活动启动</a>
</strong>
</li>
<li class="hdline4">
<i class="dot"></i>
<strong>
<a href="http://xhpfmapi.zhongguowangshi.com/vh512/share/6671393?channel=weixin" target="_blank" class="a3" mon="ct=1&a=1&c=top&pn=2">海外人士谴责涉疆法案</a><i style="font-size: 12px">&nbsp;</i><a href="http://www.xinhuanet.com//legal/2019-12/10/c_1125330011.htm" target="_blank" class="a3" mon="ct=1&a=1&c=top&pn=2">"以疆制华"图谋必失败</a>
</strong>
</li>
<li class="hdline5">
<i class="dot"></i>
<strong>
<a href="http://finance.ce.cn/stock/gsgdbd/201912/09/t20191209_33805989.shtml" target="_blank"  mon="r=1">资本市场新一轮改革加速推进</a>
<i style="font-size: 12px">&nbsp;</i><a href="http://news.cctv.com/2019/12/09/ARTIxy8BeHFqG7fQDPc32B6r191209.shtml" target="_blank"  mon="r=1">制造业高质量发展</a>
</strong>
</li>
</ul>
</div>
<ul class="ulist focuslistnews">
<li class="bold-item">
<span class="dot"></span>
<a href="https://3w.huanqiu.com/a/78fa3c/9CaKrnKofHw?agt=8" mon="ct=1&amp;a=2&amp;c=top&pn=1" target="_blank">下个月可以放假13天！这件事需要提前计划</a></li>
<li>
<a href="https://3w.huanqiu.com/a/16dac8/9CaKrnKogzl?agt=8" mon="ct=1&amp;a=2&amp;c=top&pn=2" target="_blank">陆军举行晋升中将少将军衔仪式 </a></li>
<li>
<a href="https://baijiahao.baidu.com/s?id=1652579853012323046" mon="ct=1&amp;a=2&amp;c=top&pn=3" target="_blank">外交部回应美方涉疆言论：羡慕可以抹黑不接受</a></li>
<li>
<a href="https://3w.huanqiu.com/a/564394/9CaKrnKogrD?agt=8" mon="ct=1&amp;a=2&amp;c=top&pn=4" target="_blank">中国低轨遥感卫星分辨率达0.65米 最新高清大图发布 </a></li>
<li>
<a href="https://3w.huanqiu.com/a/3a1189/9CaKrnKogrJ?agt=8" mon="ct=1&amp;a=2&amp;c=top&pn=5" target="_blank">时隔俩月 储备肉增量投放！“双节”猪肉管够 </a></li>
<li>
<a href="https://3w.huanqiu.com/a/96194f/9CaKrnKogv3?agt=8" mon="ct=1&amp;a=2&amp;c=top&pn=6" target="_blank">最高法：以政府换届领导更替为由毁约要担责</a></li>
</ul>
<ul class="ulist focuslistnews" >
<li class="bold-item">
<span class="dot"></span>
<a href="https://3w.huanqiu.com/a/a4d1ef/9CaKrnKogrz?agt=8" mon="ct=1&amp;a=2&amp;c=top&pn=7" target="_blank">2020春运火车票明起开抢 回家路上将有这些新变化</a></li>
<li>
<a href="https://3w.huanqiu.com/a/3a1189/9CaKrnKogrI?agt=8" mon="ct=1&amp;a=2&amp;c=top&pn=8" target="_blank">明年个税专项附加扣除开始确认了 算算自己交多少税？</a></li>
<li>
<a href="http://baijiahao.baidu.com/s?id=1652576826785378111" mon="ct=1&amp;a=2&amp;c=top&pn=9" target="_blank">储户10分钟被划走近8万！央行新规防“扣款黑手”</a></li>
<li>
<a href="https://3w.huanqiu.com/a/c36dc8/9CaKrnKogtf?agt=8 " mon="ct=1&amp;a=2&amp;c=top&pn=10" target="_blank">香港教育局要对纵暴教师出手了 30宗教师违反操守面临惩处</a></li>
<li>
<a href="http://baijiahao.baidu.com/s?id=1652585635115233897" mon="ct=1&amp;a=2&amp;c=top&pn=11" target="_blank">任正非：美国帮我们宣传 华为不仅没赤字 收益还非常大</a></li>
<li>
<a href="https://3w.huanqiu.com/a/de583b/9CaKrnKogqh?agt=8" mon="ct=1&amp;a=2&amp;c=top&pn=12" target="_blank">蔡英文被起诉“论文虚假”，还被指有诈领高薪嫌疑 </a></li>
</ul>
<ul class="ulist focuslistnews" >
<li class="bold-item">
<span class="dot"></span>
<a href="https://3w.huanqiu.com/a/c36dc8/9CaKrnKogtA?agt=8" mon="ct=1&amp;a=2&amp;c=top&pn=13" target="_blank">美新泽西州发生枪击案致6死  执法人员:系"伏击" </a></li>
<li>
<a href="https://baijiahao.baidu.com/s?id=1652576960010875628" mon="ct=1&amp;a=2&amp;c=top&pn=14" target="_blank">滥用职权、妨碍国会 美众议院委员会宣布两项总统弹劾罪名</a></li>
<li>
<a href="https://3w.huanqiu.com/a/de583b/9CaKrnKogq0?agt=8" mon="ct=1&amp;a=2&amp;c=top&pn=15" target="_blank">亚马逊“状告”特朗普：将国防预算用于私利 </a></li>
<li>
<a href="http://baijiahao.baidu.com/s?id=1652577427912289436" mon="ct=1&amp;a=2&amp;c=top&pn=16" target="_blank">伊朗外交部警告公民：别去美国，有被捕风险</a></li>
<li>
<a href="http://baijiahao.baidu.com/s?id=1652581210471736650" mon="ct=1&amp;a=2&amp;c=top&pn=17" target="_blank">尼泊尔八成女孩生理期被隔离 “月经小屋”变“死亡之屋”</a></li>
<li>
<a href="https://3w.huanqiu.com/a/26ef70/9CaKrnKogCq?agt=8" mon="ct=1&amp;a=2&amp;c=top&pn=18" target="_blank">新西兰火山喷发两中国公民烧伤严重 一人清醒一人仍昏迷</a></li>
</ul>
<ul class="ulist focuslistnews" >
<li class="bold-item">
<span class="dot"></span>
<a href="https://3w.huanqiu.com/a/87f17a/9CaKrnKogAT?agt=8" mon="ct=1&amp;a=2&amp;c=top&pn=19" target="_blank">因翻译不准确，孙杨听证会结果将推迟公布 </a></li>
<li>
<a href="http://baijiahao.baidu.com/builder/preview/s?id=1652577991377550877" mon="ct=1&amp;a=2&amp;c=top&pn=20" target="_blank">公共场所心源性猝死事件频发 "救命神器"AED为何难普及？ </a></li>
<li>
<a href="https://3w.huanqiu.com/a/0c789f/9CaKrnKogrN?agt=8" mon="ct=1&amp;a=2&amp;c=top&pn=21" target="_blank">河南巩义发生三轮摩托车意外坠崖事件，已致6死1伤 </a></li>
<li>
<a href="http://baijiahao.baidu.com/s?id=1652573554790389498" mon="ct=1&amp;a=2&amp;c=top&pn=22" target="_blank">新疆厕所沉尸案被告人无罪后上诉：不是证据不足是没证据</a></li>
<li>
<a href="https://3w.huanqiu.com/a/0c789f/9CaKrnKogCf?agt=8" mon="ct=1&amp;a=2&amp;c=top&pn=23" target="_blank">法大副教授吴丹红代理劳荣枝案，“还有谜团未揭开” </a></li>
<li>
<a href="https://3w.huanqiu.com/a/564394/9CaKrnKogrC?agt=8" mon="ct=1&amp;a=2&amp;c=top&pn=24" target="_blank">血色燕窝是雨燕“呕心沥血”而成？ 实则是氧化发酵的结果</a></li>
</ul>
<ul class="ulist focuslistnews" >
<li class="bold-item">
<span class="dot"></span>
<a href="https://baijiahao.baidu.com/s?id=1652582740526007144&wfr=content" mon="ct=1&amp;a=2&amp;c=top&pn=25" target="_blank">注入灵魂!2019年度十大BGM出炉 你爱哪一首?</a></li>
<li>
<a href="https://3w.huanqiu.com/a/98a920/9CaKrnKogrO?agt=8" mon="ct=1&amp;a=2&amp;c=top&pn=26" target="_blank">女子陷入鉴宝骗局:10块钱金币“专家”估价1100万 </a></li>
<li>
<a href="https://3w.huanqiu.com/a/c4b13d/9CaKrnKogrt?agt=8" mon="ct=1&amp;a=2&amp;c=top&pn=27" target="_blank">开水烫餐具？饭菜凉了再放冰箱？好多小习惯可能都错了 </a></li>
<li>
<a href="https://3w.huanqiu.com/a/26ef70/9CaKrnKogyM?agt=8" mon="ct=1&amp;a=2&amp;c=top&pn=28" target="_blank">通报来了！私用救护车接机，浦东机场多人被处分 </a></li>
<li>
<a href="http://baijiahao.baidu.com/s?id=1652583812220092369" mon="ct=1&amp;a=2&amp;c=top&pn=29" target="_blank">室内运动场所缺乏，开放时间别扭，冬天去哪儿锻炼真愁</a></li>
<li>
<a href="https://3w.huanqiu.com/a/a4d1ef/9CaKrnKogrG?agt=8" mon="ct=1&amp;a=2&amp;c=top&pn=30" target="_blank">“单身狗养狗”：你的孤独，价值千亿 </a></li>
</ul>
</div>
<div id="pane-recommend" class="mod-tab-pane pane-recommend ">
<div class="mod-tab-loading">
<i class="icon-loading"></i>
<p class="desc">加载中请您耐心等待...</p>
</div>
<div class="tip-wrapper">
<a id="tip" class="mod-headline-tip" href="javascript:void(0);" mon="m=53&a=5">
<i class="tip-logo"></i>
<div class="tip-content">点击刷新，将会有未读推荐</div>
</a>
</div>
<script type="text/javascript">
            // 如果有图的文章出现白图的情况（图片大小小于10*10则视为白图），去掉图片展示
            function checkimg(obj){
                // console.log('obj.width: ' + obj.width);
                if(obj.naturalWidth < 10){
                    var picWrapper = obj.parentElement.parentElement;
                    var item = obj.parentElement.parentElement.parentElement;
                    // console.log('-------picWrapper');
                    // console.dir(picWrapper);
                    // console.log('-------item');
                    // console.dir(item);
                    picWrapper.style.display = 'none';
                    if (item.className.search('notb') > -1){
                        item.className = 'feeds-item-detail notb';
                    } else {
                        item.className = 'feeds-item-detail';
                    }
                }
            }
        </script>
<div class="feeds" id="feeds"></div>
<div class="feeds-more" id="feeds-more">
<a href="javascript:void(0);" onclick="return false" mon="m=53&a=4"><span>更多个性推荐新闻</span></a>
</div>
</div>
</div>
</div>
</div>
<div class="l-right-col" alog-group="focus-top-right">
<div class="toparea-aside-top" alog-group="focustop-carousel">
<div class="imgplayer clearfix" id="imgplayer">
<div id="imgplayer-control" class="carousel-control">
<a href="javascript:void(0);" mon="c=top&a=50&col=4&ct=1&pn=0" id="imgplayer-prev" class="carousel-btn-prev">
<span class="icon-wrap"></span>
</a>
<a href="javascript:void(0);" mon="c=top&a=52&col=4&ct=1&pn=0" id="imgplayer-next" class="carousel-btn-next">
<span class="icon-wrap"></span>
</a>
</div>
<div class="imgview" id="imgView">
<a href="javascript:void(0);" target="_blank"></a>
</div>
<div class="imgnav-mask"></div>
<div class="imgnav" id="imgNav">
<a class="navbtn" index="8" mon="c=top&a=51&col=4&ct=1&pn=8" href="javascript:void(0);">8</a>
<a class="navbtn" index="7" mon="c=top&a=51&col=4&ct=1&pn=7" href="javascript:void(0);">7</a>
<a class="navbtn" index="6" mon="c=top&a=51&col=4&ct=1&pn=6" href="javascript:void(0);">6</a>
<a class="navbtn" index="5" mon="c=top&a=51&col=4&ct=1&pn=5" href="javascript:void(0);">5</a>
<a class="navbtn" index="4" mon="c=top&a=51&col=4&ct=1&pn=4" href="javascript:void(0);">4</a>
<a class="navbtn" index="3" mon="c=top&a=51&col=4&ct=1&pn=3" href="javascript:void(0);">3</a>
<a class="navbtn" index="2" mon="c=top&a=51&col=4&ct=1&pn=2" href="javascript:void(0);">2</a>
<a class="navbtn" index="1" mon="c=top&a=51&col=4&ct=1&pn=1" href="javascript:void(0);">1</a>
</div>
<div class="imgtit" id="imgTitle">
<a href="javascript:void(0);" target="_blank"></a>
</div>
</div>
<ul class="sub_19da">
<a  class="home-banner-cell left" href="http://www.qstheory.cn/zt2019/llxjj/index.htm" ></a>
<a  class="home-banner-cell right" href="http://www.qstheory.cn/zt2017/xcgcdd19djs/index.htm" ></a>
</ul>
<div class="sda_line">
</div>
</div>
<div alog-group="focus-top-news-hotwords">
<div class="mod h-bd-box" id="news-hotwords">
<div class="hd line"><h3>热搜新闻词<span class="en">HOT WORDS</span></h3></div>
<div class="bd">
<ul class="hotwords clearfix">
<li class="li_0 li_color_0 button-slide">
<a href="https://www.baidu.com/s?wd=%E4%B9%A0%E8%BF%91%E5%B9%B3%E5%90%8C%E6%AC%A7%E6%B4%B2%E7%90%86%E4%BA%8B%E4%BC%9A%E4%B8%BB%E5%B8%AD%E7%B1%B3%E6%AD%87%E5%B0%94%E9%80%9A%E8%AF%9D" target="_blank" class="hotwords_li_a" title="习近平同欧洲理事会主席米歇尔通话" mon="ct=1&amp;c=top&amp;a=30&pn=1">习近平同欧洲理事会主席米歇尔通话</a>
</li>
<li class="li_1 li_color_1 button-slide">
<a href="https://www.baidu.com/s?wd=%E4%B9%A0%E8%BF%91%E5%B9%B3%E5%AF%B9%E5%86%9B%E9%98%9F%E8%80%81%E5%B9%B2%E9%83%A8%E5%B7%A5%E4%BD%9C%E4%BD%9C%E5%87%BA%E9%87%8D%E8%A6%81%E6%8C%87%E7%A4%BA" target="_blank" class="hotwords_li_a" title="习近平对军队老干部工作作出重要指示" mon="ct=1&amp;c=top&amp;a=30&pn=2">习近平对军队老干部工作作出重要指示</a>
</li>
<li class="li_2 li_color_2 button-slide">
<a href="https://www.baidu.com/s?wd=%E5%B9%B4%E5%BA%A6%E8%AF%8D%E6%B1%87%E7%BA%B7%E5%87%BA%E7%82%89" target="_blank" class="hotwords_li_a" title="年度词汇纷出炉" mon="ct=1&amp;c=top&amp;a=30&pn=3">年度词汇纷出炉</a>
</li>
<li class="li_3 li_color_3 button-slide">
<a href="https://www.baidu.com/s?wd=%E9%92%B1%E5%AD%A6%E6%A3%AE%E8%AF%9E%E8%BE%B0108%E5%91%A8%E5%B9%B4" target="_blank" class="hotwords_li_a" title="钱学森诞辰108周年" mon="ct=1&amp;c=top&amp;a=30&pn=4">钱学森诞辰108周年</a>
</li>
<li class="li_4 li_color_4 button-slide">
<a href="https://www.baidu.com/s?wd=%E6%B3%B0%E5%B1%B1%E7%9F%B3%E5%85%A8%E9%9D%A2%E7%A6%81%E5%94%AE" target="_blank" class="hotwords_li_a" title="泰山石全面禁售" mon="ct=1&amp;c=top&amp;a=30&pn=5">泰山石全面禁售</a>
</li>
<li class="li_5 li_color_5 button-slide">
<a href="https://www.baidu.com/s?wd=iPhone%E5%B0%86%E6%94%AF%E6%8C%81VoLTE%E5%8A%9F%E8%83%BD" target="_blank" class="hotwords_li_a" title="iPhone将支持VoLTE功能" mon="ct=1&amp;c=top&amp;a=30&pn=6">iPhone将支持VoLTE功能</a>
</li>
<li class="li_6 li_color_6 button-slide">
<a href="https://www.baidu.com/s?wd=SpaceX%EF%BC%9A12%E6%9C%88%E5%92%8C1%E6%9C%88%E5%B0%86%E5%86%8D%E5%8F%91%E5%B0%84%E6%98%9F%E9%93%BE%E5%8D%AB%E6%98%9F" target="_blank" class="hotwords_li_a" title="SpaceX：12月和1月将再发射星链卫星" mon="ct=1&amp;c=top&amp;a=30&pn=7">SpaceX：12月和1月将再发射星链卫星</a>
</li>
<li class="li_7 li_color_7 button-slide">
<a href="https://www.baidu.com/s?wd=2020%E6%98%A5%E8%BF%90%E7%81%AB%E8%BD%A6%E7%A5%A8%E6%98%8E%E8%B5%B7%E5%BC%80%E6%8A%A2" target="_blank" class="hotwords_li_a" title="2020春运火车票明起开抢" mon="ct=1&amp;c=top&amp;a=30&pn=8">2020春运火车票明起开抢</a>
</li>
<li class="li_8 li_color_8 button-slide">
<a href="https://www.baidu.com/s?wd=%E8%A7%86%E8%A7%89%E4%B8%AD%E5%9B%BD%E5%86%8D%E9%81%AD%E6%95%B4%E6%94%B9" target="_blank" class="hotwords_li_a" title="视觉中国再遭整改" mon="ct=1&amp;c=top&amp;a=30&pn=9">视觉中国<br/>再遭整改</a>
</li>
<li class="li_9 li_color_9 button-slide">
<a href="https://www.baidu.com/s?wd=%E4%B8%AD%E5%9B%BD%E9%80%9F%E6%BB%91%E9%A6%96%E5%A4%BA%E9%87%91%E7%89%8C" target="_blank" class="hotwords_li_a" title="中国速滑首夺金牌" mon="ct=1&amp;c=top&amp;a=30&pn=10">中国速滑<br/>首夺金牌</a>
</li>
</ul>
</div>
</div>
</div>
<div class="mod-baijia column clearfix" id="baijia" alog-group="log-baijia">
<div class="column-title-home">
<div class="column-title-border">
<h2>
<span class="column-title">百家号</span>
<span class="en">BAIJIA</span>
</h2>
<div class="sub-class">
</div>
</div>
</div>
<div class="l-middle-col" style="height:305px;" alog-group="log-baijia-left-up">
<div class="imagearea">
<div class="imagearea-top" style="height:164px;">
<div class="image-mask-item">
<a href="http://baijiahao.baidu.com/s?id=1652436239093085899" target="_blank" class="item-image" mon="&a=12" title="杨振宁惊扰了中国的大对撞机之梦" style="background-image:url(http://hiphotos.baidu.com/news/crop%3D0%2C43%2C515%2C346%3Bq%3D80%3B/sign=549728e96381800a7aaad34e8c051fce/4a36acaf2edda3ccf91669460ee93901203f92e2.jpg)"></a>
<a href="http://baijiahao.baidu.com/s?id=1652436239093085899" target="_blank" class="item-title" title="杨振宁惊扰了中国的大对撞机之梦" mon="&a=9">杨振宁惊扰了中国的大对撞机之梦</a>
</div>
</div>
<div class="imagearea-bottom">
<div class="image-list-item">
<a href="http://baijiahao.baidu.com/s?id=1652453330851906654" title="8亿豪赌 B站拿下LOL三年独播权" target="_blank" mon="&a=12" class="img" style="background-image:url(http://hiphotos.baidu.com/news/crop%3D78%2C0%2C535%2C359%3Bq%3D80%3B/sign=c6a8d17cc95c1038303194828f26ab3f/6f061d950a7b0208540cee876dd9f2d3562cc88b.jpg)"></a><a href="http://baijiahao.baidu.com/s?id=1652453330851906654" mon="&a=9"  class="txt" target="_blank">8亿豪赌 B站拿下LOL三年独播权</a>
</div>
<div class="image-list-item">
<a href="http://baijiahao.baidu.com/s?id=1652398315665401501" title="电动车充电桩生意掉下风口" target="_blank" mon="&a=12" class="img" style="background-image:url(http://hiphotos.baidu.com/news/crop%3D0%2C0%2C507%2C340%3Bq%3D80%3B/sign=c5e76357ae8b87d6440df15f3a380408/b17eca8065380cd7e7d8738bae44ad3458828196.jpg)"></a><a href="http://baijiahao.baidu.com/s?id=1652398315665401501" mon="&a=9"  class="txt" target="_blank">电动车充电桩生意掉下风口</a>
</div>
</div>
</div>
</div>
<div class="l-right-col" style="width:290px;" alog-group="log-baijia-right-up">
<div class="baijia-focus-list">
<ul class="ulist bdlist">
<li class="bold-item"><a href="http://baijiahao.baidu.com/s?id=1652491964596459978" target="_blank" mon="a=9">华为考虑欧洲建厂生产5G设备</a></li>
<li><a href="http://baijiahao.baidu.com/s?id=1652495595499647247" target="_blank" mon="a=9">OPPO创始人：有一半员工负责IoT等新兴业务</a></li>
<li><a href="http://baijiahao.baidu.com/s?id=1652496245658267917" target="_blank" mon="a=9">高通总裁：中国5G规模将领先世界</a></li>
<li><a href="http://baijiahao.baidu.com/s?id=1652496722437763206" target="_blank" mon="a=9">京东设立集团技术委员会 将构建技术品牌</a></li>
<li><a href="http://baijiahao.baidu.com/s?id=1652494754786382549" target="_blank" mon="a=9">亚马逊AWS遭微软谷歌猛追 先发优势正被追平</a></li>
</ul>
<ul class="ulist bdlist" style="padding-top:5px">
<li class="bold-item"><a href="http://baijiahao.baidu.com/s?id=1652446340098940075" target="_blank" mon="a=9">比特大陆创始人大战特别股东会</a></li>
<li><a href="http://baijiahao.baidu.com/s?id=1652440878999963532" target="_blank" mon="a=9">水滴筹线下团队周三前将恢复试运营</a></li>
<li><a href="http://baijiahao.baidu.com/s?id=1652457903640314399" target="_blank" mon="a=9">三星电子3名高管被判入狱两年</a></li>
<li><a href="http://baijiahao.baidu.com/s?id=1652485286277480369" target="_blank" mon="a=9">苹果将正式参加CES 2020，上次参加是1992年</a></li>
<li><a href="http://baijiahao.baidu.com/s?id=1652484516744187612" target="_blank" mon="a=9">罗森布拉特证券：iPhone 11 Pro减产25%</a></li>
</ul>
<ul class="ulist bdlist" style="padding-top:5px">
<li class="bold-item"><a href="http://baijiahao.baidu.com/s?id=1652487292497442684" target="_blank" mon="a=9">谷歌新当家皮查伊的登顶之路</a></li>
<li><a href="http://baijiahao.baidu.com/s?id=1652446910866024804" target="_blank" mon="a=9">Win 7国内份额仍达60%，Win 10份额刚超21%</a></li>
<li><a href="http://baijiahao.baidu.com/s?id=1652486958483043318" target="_blank" mon="a=9">分析师：2020年发布6款iPhone机型</a></li>
<li><a href="http://baijiahao.baidu.com/s?id=1652436584974119241" target="_blank" mon="a=9">滴滴盈利破局：挑战尚存，但美团不是归宿</a></li>
<li><a href="http://baijiahao.baidu.com/s?id=1652497913648743657" target="_blank" mon="a=9">王卫卸任顺丰旗下公司董事长</a></li>
<li><a href="http://baijiahao.baidu.com/s?id=1652438785258324090" target="_blank" mon="a=9">首批23家移动金融App试点备案名单出炉</a></li>
</ul>
</div>
</div>
<div class="l-middle-col" alog-group="log-baijia-left-down">
<div class="mod tbox" id="baijia-aside-recommend">
<div class="bd" style="position:relative;height:160px;overflow:hidden;">
<div class="imagearea">
<div class="imagearea-top">
<div class="image-mask-item">
<a href="http://baijiahao.baidu.com/s?id=1652488701837640888" target="_blank" class="item-image" mon="&a=12" title="盘点2019：科技互联网20大事件" style="background-image:url(http://hiphotos.baidu.com/news/crop%3D52%2C0%2C536%2C360%3Bq%3D80%3B/sign=c2f3ff1a5e0fd9f9b4580f291818e606/1e30e924b899a90165038b5012950a7b0208f5a6.jpg)"></a>
<a href="http://baijiahao.baidu.com/s?id=1652488701837640888" target="_blank" class="item-title" title="盘点2019：科技互联网20大事件" mon="&a=9">盘点2019：科技互联网20大事件</a>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="mod-localnews column clearfix" id="local_news">
<div class="column-title-home" alog-group="log-mil-title">
<div class="column-title-border">
<h2><span id="city_name"><span style="padding-right: 5px"><span>北京</span>新闻</span></span><span class="cname">LOCAL NEWS</span></h2>
<div class="localnews_logo" id="localnews_logo"></div>
<a id="change-city" class="select-btn">切换城市</a>
<span id="p-more-link"></span>
</div>
</div>
<div class="l-left-col col-mod" alog-group="log-local-left">
<ul class="ulist focuslistnews" id="localnews-focus">
</ul>
</div>
<div class="l-middle-col" alog-group="log-local-middle">
<div class="mod">
<div class="hd">
<h3>新闻图片</h3>
</div>
<div class="bd">
<div class="imagearea" id="local_default" style="display:block">
<div class="imagearea-top">
<div class="image-mask-item">
<a href="" target="_blank" class="item-image" mon="&amp;pn=1&a=12" title=""><img src="" alt=""/></a>
<a href="" target="_blank" class="item-title" title="" mon="&amp;pn=1&a=9"></a>
</div>
</div>
</div>
<div class="imagearea" id="local_current" style="display:none">
<div class="imagearea-top" id="localnews-pic">
</div>
</div>
</div>
</div>
</div>
<div class="l-right-col" alog-group="log-local-right">
<div class="mod tbox" id="internet-aside-gsdt">
<div class="hd line"><h3>新闻资讯</h3></div>
<div class="bd" id="localnews-zixun">
<ul class="ulist">
</ul>
</div>
</div>
</div>
<div class="ad-banner" id="localNews_ad"></div>
<div id="city_view" class="city_view">
<div class="city_list"></div>
<div id="btn_back" class="btn_back">返回</div>
<div id="btn_close" class="btn_close"></div>
<p class="city-tip">您所选城市新闻不足，将展示省会新闻</p>
<div class="up_triangle"></div>
</div>
<div id="status" class="loading">正在加载，请稍候...</div>
</div>
<ul id="goTop" class="mod-sidebar">
<li class="item report button-rotate" data-text="举报">
<a href="http://report.12377.cn:13225/toreportinputNormal_anis.do">举报</a>
</li>
<li class="item qr-code button-rotate" data-text="二维码">
<a href="javascript:void(0);">二维码</a>
</li>
<li class="qr-code-container clearfix">
<span class="item-container left">
<span class="img-container">
<img src="//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/common/img/sidebar/newErweima_9fa03e0.png"/>
</span>
</span>
<span class="item-container right">
<p class="title">百度新闻客户端</p>
<ul>
<li>扫描二维码下载</li>
<li>随时随地收看更多新闻</li>
</ul>
</span>
</li>
<li class="item favorite button-rotate" data-text="收藏本站">
<a href="javascript:void(0);">收藏本站</a>
</li>
<li class="item search button-rotate" data-text="搜索">
<a href="javascript:void(0);" id="search-btn">搜索</a>
</li>
<li class="item feedback button-rotate" id="feedbackbtn" data-text="用户反馈">
<a href="javascript:void(0);">用户反馈</a>
</li>
<li class="item gotop">
<a id="gotop_btn" href="javascript:void(0);" onclick="window.scroll(0, 0)"></a>
</li>
<li class="searchbox">
<span class="close-btn"></span>
<p>
<input type="hidden" name="tn" id="tn" value="news"/>
<input type="hidden" name="from" id="from" value="news"/>
<input type="hidden" name="cl" id="cl" value="2"/>
<input type="hidden" name="rn" id="rn" value="20"/>
<input type="hidden" name="ct" id="ct" value="1"/>
<input class="searchInput" type="text" value="输入搜索词" name="word" autocomplete="off" tabindex="1" maxlength="100"/>
<button class="submit-btn" type="button">搜索</button>
</p>
</li>
<li class="close-tip">收起<i class="arrow"></i></li>
</ul>
<style>
#goTop{
    position: fixed;
    width: 54px;
    left: 50%;
    margin-left: 502px;
    bottom: 20px;
    _position: absolute;
    _top: expression(eval(document.documentElement.scrollTop || document.body.scrollTop)+eval(document.documentElement.clientHeight || document.body.clientHeight)-361+'px');
    z-index:998;
}
</style>

</div>

<div id="footerwrapper">
<div class="bottombar" alog-group="log-footer-bottombar" alog-alias="hunter-start-bottombar">
<div class="bottombar-inner clearfix">
<div class="bot-left">
<div class="title-container">
<i class="icon">&nbsp;</i>
<h4>更多精彩内容</h4>
</div>
<div class="qrcode-container clearfix">
<div class="img-container">
<img src="//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/common/img/footer/newErweima_9fa03e0.png">
</div>
<div class="link-container">
<a href="http://downpack.baidu.com/baidunews_AndroidPhone_1014720b.apk" target="_blank">Android版下载</a>
<a href="https://itunes.apple.com/cn/app/id482820737" target="_blank">iPhone版下载</a>
</div>
<p class="info">扫描二维码, 收看更多新闻</p>
</div>
</div>
<div class="bot-right">
<div class="title-container">
<i class="icon">&nbsp;</i>
<h4>百度新闻独家出品</h4>
</div>
<ol>
<li>1. 新闻由机器选取每5分钟自动更新</li>
<li>2. 百度新闻搜索源于互联网新闻网站和频道，系统自动分类排序</li>
<li>3. 百度不刊登或转载任何完整的新闻内容</li>
</ol>
</div>
</div>
</div>
<div style="font-size:12px;text-align:center;">
责任编辑：胡彦BN098 刘石娟BN068 谢建BN085 李芳雨BN091 储信艳BN087 焦碧碧BN084 禤聪BN095 王鑫BN060 崔超BN071 违法和不良信息举报电话：400-921-6911</div>
<div id="footer" alog-group="log-footer" alog-alias="hunter-start-footer">
<a href="//news-bos.cdn.bcebos.com/mvideo/baidu_news_protocol.html">用户协议</a>
<a href="https://www.baidu.com/duty/wise/wise_secretright.html">隐私策略</a>
<a href="//help.baidu.com/newadd?prod_id=5&category=1">投诉中心</a>
<span>京公网安备11000002000001号</span>
<a href="//news-bos.cdn.bcebos.com/mvideo/pcnews_licence.html">互联网新闻信息服务许可</a>
<span>&copy;2019Baidu</span>
<a class="cy" href="//www.baidu.com/duty/">使用百度前必读</a>
<a target="_blank" class="img-link img-link1" href="http://net.china.cn/chinese/index.htm">
</a>
<a target="_blank" class="img-link img-link2" href="http://www.cyberpolice.cn/wfjb/">
</a>
<a target="_blank" class="img-link img-link3" href="http://www.bjjubao.org/">
</a>
</div>
</div>
<style>
.focustop-anchor{
    height:0;
    line-height:0;
    font-size:0;
}
#headerwrapper{
    width:100%;
}
</style>
</body><script type="text/javascript" src="//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/common/lib/mod_b818356.js"></script>
<script type="text/javascript">require.resourceMap({"res":{"common:widget/lib/tangram/base/base.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/lib/tangram/base/base_c518988.js","pkg":"common:p0"},"common:widget/lib/magic/magic.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/lib/magic/magic_56edf31.js","pkg":"common:p0"},"common:widget/lib/magic/Base/Base.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/lib/magic/Base/Base_50a505e.js","pkg":"common:p0","deps":["common:widget/lib/tangram/base/base.js","common:widget/lib/magic/magic.js"]},"common:widget/lib/magic/control/control.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/lib/magic/control/control_5c7cfca.js","pkg":"common:p0","deps":["common:widget/lib/tangram/base/base.js","common:widget/lib/magic/magic.js"]},"common:widget/lib/magic/control/Layer/Layer.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/lib/magic/control/Layer/Layer_ccd8d01.js","pkg":"common:p0","deps":["common:widget/lib/tangram/base/base.js","common:widget/lib/magic/magic.js","common:widget/lib/magic/Base/Base.js","common:widget/lib/magic/control/control.js"]},"common:widget/lib/magic/Mask/Mask.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/lib/magic/Mask/Mask_d1105f9.js","pkg":"common:p0","deps":["common:widget/lib/tangram/base/base.js","common:widget/lib/magic/magic.js","common:widget/lib/magic/control/Layer/Layer.js"]},"common:widget/lib/magic/setup/setup.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/lib/magic/setup/setup_8207eff.js","pkg":"common:p0","deps":["common:widget/lib/tangram/base/base.js","common:widget/lib/magic/magic.js"]},"common:widget/lib/magic/_query/_query.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/lib/magic/_query/_query_a974d80.js","pkg":"common:p0","deps":["common:widget/lib/tangram/base/base.js","common:widget/lib/magic/magic.js"]},"common:widget/lib/magic/control/Tab/Tab.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/lib/magic/control/Tab/Tab_6e3b376.js","pkg":"common:p0","deps":["common:widget/lib/tangram/base/base.js","common:widget/lib/magic/magic.js","common:widget/lib/magic/Base/Base.js","common:widget/lib/magic/control/control.js","common:widget/lib/magic/_query/_query.js"]},"common:widget/lib/magic/setup/tab/tab.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/lib/magic/setup/tab/tab_7ca296e.js","pkg":"common:p0","deps":["common:widget/lib/tangram/base/base.js","common:widget/lib/magic/magic.js","common:widget/lib/magic/setup/setup.js","common:widget/lib/magic/control/Tab/Tab.js"]},"common:widget/lib/magic/control/Dialog/Dialog.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/lib/magic/control/Dialog/Dialog_c2b9c1a.js","pkg":"common:p0","deps":["common:widget/lib/tangram/base/base.js","common:widget/lib/magic/magic.js","common:widget/lib/magic/control/Layer/Layer.js"]},"common:widget/lib/magic/Background/Background.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/lib/magic/Background/Background_353ebd3.js","pkg":"common:p0","deps":["common:widget/lib/tangram/base/base.js","common:widget/lib/magic/magic.js","common:widget/lib/magic/Base/Base.js"]},"common:widget/lib/magic/Dialog/Dialog.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/lib/magic/Dialog/Dialog_239df5f.js","pkg":"common:p0","deps":["common:widget/lib/tangram/base/base.js","common:widget/lib/magic/magic.js","common:widget/lib/magic/control/Dialog/Dialog.js","common:widget/lib/magic/Background/Background.js"]},"common:widget/lib/magic/control/Dialog/$mask/$mask.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/lib/magic/control/Dialog/$mask/$mask_50466b3.js","pkg":"common:p0","deps":["common:widget/lib/tangram/base/base.js","common:widget/lib/magic/magic.js","common:widget/lib/magic/control/Dialog/Dialog.js","common:widget/lib/magic/Mask/Mask.js"]},"common:widget/ui/jquery/jquery.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/ui/jquery/jquery_5d7279d.js","pkg":"common:p1"},"common:widget/ui/jquery/jquery.cookie.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/ui/jquery/jquery.cookie_e1f1479.js","pkg":"common:p1"},"common:widget/banner_ad/banner_ad.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/banner_ad/banner_ad_5c31727.js","pkg":"common:p1","deps":["common:widget/ui/jquery/jquery.js","common:widget/ui/jquery/jquery.cookie.js"]},"common:widget/banner_ad/banner_ad_data.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/banner_ad/banner_ad_data_aff68ed.js","pkg":"common:p1"},"common:widget/dep/jQuery/plugins/jquery.lavalamp.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/dep/jQuery/plugins/jquery.lavalamp_5a9954b.js","pkg":"common:p1"},"common:widget/favorite/favorite.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/favorite/favorite_bfc0622.js","pkg":"common:p1","deps":["common:widget/ui/jquery/jquery.js","common:widget/ui/jquery/jquery.cookie.js"]},"common:widget/feedback/feedback.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/feedback/feedback_6e10548.js","pkg":"common:p1","deps":["common:widget/ui/jquery/jquery.js","common:widget/ui/jquery/jquery.cookie.js"]},"common:widget/fixedpannel/fixedpannel.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/fixedpannel/fixedpannel_bf4dc4c.js","pkg":"common:p1","deps":["common:widget/lib/tangram/base/base.js","common:widget/lib/magic/magic.js","common:widget/lib/magic/control/Layer/Layer.js","common:widget/lib/magic/Mask/Mask.js","common:widget/lib/magic/setup/tab/tab.js","common:widget/lib/magic/Dialog/Dialog.js"]},"common:widget/footer/statistics.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/footer/statistics_83e2581.js","pkg":"common:p1","deps":["common:widget/ui/jquery/jquery.js"]},"common:widget/header/header.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/header/header_c2a1ecd.js","pkg":"common:p1","deps":["common:widget/ui/jquery/jquery.js"]},"common:widget/hunter/hunter.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/hunter/hunter_2113114.js","pkg":"common:p1"},"common:widget/navbar/navbar.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/navbar/navbar_3ad387b.js","pkg":"common:p1","deps":["common:widget/dep/jQuery/plugins/jquery.lavalamp.js","common:widget/ui/jquery/jquery.js"]},"common:widget/searchbox/searchbox.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/searchbox/searchbox_21149bc.js","pkg":"common:p1","deps":["common:widget/lib/tangram/base/base.js"]},"common:widget/searchbox/searchboxActive.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/searchbox/searchboxActive_f139a7f.js","pkg":"common:p1","deps":["common:widget/ui/jquery/jquery.js"]},"common:widget/searchbox/searchradio.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/searchbox/searchradio_e67ae37.js","pkg":"common:p1","deps":["common:widget/ui/jquery/jquery.js"]},"common:widget/second_navbar/fold.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/second_navbar/fold_b1dea17.js","pkg":"common:p1","deps":["common:widget/ui/jquery/jquery.js"]},"common:widget/show_top_qrcode/show_top_qrcode.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/show_top_qrcode/show_top_qrcode_db04dfa.js","pkg":"common:p1","deps":["common:widget/ui/jquery/jquery.js"]},"common:widget/sidebar/sidebar.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/sidebar/sidebar_8df2d84.js","pkg":"common:p1","deps":["common:widget/ui/jquery/jquery.js","common:widget/feedback/feedback.js"]},"common:widget/ui/jquery/jquery-ui.min.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/ui/jquery/jquery-ui.min_793696a.js","pkg":"common:p1"},"common:widget/ui/jquery/jquery.animateEvents.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/ui/jquery/jquery.animateEvents_fa2738c.js","pkg":"common:p1"},"common:widget/ui/vs/vs.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/ui/vs/vs_ac8f6e6.js","pkg":"common:p1","deps":["common:widget/lib/tangram/base/base.js"]},"common:widget/ui/vs/observer/observer.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/ui/vs/observer/observer_7031f75.js","pkg":"common:p1"},"common:widget/ui/vs/ContentPlayer/ContentPlayer.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/ui/vs/ContentPlayer/ContentPlayer_cfa437e.js","pkg":"common:p1","deps":["common:widget/lib/tangram/base/base.js","common:widget/ui/vs/vs.js","common:widget/ui/vs/observer/observer.js"]},"common:widget/ui/vs/DynamicList/DynamicList.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/ui/vs/DynamicList/DynamicList_757360e.js","pkg":"common:p1","deps":["common:widget/lib/tangram/base/base.js","common:widget/ui/vs/vs.js","common:widget/ui/vs/observer/observer.js"]},"common:widget/ui/vs/ScrollView/ScrollView.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/ui/vs/ScrollView/ScrollView_e529192.js","pkg":"common:p1","deps":["common:widget/lib/tangram/base/base.js","common:widget/ui/vs/vs.js"]},"common:widget/ui/vs/Slide/Slide.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/ui/vs/Slide/Slide_bcb1535.js","pkg":"common:p1","deps":["common:widget/ui/jquery/jquery.js"]},"common:widget/ui/vs/citylist/citylist.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/ui/vs/citylist/citylist_39082c3.js","pkg":"common:p1"},"common:widget/ui/vs/clickMonitor/clickMonitor.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/ui/vs/clickMonitor/clickMonitor_3b94ea0.js","pkg":"common:p1","deps":["common:widget/lib/tangram/base/base.js"]},"common:widget/ui/vs/delayload/delayload.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/ui/vs/delayload/delayload_360bc2c.js","pkg":"common:p1","deps":["common:widget/lib/tangram/base/base.js"]},"common:widget/ui/vs/enterState/enterState.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/ui/vs/enterState/enterState_4f3114b.js","pkg":"common:p1","deps":["common:widget/lib/tangram/base/base.js"]},"common:widget/ui/vs/imgLazyLoad/ImglazyLoad.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/ui/vs/imgLazyLoad/ImglazyLoad_f2b8599.js","pkg":"common:p1"},"common:widget/ui/vs/slider/slider.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/ui/vs/slider/slider_32bdf45.js","pkg":"common:p1","deps":["common:widget/lib/tangram/base/base.js"]},"common:widget/ui/vs/suggestion/suggestion.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/ui/vs/suggestion/suggestion_f2b3c80.js","pkg":"common:p1","deps":["common:widget/lib/tangram/base/base.js"]},"common:widget/ui/vs/utils/utils.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/common/widget/ui/vs/utils/utils_73e2453.js","pkg":"common:p1"},"news:widget/HouseNews/HouseNews.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/news/widget/HouseNews/HouseNews_4ceed49.js","pkg":"news:p0","deps":["common:widget/ui/vs/DynamicList/DynamicList.js","common:widget/ui/vs/vs.js","common:widget/lib/tangram/base/base.js","common:widget/ui/vs/citylist/citylist.js","common:widget/ui/jquery/jquery.js"]},"news:widget/LocalNews/LocalNews.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/news/widget/LocalNews/LocalNews_e5984a9.js","pkg":"news:p0","deps":["common:widget/ui/vs/DynamicList/DynamicList.js","common:widget/ui/vs/vs.js","common:widget/lib/tangram/base/base.js","common:widget/ui/vs/citylist/citylist.js","common:widget/ui/jquery/jquery.js"]},"news:widget/TopBanner/TopBanner.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/news/widget/TopBanner/TopBanner_6f86843.js","pkg":"news:p0","deps":["common:widget/ui/jquery/jquery.js"]},"news:widget/col_media/col_media.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/news/widget/col_media/col_media_c2b0b0c.js","pkg":"news:p0"},"news:widget/events/events.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/news/widget/events/events_b4e3140.js","pkg":"news:p0"},"news:widget/hotrollnews/hotrollnews.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/news/widget/hotrollnews/hotrollnews_debd370.js","pkg":"news:p0","deps":["common:widget/lib/tangram/base/base.js"]},"news:widget/hotwords/hotwords.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/news/widget/hotwords/hotwords_85ad191.js","pkg":"news:p0","deps":["common:widget/ui/jquery/jquery.js"]},"news:widget/hx_stock/hx_stock.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/news/widget/hx_stock/hx_stock_71853d1.js","pkg":"news:p0","deps":["common:widget/lib/tangram/base/base.js","common:widget/ui/vs/vs.js"]},"news:widget/mod_baijia/mod_baijia.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/news/widget/mod_baijia/mod_baijia_471a804.js","pkg":"news:p0","deps":["common:widget/lib/tangram/base/base.js"]},"news:widget/mod_headline_tab/mod_headline_recommend.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/news/widget/mod_headline_tab/mod_headline_recommend_15dbeeb.js","pkg":"news:p0","deps":["common:widget/ui/jquery/jquery.js"]},"news:widget/mod_headline_tab/mod_headline_tab.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/news/widget/mod_headline_tab/mod_headline_tab_7304c05.js","pkg":"news:p0","deps":["common:widget/ui/jquery/jquery.js","common:widget/ui/jquery/jquery.cookie.js","news:widget/mod_headline_tab/mod_headline_recommend.js"]},"news:widget/mod_pagination/mod_pagination.js":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/news/widget/mod_pagination/mod_pagination_20b212d.js","pkg":"news:p0"}},"pkg":{"common:p0":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/common/framework_static_include/framework_static_include_aa59e0d.js"},"common:p1":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/common/module_static_include/module_static_include_5309ae3.js"},"news:p0":{"url":"//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/news/focustop/focustop_b924ecb.js"}}});</script><script type="text/javascript" src="//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/news/focustop/focustop_b924ecb.js"></script>
<script type="text/javascript" src="//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/common/framework_static_include/framework_static_include_aa59e0d.js"></script>
<script type="text/javascript" src="//gss0.bdstatic.com/5foIcy0a2gI2n2jgoY3K/static/fisp_static/common/module_static_include/module_static_include_5309ae3.js"></script>
<script type="text/javascript">!function(){    	void function(a,b,c,d,e,f,g){a.alogObjectName=e,a[e]=a[e]||function(){(a[e].q=a[e].q||[]).push(arguments)},a[e].l=a[e].l||+new Date,d="https:"===a.location.protocol?"https://fex.bdstatic.com"+d:"http://fex.bdstatic.com"+d;var h=!0;if(a.alogObjectConfig&&a.alogObjectConfig.sample){var i=Math.random();a.alogObjectConfig.rand=i,i>a.alogObjectConfig.sample&&(h=!1)}h&&(f=b.createElement(c),f.async=!0,f.src=d+"?v="+~(new Date/864e5)+~(new Date/864e5),g=b.getElementsByTagName(c)[0],g.parentNode.insertBefore(f,g))}(window,document,"script","/hunter/alog/alog.min.js","alog"),void function(){function a(){}window.PDC={mark:function(a,b){alog("speed.set",a,b||+new Date),alog.fire&&alog.fire("mark")},init:function(a){alog("speed.set","options",a)},view_start:a,tti:a,page_ready:a}}();
      void function(n){var o=!1;n.onerror=function(n,e,t,c){var i=!0;return!e&&/^script error/i.test(n)&&(o?i=!1:o=!0),i&&alog("exception.send","exception",{msg:n,js:e,ln:t,col:c}),!1},alog("exception.on","catch",function(n){alog("exception.send","exception",{msg:n.msg,js:n.path,ln:n.ln,method:n.method,flag:"catch"})})}(window);
	}();
!function(){		alog('speed.set', 'ht', +new Date);
	}();
!function(){		var widgetList = ['civilnews', 'InternationalNews',  'EnterNews', 'SportNews', 'FinanceNews', 'TechNews', 'MilitaryNews','InternetNews',   'DiscoveryNews',  'LadyNews', 'HealthNews',   'PicWall'];
		var remainWigetList = $.extend(true, [], widgetList);
		var widgetStatus = (function () {
			var list = {};
			for (var i in widgetList) {
				list[widgetList[i]] = false;

				// 是否渲染的标志
				list[widgetList[i]+'rendered'] = false;
			}
			return list;
		})();

		var widgetRenderFlag = [];


		var appendWidget = function (widgetName, widgetDom) {
			// 保证栏目按widgetList的顺序append到#body上
			// 渲染逻辑重构2018-04-09
			if(widgetStatus[widgetName+'rendered']){
				return false
			}else{
				var dom = $('<div>'+widgetDom+'</div>').addClass(widgetName);
				if(widgetRenderFlag.length != 0){
					$(widgetList).each(function(idx,ele){
						if(ele === widgetName){
							if(widgetRenderFlag.length == 1){
								if(idx > widgetRenderFlag[0].originIndex){
									$('.'+widgetRenderFlag[0].name).after(dom)
									widgetRenderFlag.push({
										name:widgetName,
										originIndex:idx
									})
								}else{
									$('.'+widgetRenderFlag[0].name).before(dom)
									widgetRenderFlag.unshift({
										name:widgetName,
										originIndex:idx
									})
								}
							}else{
								var wrflast = widgetRenderFlag[widgetRenderFlag.length - 1];
								var wrfirst = widgetRenderFlag[0];

								if(idx > wrflast.originIndex){
									$('.'+wrflast.name).after(dom);
									widgetRenderFlag.push({
										name:widgetName,
										originIndex:idx
									});
								} else if(idx < wrfirst.originIndex){
									$('.'+wrfirst.name).before(dom);
									widgetRenderFlag.unshift({
										name:widgetName,
										originIndex:idx
									});

								} else {

									$(widgetRenderFlag).each(function(idx1,ele1){
										if(idx > ele1.originIndex && idx < widgetRenderFlag[idx1 + 1].originIndex){
											// 数组插入
											$('.'+widgetRenderFlag[idx1].name).after(dom)
											widgetRenderFlag.splice(idx1+1,0,{
												name:widgetName,
												originIndex:idx
											})

											return false;
											
										}								
									})
								}
							}

							
						}
						
					})
					
				}else{
					$(body).append(dom);
					$(widgetList).each(function(idx,ele){
						if(ele === widgetName){
							widgetRenderFlag.push({
								name:widgetName,
								originIndex:idx
							});
						}
					})
				}
				
				widgetStatus[widgetName+'rendered'] = true;
				
					
			}	
		}

		var renderWidget = function (widgetName) {
			$.ajax({
				url: '/widget',
				type: 'GET',
				dataType: 'html',
				data: {
					id: widgetName,
					/*ajax: 'json',*/
					// 时间戳，防止ie6缓存ajax请求导致第二次不请求数据
					t: new Date().getTime()
				},
				timeout: 5000
			}).done(function (data) {
					appendWidget(widgetName, data);
			});
		}
		var getLoadingWidgetName = function () {
			return remainWigetList.shift();
		}
		var isChrome = navigator.userAgent.indexOf("Chrome") > -1;
		var isSafari = navigator.userAgent.indexOf("Safari") > -1;
		window.onscroll = function () {
			var body = $('body');
			var height = body.height();
			var scrollTop = get_scrollTop();
			
			if (scrollTop > 1) {
				widgetName = getLoadingWidgetName();

				if (widgetStatus[widgetName] === false) {
					widgetStatus[widgetName] = true;
					renderWidget(widgetName);
				}
			}
		}
		function get_scrollTop() {
                    var scrollTop;
                    if (typeof window.pageYOffset != 'undefined') { //pageYOffset指的是滚动条顶部到网页顶部的距离
                        scrollTop = window.pageYOffset;
                    } else if (typeof document.compatMode != 'undefined' && document.compatMode != 'BackCompat') {
                        scrollTop = document.documentElement.scrollTop;
                    } else if (typeof document.body != 'undefined') {
                        scrollTop = document.body.scrollTop;
                    }
                    return scrollTop;
                }
	}();
!function(){		$(function () {
			$.ajax({
				url: '/passport',
				type: 'GET',
				dataType: 'json',
				timeout: 5000
			}).done(function (data) {
				var userName = '';
				var isLogin = false;
				if(data.errno ===0 && data.data && data.data.displayname) {
					isLogin = true;
					userName = data.data.displayname;
				}
				window['isLogin'] = isLogin;
				require.async("common:widget/ui/vs/enterState/enterState.js", function (enterState) {
					enterState(userName, "")
				});
			});
		})
	}();
!function(){	window.onbeforeunload = function(e){
		window.scrollTo(0,0);
	}
	}();
!function(){    require.async('news:widget/events/events.js', function (event) {
        event.init();
    });
}();
!function(){    require.async(['common:widget/header/header.js'],
        function (mod) {
            mod.init();
        }
    );
}();
!function(){	require.async('common:widget/show_top_qrcode/show_top_qrcode.js', function(showqrcode) {
		showqrcode.init();
	});
}();
!function(){    require.async(["common:widget/lib/tangram/base/base.js", "common:widget/searchbox/searchbox.js", "common:widget/ui/vs/suggestion/suggestion.js"], function(baidu,searchbox,suggestion){
        baidu.dom.ready(function(){
            searchbox.searchbox();
            searchbox.searchnews();
            if (navigator.cookieEnabled && !/sug?=0/.test(document.cookie)){
                    suggestion();
            }
        });
    });
}();
!function(){    require.async(['common:widget/searchbox/searchradio.js', 'common:widget/searchbox/searchboxActive.js'], function(searchRadio, searchboxActive) {
        searchRadio();
        searchboxActive();
    });
}();
!function(){require.async(['common:widget/navbar/navbar.js'],
function (mod) {
mod.init();
}
);
}();
!function(){    require.async(['common:widget/ui/jquery/jquery.js', 'news:widget/TopBanner/TopBanner.js'], function($, module){
        $(function(){
			module.loadTopAD();
        });
    });
}();
!function(){		var extraInfo = {
			m: 11,
			c: 'top'
		};
		require.async('common:widget/ui/vs/clickMonitor/clickMonitor.js', function(clickMonitor){
		    clickMonitor.init('TOP');
		});
	    require.async(['common:widget/lib/tangram/base/base.js', 'common:widget/ui/vs/delayload/delayload.js'],function(baidu,delayload){
	      baidu.dom.ready(function(){
	        //图片延迟加载
	        var delay=new delayload();

	        delay.init();
	        delay.delayLoader(1);
	        delay.bindUI();
	      });
	    });

		var PAGE_DATA = {
		    "guess_list_num": 0,
		    "guess_jsonp_status" : true
		};
	}();
!function(){        require.async('news:widget/mod_headline_tab/mod_headline_tab.js', function (Tab) {
            $(function () {
                var tab = new Tab(0);
                tab.init();
            });
        });
    }();
!function(){  require.async(["common:widget/lib/tangram/base/base.js", "common:widget/ui/vs/ContentPlayer/ContentPlayer.js"], function(T, I) {
    var G = T.dom.g;
    var on = T.event.on;
    var imgList = [];
    var cpOptions_1 = {
      getBtns: function(){
        var a, btns;
            btns = G('imgNav').getElementsByTagName('a');
            a = [];
            for(var i=btns.length - 1; i>=0; i--){
                a.push(btns[i]);
            }
            return a;
      },
      mainViewContainer: G('imgView'),
      prevBtn: G('imgplayer-prev'),
      nextBtn: G('imgplayer-next'),
      changeAction: 'mouseover',
      subViewContainer: G('imgTitle'),
      style: {on: 'active', off: ''},
      mainViewTpl: '<a href="#{url}" target="_blank" mon="c=top&a=12&col=4&pn=#{index}"><img src="#{imgUrl}"></a>',
      subViewTpl: '<a href="#{url}" target="_blank" mon="col=4&a=9&ct=1&pn=#{index}"><strong>#{title}</strong>#{abs}</a>',
      curIndex: 0,
      data: [],
      interval: 5000
    };
  
                          cpOptions_1.data.push({
          "index": 1,
          //"title": "巨幅壁画亮相台北西门町 关注独居弱势老人",
          "title": "巨幅壁画亮相台北西门町 关注独居弱势老人",
          "url": "https:\/\/3w.huanqiu.com\/a\/58ef16\/9CaKrnQhXOb?agt=8",
          "imgUrl": "https:\/\/imgsa.baidu.com\/news\/q%3D100\/sign=60543cb8c11b9d168cc79e61c3dfb4eb\/6609c93d70cf3bc789af638bde00baa1cd112a2d.jpg",
          "abs": "",
          "meadia": ""
        });
        imgList.push({"url":"https:\/\/3w.huanqiu.com\/a\/58ef16\/9CaKrnQhXOb?agt=8"});
                                cpOptions_1.data.push({
          "index": 2,
          //"title": "探访鄂伦春族猎民乡：猎民必需品变成旅游工艺品",
          "title": "探访鄂伦春族猎民乡：猎民必需品变成旅游工艺品",
          "url": "https:\/\/3w.huanqiu.com\/a\/3458fa\/9CaKrnQhXOr?agt=8",
          "imgUrl": "https:\/\/imgsa.baidu.com\/news\/q%3D100\/sign=dc0b3f95721ed21b7fc92ae59d6fddae\/8b82b9014a90f603281232203612b31bb051ed33.jpg",
          "abs": "",
          "meadia": ""
        });
        imgList.push({"url":"https:\/\/3w.huanqiu.com\/a\/3458fa\/9CaKrnQhXOr?agt=8"});
                                cpOptions_1.data.push({
          "index": 3,
          //"title": "霓虹灯下的莲花卫士——记驻澳门部队某装甲步兵连",
          "title": "霓虹灯下的莲花卫士——记驻澳门部队某装甲步兵连",
          "url": "https:\/\/3w.huanqiu.com\/a\/3458fa\/9CaKrnQhXOn?agt=8",
          "imgUrl": "https:\/\/imgsa.baidu.com\/news\/q%3D100\/sign=b8afaeade9cd7b89ef6c3e833f254291\/8601a18b87d6277ff2879c5f27381f30e824fcc4.jpg",
          "abs": "",
          "meadia": ""
        });
        imgList.push({"url":"https:\/\/3w.huanqiu.com\/a\/3458fa\/9CaKrnQhXOn?agt=8"});
                                cpOptions_1.data.push({
          "index": 4,
          //"title": "埃及中文导游的“小确幸”",
          "title": "埃及中文导游的“小确幸”",
          "url": "https:\/\/3w.huanqiu.com\/a\/3458fa\/9CaKrnQhXOo?agt=8",
          "imgUrl": "https:\/\/imgsa.baidu.com\/news\/q%3D100\/sign=b6a7828fb33eb13542c7b3bb961fa8cb\/d1160924ab18972be2aaaeade9cd7b899f510ac0.jpg",
          "abs": "",
          "meadia": ""
        });
        imgList.push({"url":"https:\/\/3w.huanqiu.com\/a\/3458fa\/9CaKrnQhXOo?agt=8"});
                                cpOptions_1.data.push({
          "index": 5,
          //"title": "澳门轻轨举行通车仪式",
          "title": "澳门轻轨举行通车仪式",
          "url": "http:\/\/pic.people.com.cn\/n1\/2019\/1211\/c1016-31500444.html",
          "imgUrl": "https:\/\/imgsa.baidu.com\/news\/q%3D100\/sign=f115ca199d58d109c2e3adb2e159ccd0\/0ff41bd5ad6eddc47d9b1d9c36dbb6fd5266335c.jpg",
          "abs": "",
          "meadia": ""
        });
        imgList.push({"url":"http:\/\/pic.people.com.cn\/n1\/2019\/1211\/c1016-31500444.html"});
                                cpOptions_1.data.push({
          "index": 6,
          //"title": "法国遭遇新一轮响应大罢工的示威游行",
          "title": "法国遭遇新一轮响应大罢工的示威游行",
          "url": "http:\/\/www.chinanews.com\/tp\/hd2011\/2019\/12-11\/917847.shtml",
          "imgUrl": "https:\/\/imgsa.baidu.com\/news\/q%3D100\/sign=aa6b0e12d988d43ff6a995f24d1fd2aa\/42a98226cffc1e17dcea25564590f603738de904.jpg",
          "abs": "",
          "meadia": ""
        });
        imgList.push({"url":"http:\/\/www.chinanews.com\/tp\/hd2011\/2019\/12-11\/917847.shtml"});
                                cpOptions_1.data.push({
          "index": 7,
          //"title": "“中华名楼”黄鹤楼重现宋清时期被毁“前身”",
          "title": "“中华名楼”黄鹤楼重现宋清时期被毁“前身”",
          "url": "http:\/\/www.chinanews.com\/tp\/hd2011\/2019\/12-11\/917844.shtml",
          "imgUrl": "https:\/\/imgsa.baidu.com\/news\/q%3D100\/sign=38b3a545bc1bb0518924b728067bda77\/4e4a20a4462309f7019604757d0e0cf3d6cad6d8.jpg",
          "abs": "",
          "meadia": ""
        });
        imgList.push({"url":"http:\/\/www.chinanews.com\/tp\/hd2011\/2019\/12-11\/917844.shtml"});
                                cpOptions_1.data.push({
          "index": 8,
          //"title": "这座博物馆里全是土！探访贵州“土壤档案馆”",
          "title": "这座博物馆里全是土！探访贵州“土壤档案馆”",
          "url": "http:\/\/www.chinanews.com\/tp\/hd2011\/2019\/12-10\/917777.shtml",
          "imgUrl": "https:\/\/imgsa.baidu.com\/news\/q%3D100\/sign=bbc9dd4e8918367aab897bdd1e728b68\/08f790529822720e076bf29d74cb0a46f21fab2b.jpg",
          "abs": "",
          "meadia": ""
        });
        imgList.push({"url":"http:\/\/www.chinanews.com\/tp\/hd2011\/2019\/12-10\/917777.shtml"});
            
    var index = 0 ;
    var url = location.href.substr(location.href.indexOf("?")+1).split("&");
    var key ;
    for(var i = 0 ; i < url.length ; i++){
       var tmp = url[i].split("=");
       if(tmp&&tmp.length>0&&tmp[0]=="lb"){
           key = tmp[1];
       }
    }
    for(var p in imgList){
       if(imgList[p].url == key){
           index = p ;
       }
    }
    cpOptions_1.curIndex = index;
    var cp_1 = new I.Model(cpOptions_1);

    on(window, 'load', function(){
       cp_1.play(index+1);
    });

    var controlers = baidu.dom.query('#imgNav a');
    baidu.each(controlers, function(item,i){
        baidu.on(item,'mouseover',function(e){
            UserMonitor.send(e, 6, {c: "top", a:"51", col: "4", ct: "1", m: "11", pn: 8-i});
            window.alog && alog("monkey.fire", "record", {
                type: "click",
                target: item
            });
        });
    });
  });
}();
!function(){
    /*var ___lis___ = $(".hotwords li"),___images___ = $('.hotwords img'),___words___=$('.hotwords_li_a');
    $.each(___images___,function(i,item){
        var $item = $(item),
        src = $item.attr('m_m_src'),
        _img = new Image();
        _img.onload = function(){

            $item.attr('src', src);
            if(_img.width > _img.height){
                if($item.parents('li').width() > 68){
                    $item.css('width', '139px');
                }else{
                    $item.css('height', '68px');

                }
            }else{
                $item.css('width',$item.parents('li').width());
            }
            _img.onload = null;
        }
        _img.src = src;
    });
    $.each(___lis___,function(i,item){
        $(item).mouseenter(function(e){
        $('.detail',this).animate({top:'0px'},200,function(){});

        });
        $(item).mouseleave(function(e){
        $('.detail',this).animate({top:'68px'},200,function(){});
        });
    });
    $.each(___words___, function(i, item) {
        $(item).find('img').length == 0 && $(item).css({"padding-top": (68 - item.offsetHeight)/2 + "px"}) || $(item).css({"padding": 0, 'width':$(item).width()+9+'px'});
        $(item).css({
            "visibility": "visible"
        });
    });*/



    require.async('news:widget/hotwords/hotwords.js', function (mod) {
        mod.init();
    });

}();
!function(){    require.async('news:widget/mod_baijia/mod_baijia.js', function(tab){
       var tab =  new tab({
            container : 'nba-tab',
            event : 'mouseover'
       }).setup();
    });
}();
!function(){	    void function(e,t){for(var n=t.getElementsByTagName("img"),a=+new Date,i=[],o=function(){this.removeEventListener&&this.removeEventListener("load",o,!1),i.push({img:this,time:+new Date})},s=0;s<n.length;s++)!function(){var e=n[s];e.addEventListener?!e.complete&&e.addEventListener("load",o,!1):e.attachEvent&&e.attachEvent("onreadystatechange",function(){"complete"==e.readyState&&o.call(e,o)})}();alog("speed.set",{fsItems:i,fs:a})}(window,document);
	}();
!function(){    require.async('news:widget/LocalNews/LocalNews.js', function(initLocalHotNews){

        //地方新闻和各地房产新闻共享LocalNewsConfig配置
        window.LocalNewsConfig = {
            cookieName: 'LOCALGX',
            cookieDomain: 'news.baidu.com',
            defaultFailedLocalCity: '北京',
            defaultLocalCityID:0,
            defaultHouseCity: '北京',
            defaultFailedHouseCity: '各地',
            htmlTpl: {
                more_link: '',
                more_link_sh: '<a target="_blank" href="/sh" id="more-link" style="visibility: visible;"></a> ',
                city_list: '<a href="javascript:void(0);" mon="col=10&locname=#{city_name}&locid=#{locID}" prop="#{prop}">#{title}</a> ',
                city_name_link: '<b>#{city_name}</b>新闻',
                city_name_link_sh: '<a href="/sh" target="_blank" class="#{class_name}"><b>#{city_name}</b>新闻</a>',
                city_name_no_link: '<b>#{city_name}</b>新闻',
                local_news: '<li><span class="num num-#{index}">#{index_pad}</span><a href="#{url}" mon="c=civilnews&ct=0&a=27&col=8&locname=#{city_name}&locid=#{locID}" target="_blank">#{title}</a></li>',
                //local_news_sh: '<li><span class="num num-#{index}">#{index_pad}</span><a href="/sh" mon="c=civilnews&ct=0&a=27&col=8&locname=#{city_name}&locid=#{locID}" target="_blank">#{title}</a></li>',
                house_news: '<li><span class="num num-#{index}">#{index_pad}</span><a href="#{url}" mon="c=housenews&ct=0&a=27&col=9" target="_blank">#{title}</a></li>',
                local_news_top : '<li class="top-localnews"><h4><a href="#{url}" mon="c=civilnews&ct=0&a=27&col=8&locname=#{city_name}&locid=#{locID}" target="_blank">#{title}</a></h4><p><a href="#{url}" mon="c=civilnews&ct=0&a=27&col=8&locname=#{city_name}&locid=#{locID}" target="_blank"><img src="#{imgUrl}"></a>#{abs}</p></li>',
                local_news_top_noimg : '<li class="top-localnews" style="height:80px"><h4><a href="#{url}" mon="c=civilnews&ct=0&a=27&col=8&locname=#{city_name}&locid=#{locID}" target="_blank">#{title}</a></h4><p>#{abs}</p></li>',
                focus : '<li><a href="#{url}" mon="c=civilnews&ct=0&a=27&col=8&locname=#{city_name}&locid=#{locID}" target="_blank">#{title}</a></li>',
                focus_bold : '<li class="bold-item"><span class="dot"></span><a href="#{url}" mon="c=civilnews&ct=0&a=27&col=8&locname=#{city_name}&locid=#{locID}" target="_blank">#{title}</a></li>',
                pic : '<div class="image-mask-item"><a href="#{url}" target="_blank" class="item-image" mon="c=civilnews&ct=0&a=27&col=8&locname=#{city_name}&locid=#{locID}"><img src="#{imgUrl}"/></a><a href="#{url}" target="_blank" class="item-title" mon="">#{title}</a></div>',
                other : '<li><a href="#{url}" mon="c=civilnews&ct=0&a=27&col=8&locname=#{city_name}&locid=#{locID}" target="_blank">#{title}</a></li>'
            },
            timeout: 5000
        }
        initLocalHotNews({
            pageType: 'TOP',
            request: {
                url: '/n?m=rddata&v=index_data&rn1=17',
                callback : 'bdNewsJsonCallBack'
            },
            //data: city.localCities,
            triggerLevel: 2,
            statusID: 'status',
            cityNameID: 'city_name',
            logoID: 'localnews_logo',
            pmoreLinkID: 'p-more-link',
            moreLinkID: 'more-link',
            cityViewID: 'city_view',
            changeCityID: 'change-city',
            closeBtnID: 'btn_close',
            backBtnID: 'btn_back',
            localNewsID:{
                focus : 'localnews-focus',
                pic : 'localnews-pic',
                other :'localnews-zixun',
                ad:'localNews_ad'
            },
            maxItemsShown: 10,
            timeout: LocalNewsConfig.timeout
        });
    });
}();
!function(){require.async(['common:widget/sidebar/sidebar.js'],
    function (Sidebar) {
        $(function () {
            var sidebar = new Sidebar();
            sidebar.init();
        });
    }
);
}();
!function(){    require.async(['common:widget/footer/statistics.js'], function (mod) {
        // 页面加载后，向biglog发送一个pv统计，传入hostname区分产品和频道
        mod.postReferToBiglog();
        // 页面加载后，初始化发送往百度统计的打点
        mod.initClickPostToTongji();
        // 页面加载后，向百度统计发送页面的refer
        mod.postReferToTongji();
    });
}();
!function(){   	document.write("<img src='/nocache/mp/b.jpg?cmd=1&class=technnews&cy=0&"+Math.random()+"' style='display:none;'>");
     <!-- document.write("<img id='cgif' src='http://ccccccc.baidu.com/c.gif?t=5&p=2&"+Math.random()+"' style='display:none'>"); -->
   58  }();
!function(){	var _bdhmProtocol = (("https:" == document.location.protocol) ? " https://" : " http://");
	document.write(unescape("%3Cscript src='" + _bdhmProtocol + "hm.baidu.com/h.js%3Fe9e114d958ea263de46e080563e254c4' type='text/javascript'%3E%3C/script%3E"));
}();
!function(){	require.async('common:widget/lib/tangram/base/base.js',function(baidu){
	    baidu.each(baidu.dom.query('img'),function(item){	
	        if(/eiv.baidu.com\/hmt\/icon/.test(baidu.dom.getAttr(item, 'src'))){
	            item.style.display = 'none';		
	        }
	    });
	});
}();
!function(){    require.async(['common:widget/hunter/hunter.js'],
        function (mod) {
            if (location.search.indexOf('hunterrandom=0') >= 0) {
                // url的search中有 hunterrandom=0 则忽略限流
                mod.init(73791);
            } else if (parseInt(Math.random().toString().slice(2)) % 10 === 0) {
                // 限制流量，只传10%的统计量
                mod.init(73791);
            }
        }
    );
}();
!function(){        $(function() {
            alog('speed.set', 'drt', +new Date);
        });

        window.alogObjectConfig = {
            product: '107',
            page: 'newspc_107',

            // 性能
            speed: {
                sample: '0.15'
            },

            // js异常
            exception: {
                sample: '0.08'
            },

            // 新特性
            feature: {
                sample: '0.08'
            },

            csp: {
                sample: '0.15',
                'default-src': [
                    {match: '*bae.baidu.com', target: 'Accept,Warn'},
                    {match: '*.baidu.com,*.bdstatic.com,*.bdimg.com,localhost,*.hao123.com,*.hao123img.com', target: 'Accept'},
                    {match: /^(127|172|192|10)(\.\d+){3}$/, target: 'Accept'},
                    {match: '*', target: 'Accept,Warn'}
                ]
            }
        };
				void function(a,b,c,d,e,f){function g(b){a.attachEvent?a.attachEvent("onload",b,!1):a.addEventListener&&a.addEventListener("load",b)}function h(a,c,d){d=d||15;var e=new Date;e.setTime((new Date).getTime()+1e3*d),b.cookie=a+"="+escape(c)+";path=/;expires="+e.toGMTString()}function i(a){var c=b.cookie.match(new RegExp("(^| )"+a+"=([^;]*)(;|$)"));return null!=c?unescape(c[2]):null}function j(){var a=i("PMS_JT");if(a){h("PMS_JT","",-1);try{a=a.match(/{["']s["']:(\d+),["']r["']:["']([\s\S]+)["']}/),a=a&&a[1]&&a[2]?{s:parseInt(a[1]),r:a[2]}:{}}catch(c){a={}}a.r&&b.referrer.replace(/#.*/,"")!=a.r||alog("speed.set","wt",a.s)}}if(a.alogObjectConfig){var k=a.alogObjectConfig.sample,l=a.alogObjectConfig.rand;d="https:"===a.location.protocol?"https://fex.bdstatic.com"+d:"http://fex.bdstatic.com"+d,k&&l&&l>k||(g(function(){alog("speed.set","lt",+new Date),e=b.createElement(c),e.async=!0,e.src=d+"?v="+~(new Date/864e5)+~(new Date/864e5),f=b.getElementsByTagName(c)[0],f.parentNode.insertBefore(e,f)}),j())}}(window,document,"script","/hunter/alog/dp.min.js");
    }();
!function(){        $.ready(function() {
            alog('speed.set', 'drt', +new Date);
        });
    }();</script></html>
"""


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9102, debug=True)
