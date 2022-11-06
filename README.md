# Cov19-Visualization
开发理念： 监控疫情数据，合理采取措施！

# 目前问题
1. https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5 
   此链接返回的疫情json数据不完整，导致json解析报错。
2. 国内疫情前五统计会出现重名城市【sql处理问题】
3. 前端定时刷新策略不够完备
4. 数据为统一刷新，没有动态化展示直观

# TODO List
1. 修复疫情数据爬取错误问题【可能要换源重写】
2. 前端页面重构【使用vue+elementUI重写页面】
3. 前端图表动态刷新
4. 数据源多源头解析【设计多类数据源解析，有可能需要多套前端页面】



