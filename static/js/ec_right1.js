var ec_right1 = echarts.init(document.getElementById('r1'),"#F5F5F5");
var ec_right1_option = {
	//标题样式
	title : {
	    text : "昨日新增确诊病例前五城市",
	    textStyle : {
	        color : '#000000',
	    },
	    left : 'left'
	},
	  color: ['#3398DB'],
	    tooltip: {
	        trigger: 'axis',
	        axisPointer: {            // 坐标轴指示器，坐标轴触发有效
	            type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
	        }
	    },
    xAxis: {
        type: 'category',
        data: [],
		axisLabel: {
        show: true,
        textStyle: {
          color: '#000000',  //更改坐标轴文字颜色
          fontSize : 16      //更改坐标轴文字大小
        }
     },
    },
    yAxis: {
        type: 'value',
		axisLabel: {
        show: true,
        textStyle: {
          color: '#000000',  //更改坐标轴文字颜色
          fontSize : 16      //更改坐标轴文字大小
        }
     },
		// max : 15,
		// splitNumber : 5,

    },
    series: [{
        data: [],
		 name: '新增病例',
        type: 'bar',
		barMaxWidth:"50%",

    }]
};
ec_right1.setOption(ec_right1_option)