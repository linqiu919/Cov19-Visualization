var ec_left2 = echarts.init(document.getElementById("l2"),"#F5F5F5");

var ec_left2_Option = {
	tooltip: {
		trigger: 'axis',
		//指示器
		axisPointer: {
			type: 'line',
			lineStyle: {
				color: '#7171C6'
			}
		},
	},
	legend: {
		data: ['新增确诊', '新增疑似'],
		left: "right",
		top:'3%',
	},
	//标题样式
	title: {
		text: "全国新增趋势",
		textStyle: {
			color : '#000000',
		},
		left: 'left'
	},
	//图形位置
	grid: {
		left: '4%',
		right: '6%',
		bottom: '4%',
		top: 50,
		containLabel: true
	},
	xAxis: [{
		type: 'category',
		axisLabel: {
        show: true,
        textStyle: {
          color: '#000000',  //更改坐标轴文字颜色
          fontSize : 16      //更改坐标轴文字大小
        }
     },
		//x轴坐标点开始与结束点位置都不在最边缘
		boundaryGap : true,

		data: []
	}],
	yAxis: [{
		type: 'value',
		//y轴字体设置

		//y轴线设置显示
		axisLine: {
			show: true
		},
		axisLabel: {
			show: true,
			color: '#000000',
			fontSize: 16,
			formatter: function(value) {
				if (value >= 1000) {
					value = value / 1000 + 'k';
				}
				return value;
			}
		},
		//与x轴平行的线样式
		splitLine: {
			show: true,
			lineStyle: {
				color: '#17273B',
				width: 1,
				type: 'solid',
			}
		}
	}],
	series: [
		{
		name: "新增确诊",
		type: 'line',
		smooth: true,
		data: []
	}, {
		name: "新增疑似",
		type: 'line',
		smooth: true,
		data: []
	}]
};

ec_left2.setOption(ec_left2_Option)