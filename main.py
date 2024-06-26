import feedparser, time

URL="https://yjhdevelopdiary.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST=7

markdown_text = """
<img src="https://capsule-render.vercel.app/api?type=waving&color=BDBDC8&height=150&section=header" />
<div align=center>
 
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FYujinhyeonWilliam%2F&count_bg=%23EF9605&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
  
</div>

### Thanks For Coming

- ⚡ Former Unity Game Developer (2yrs)

![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=YujinhyeonWilliam&layout=compact&theme=vision-friendly-dark)

<br/>

## 📚 Currently Studying
<img src="https://img.shields.io/badge/C++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white"> <img src="https://img.shields.io/badge/Unreal-%23313131.svg?style=for-the-badge&logo=unrealengine&logoColor=white"> <img src="https://img.shields.io/badge/AWS-2B283A.svg?style=for-the-badge&logo=amazon-aws&logoColor=white"> 

<br/>

## 🔧 Skills Available
#### [Main]
<img src="https://img.shields.io/badge/c%23-%23239120.svg?style=for-the-badge&logo=csharp&logoColor=white"> <img src="https://img.shields.io/badge/Unity-%23000000.svg?style=for-the-badge&logo=unity&logoColor=white">

#### [Sub]
<img src="https://img.shields.io/badge/firebase-a08021?style=for-the-badge&logo=firebase&logoColor=ffcd34"> <img src="https://img.shields.io/badge/BigQuery-005571?style=for-the-badge&logo=googlebigquery"> <img src="https://img.shields.io/badge/Google Analytics-414141?style=for-the-badge&logo=googleanalytics"> 

<br/>

## ✍ Recent Blog Posts
<div style="display:flex; flex-direction:row;">
    <a href="https://yjhdevelopdiary.tistory.com/">
        <img src="https://img.shields.io/badge/Tistory-000000?style=for-the-badge&logo=Tistory&logoColor=white"> 
    </a> <br/>

""" # list of blog posts will be appended here


for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"
     
markdown_text += """<img src="https://capsule-render.vercel.app/api?type=waving&color=BDBDC8&height=150&section=footer" />"""

f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()


