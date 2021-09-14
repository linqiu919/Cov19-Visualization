var ec_right2 = echarts.init(document.getElementById('r2'), "#F5F5F5");

var data = [];
// var mydata = [{'name': '上海', 'value': 318}, {'name': '云南', 'value': 162}]

var option_left2 = {
    title: {
        text: '昨日新增确诊病例城市比例',
        textStyle: {
            color: '#000000',
        },
        left: 'left'
    },
    tooltip: {
        trigger: 'item'
    },

    series: [
        {
            top:'10%',
            name: '当日新增病例',
            type: 'pie',
            radius: '70%',
            fontSize:'20px',
            data: [],
            "label": {
            "normal": {
                "show": true,
                "textStyle": {
                    "fontSize": 18 }
            },
            "emphasis": {
                "show": true
            }
        },
            emphasis: {
                itemStyle: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            }
        }
    ]
};
ec_right2.setOption(option_left2)