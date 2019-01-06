;
//；，可能会将多个js压缩，所以第一行加上分号，这样语法不会出错
// user_login_ops，是个json对戏那个
var user_login_ops = {
    init:function(){
        this.eventBind();
    },
    //eventBind，事件绑定，就是点击登录按钮的时候，触发事件进行提交
    eventBind:function(){
        $(".login_wrap .do-login").click( function(){

            var btn_target = $(this);

            if( btn_target.hasClass("disabled") ){
                common_ops.alert("正在处理!!请不要重复提交~~");
                return;
            }

            var login_name = $(".login_wrap input[name=login_name]").val();
            var login_pwd = $(".login_wrap input[name=login_pwd]").val();

            if( login_name == undefined || login_name.length < 1){
                common_ops.alert( "请输入正确的登录用户名~~" );
                return;
            }
            if( login_pwd == undefined || login_pwd.length < 1){
                common_ops.alert( "请输入正确的密码~~" );
                return;
            }
            //登录不成功，会disabled登录按钮
            btn_target.addClass("disabled");


            // ajaxtji
            $.ajax({
                url:common_ops.buildUrl("/user/login"),
                type:'POST',
                data:{ 'login_name':login_name,'login_pwd':login_pwd },
                dataType:'json',
                success:function(res){
                    //当登录成，会将登录按钮的disabled去掉
                    btn_target.removeClass("disabled");
                    var callback = null;
                    //如何状态为200，则跳到首页
                    if( res.code == 200 ){
                        callback = function(){
                            window.location.href = common_ops.buildUrl("/");
                        }
                    }
                    common_ops.alert( res.msg,callback );
                }
            });
        } );
    }
};

$(document).ready( function(){
    user_login_ops.init();
} );