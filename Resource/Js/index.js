var RpiUrl = "http://192.168.50.5:8899/car" //树莓派地址

$(document).ready(function(){
    //监听body事件，mousedown touchstart当鼠标点击时。
    $("#forward").bind('mousedown touchstart', function(e) {
            e.preventDefault();
            $.ajax({
                    type: "GET", //调用ajax方法发送GET请求
                    url: RpiUrl, //此为树莓派URL变量
                    data: {"a": 1}, //传入参数，参数1为前进，参数2为后退，参数3为左转，参数4为右转，参数0为停车
                    dataType: "json", //传入json
                    cache: "false", //关闭缓存
                    success: function(data){},
                    error: function(data){}
            });
    });
    //以下无可奉告
    $("#back").bind('mousedown touchstart', function(e) {
            e.preventDefault();
            $.ajax({
                    type: "GET",
                    url: RpiUrl,
                    data: {"a": 2},
                    dataType: "json",
                    cache: "false",
                    success: function(data){},
                    error: function(data){}
            });
    });
    $("#front_left_turn").bind('mousedown touchstart', function(e) {
            e.preventDefault();
            $.ajax({
                    type: "GET",
                    url: RpiUrl,
                    data: {"a": 3},
                    dataType: "json",
                    cache: "false",
                    success: function(data){},
                    error: function(data){}
            });
    });
    $("#front_right_turn").bind('mousedown touchstart', function(e) {
            e.preventDefault();
            $.ajax({
                    type: "GET",
                    url: RpiUrl,
                    data: {"a": 4},
                    dataType: "json",
                    cache: "false",
                    success: function(data){},
                    error: function(data){}
            });
    });
    $("#forward").bind('mouseup touchend', function() {
            $.ajax({
                    type: "GET",
                    url: RpiUrl,
                    data: {"a": 0},
                    dataType: "json",
                    cache: "false",
                    success: function(data){},
                    error: function(data){}
            });
    });
    $("#back").bind('mouseup touchend', function() {
            $.ajax({
                    type: "GET",
                    url: RpiUrl,
                    data: {"a": 0},
                    dataType: "json",
                    cache: "false",
                    success: function(data){},
                    error: function(data){}
            });
    });
    $("#front_left_turn").bind('mouseup touchend', function() {
            $.ajax({
                    type: "GET",
                    url: RpiUrl,
                    data: {"a": 0},
                    dataType: "json",
                    cache: "false",
                    success: function(data){},
                    error: function(data){}
            });
    });
    $("#front_right_turn").bind('mouseup touchend', function() {
            $.ajax({
                    type: "GET",
                    url: RpiUrl,
                    data: {"a": 0},
                    dataType: "json",
                    cache: "false",
                    success: function(data){},
                    error: function(data){}
            });
    });
});