# Kungfu_Panda_AppStore
[GO! Kungfu Panda!] AppStore Project

Description
-----------

Application store is very popular in both Android ecosystem and iOS ecosystem. It is the most important channel for billions of users to find and download applications. Huge downloads stand for diversified software demands. That means an App store should have as much software as possible. App crawler is one of methods to collect applications and expend App Store.

Inspired by [Project App Store Crawler](https://slack-files.com/T0GUEMKEZ-F0J4G9QTT-274d3bc97e), AppStore project aims to develop a crawler to crawl 1 million Android application information from [Huawei App Store](http://appstore.huawei.com). 

If time and ability allow, there are some additional functions:
1. Find the most relevant Apps
2. Download Ranking
3. Recommender
4. Malicious review detector
5. Malicious user detector

Specification
-------------

Performance: 100 pages/second 

Plan
----

Based on our experiences on web development and descriptions metioned above, we take _Feb, 2016_ as the __1st stage__ with the __primary__ goal of __prototyping__ our own chat application following the [Development Guildlines](https://github.com/BitTigerNY/AraChat/edit/master/README.md#Development Guildlines) metioned below. Here're some tentative schedules.

* __[2016/02/01 - 2016/02/07]__ Project Selection, Plan Discussion, and Proposal Draft Writing
* __[2016/02/08 - 2016/02/24]__ System Design, Resource Discovery, Project Implementation, Document Writing 
* __[2016/02/25 - 2016/02/29]__ User Manual Writing and Video Presentation Making

_Details of each schedule and task will be added later._

Resource
--------

1. __[BitTiger Project: AppStore - Crawler]__ https://www.youtube.com/watch?v=hJuw1Wbn0PM
2. __[PPT of introduction of AppStore]__ https://www.dropbox.com/s/bja7rfnm42vwtkj/20151222AppStore%20Introduction.pdf?dl=0
3. __[Video of crawler]__ https://www.dropbox.com/s/ncgxsqkb1w8sgxr/20151223AppStore%20Crawler.mov?dl=0
4. __[PPT for crawler]__ https://www.dropbox.com/s/tpf07ir8mwedu1y/20151223AppStore%20Crawler.pdf?dl=0
5. __[Video of crawler homework]__ https://www.youtube.com/watch?v=JxCTk3Iz63w
6. __[PPT for crawler homework]__ https://www.dropbox.com/s/0ojejis71ebds3s/20160103_Appstore%20CrawlerAdvanced.pdf?dl=0
7. __[Video for crawl more pages]__ https://www.youtube.com/watch?v=qVGU1Nx_jYA
8. __[PPT for crawl more pages]__ https://www.dropbox.com/s/qzfin9zbmzevqcj/20160109_AppStore-Crawl%20More%20Apps.pdf?dl=0

Language & Framework
--------------------

+ Python, Scrapy, MongoDB, Proxy, Scrapyjs

Development Guildlines
----------------------

- __Modularity.__ Following the principle _"loose coupling and high cohesion"_, each module should be standalone.

- __Minimalism.__ Each module should be kept short, simple, and concise. Every piece of code should be transparent upon first reading. 
- __Easy extensibility.__ New modules (as new classes and functions) are should be simply add, and existing modules should be extended easily.

Owner
-----

@team: Gungfu_Panda
