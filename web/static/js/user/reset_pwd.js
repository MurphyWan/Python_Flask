;
//这个js文件是老师已经帮我们写好的，直接用就可以了。其目的是将前台提交的用户昵称和手机号和邮箱传递到后台更新数据库
//定义变量user_edit_ops，里面有2个方法：init和eventBind，和所有其他js一样。
//因为这个文件类似于edit.js，所以复值过来的
//在reset_pwd.html中式哟个id方式save，所以我们这个方法就是用id方式
var mod_pwd_ops = {
    init:function(){
        this.eventBind();
    },
    eventBind:function(){
        $("#save").click(function(){
            var btn_target = $(this);
            if( btn_target.hasClass("disabled") ){
                common_ops.alert("正在处理!!请不要重复提交~~");
                return;
            }
//上面部分是以上的；然后获取我们表单的值
            var old_password = $("#old_password").val();
            var new_password = $("#new_password").val();
            //var nickname = nickname_target.val();
//获取完毕之后就是我们参数有效性的校验部分
            //如果没有原始密码
            if( !old_password ){
                common_ops.alert( "请输入原密码~~" );
                return false;
            }
            //如果没有新密码，且新密码长度小于6
            if( !new_password || new_password < 6 ){
                common_ops.alert( "请输入不少于6位的新密码~~" );
                return false;
            }

            btn_target.addClass("disabled");

            //传递到我们后端去
            var data = {
                old_password: old_password,
                new_password: new_password
            };

            $.ajax({
                url:common_ops.buildUrl( "/user/reset-pwd" ),//方法名是reset-pwd
                type:'POST',
                data:data,
                dataType:'json',
                success:function( res ){
                    btn_target.removeClass("disabled");
                    var callback = null;
                    if( res.code == 200 ){
                        callback = function(){
                            window.location.href = window.location.href;
                        }
                    }
                    common_ops.alert( res.msg,callback );
                }
            });


        });
    }
};

//当我们jquery加载完成的时候，我们执行我们的init方法就可以了。
$(document).ready( function(){
    mod_pwd_ops.init();
} );
//写完这个js文件，回到reset_pwd.html文件，将本js引入进去