# Unnotech Backend Engineer 徵才小專案

1. 抓取 http://tw-nba.udn.com/nba/index 中的焦點新聞。
`crawler.py`
2. 使用 [Django](https://www.djangoproject.com/) 設計恰當的 Model，並將所抓取新聞存儲至 DB。
`Unnotech_HW\nba_news\models.py`
3. 使用 [Django REST Framework](http://www.django-rest-framework.org/) 配合 AJAX 實現以下頁面：
	 * 焦點新聞列表
	`/api/nba/`
	 * 新聞詳情頁面
	`/api/nba-detail`
4. 以 Pull-Request 的方式將代碼提交。
	
## 進階要求
1. 實現爬蟲自動定時抓取。 
```
30 10 * * * /root/nicetomeetyou/.env/python3 /root/nicetomeetyou/crawler.py
```
2. 使用 Websocket 服務，抓取到新的新聞時立即通知前端頁面。
```
# requirement
djangochannelsrestframework
channels
daphne
# api
ws://{domain}/ws/nba/
```
3. 將本 demo 部署到伺服器並可正確運行。
* [https://unno.virgil246.com](https://unno.virgil246.com)
  * Frontend 用Cloudflare Pages部屬
* [https://unno-api.virgil246.com](https://unno-api.virgil246.com)
  * Backend 部屬在自己的機器上
  * 用 daphne + Nginx + Cloudflare Tunnel
4. 所實現新聞列表 API 可承受 100 QPS 的壓力測試。
