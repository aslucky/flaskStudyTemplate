(function ($) {
    $.fn.form2Json = function () {
        var o = {};
        var a = this.serializeArray();
        $.each(a, function () {
            if (o[this.name]) {
                if (!o[this.name].push) {
                    o[this.name] = [o[this.name]];
                }
                o[this.name].push(this.value || '');
            } else {
                o[this.name] = this.value || '';
            }
        });
        return JSON.stringify(o);
    };
})(jQuery);

$(document).ready(function () {

    // 添加自定义的验证函数，例如 notBlank 和 telephone 这 2 个验证规则默认是没有得，可以使用下面的方式自行添加
    // 不能为空字符串
    $.validator.addMethod('notBlank', function (value, element) {
        return $.trim(value);
    });

    // 长度大于6即可
    jQuery.validator.addMethod("isPwd", function (value, element) {
        var str = value;
        if (str.length < 6)
            return false;
        else
            return true;
    });

    $('#loginForm').validate({
        // 验证规则
        rules: {
            username: {
                required: true,
                notBlank: true
            },
            password: {
                isPwd: true
            }
        },
        // 错误提示信息，和验证规则一一对应，如果不写，就会使用默认的错误提示信息
        messages: {
            username: {
                required: '姓名不能为空',
                notBlank: '姓名不能为空格'
            },
            password: {
                required: '密码不能为空',
                notBlank: '密码不能为空格',
                isPwd: '最少6个字符'
            }
        },
         errorElement: "em",
        errorPlacement: function (error, element) {
            // Add the `help-block` class to the error element
            error.addClass("help-block");

            if (element.prop("type") === "checkbox") {
                error.insertAfter(element.parent("label"));
            } else {
                error.insertAfter(element);
            }
        },
        highlight: function (element, errorClass, validClass) {
            $(element).parents(".form-text").addClass("has-error").removeClass("has-success");
        },
        unhighlight: function (element, errorClass, validClass) {
            $(element).parents(".form-text").addClass("has-success").removeClass("has-error");
        },
        // 自定义错误显示的位置，默认是显示在 <input> 的后面，很多时候不符合需求
        // 错误提示信息的 <label> 包裹在 <li> 里然后添加到 <div class="erros"> 中
        // errorContainer: "div.error",
        // errorLabelContainer: $('#error-info div.errors'),
        // wrapper: 'div',
        // showErrors: function (errorMap, errorList) {
        //     // 有错误的时候才显示
        //     if (this.numberOfInvalids() > 0) {
        //         $('#error-info').show();
        //     } else {
        //         $('#error-info').hide();
        //     }
        //     this.defaultShowErrors();
        //
        // },
        submitHandler: function (form) {
            // 点击 '提交' 按钮，验证通过，会调用这个函数，就可以在这里进行 form 表单的提交，例如 Ajax 的方式
            // 也可以不实现这个函数，表单提交时使用表单的默认方式提交
            //callback handler for form submit
            // http://api.jquery.com/jquery.ajax/#jQuery-ajax-settings
            var jsonData = $("#loginForm").form2Json();
            $.ajax(
                {
                    url: "/admin/api/v1.0/login",
                    method: "POST",
                    data: jsonData,
                    dataType: 'json',
                    contentType: "application/json; charset=utf-8",
                    success: function (data, textStatus, jqXHR) {
                        //data: return data from server
                        if (data['code'] == 0) {
                            // login success
                            // get dashboard page
                            window.location.href = "dashboard";
                        } else {
                            alert(data['msg']);
                        }
                        console.log(data, textStatus, jqXHR);
                    },
                    error: function (jqXHR, textStatus, errorThrown) {
                        alert(textStatus + errorThrown);
                        //if fails
                        console.log(jqXHR, textStatus, errorThrown);
                    }
                });

        }
    });



});