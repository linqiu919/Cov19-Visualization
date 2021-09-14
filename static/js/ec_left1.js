var ec_left1 = echarts.init(document.getElementById("l1"),"#F5F5F5");

var ec_left1_Option = {
	//标题样式
	title: {
		text: "全国累计趋势",
		textStyle: {
			 color : '#000000',
		},
		left: 'left',
	},
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
		data: ['累计确诊', '现有疑似', "累计治愈", "累计死亡"],
		left: "right",
		top: '4%',
	},

	//图形位置
	grid: {
		left: '3%',
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
		data: []//['01.20', '01.21', '01.22']
	}],
	yAxis: [{
		type: 'value',
		//y轴字体设置
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
		//y轴线设置显示
		axisLine: {
			show: true
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
	series: [{
		name: "累计确诊",
		type: 'line',
		smooth: true,
		data: [] //传入数据
	}, {
		name: "现有疑似",
		type: 'line',
		smooth: true,
		data: []//[54, 37, 3935]
	},
		{
		name: "累计治愈",
		type: 'line',
		smooth: true,
		data: []//[25, 25, 25]
	}, {
		name: "累计死亡",
		type: 'line',
		smooth: true,
		data: []//[6, 9, 17]
	}]
};

ec_left1.setOption(ec_left1_Option)
