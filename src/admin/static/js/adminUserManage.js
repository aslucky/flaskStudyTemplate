$(document).ready(function () {


});

$.extend($.fn.validatebox.defaults.rules, {
    minLength: {
        validator: function (value, param) {
            return value.length >= param[0];
        },
        message: '最少输入 {0} 个字符.'
    }
});

var url;
var submitType;

function newUser() {
    $('#dlg').dialog('open').dialog('center').dialog('setTitle', '新建用户');
    $('#fm').form('clear');
    url = '/admin/api/v1.0/users';
    submitType = 'POST';
}

function editUser() {
    var row = $('#dg').datagrid('getSelected');
    if (row) {
        $('#dlg').dialog('open').dialog('center').dialog('setTitle', 'Edit User');
        $('#fm').form('load', row);
        url = '/admin/api/v1.0/users';
        submitType = 'PUT';
    }
}

function saveUser() {
    var isValid = $('#fm').form('validate');
    if (false == isValid) {
        $.messager.alert({    // show error message
            title: 'Error',
            icon: 'error',
            msg: '表单参数不符合要求',
            showType: 'slide',
            style: {
                right: '',
                top: document.body.scrollTop + document.documentElement.scrollTop,
                bottom: ''
            }
        });
        return;
    }
    var data = $('#fm').serialize();
    $.ajax({
        type: submitType,
        url: url,
        data: data,
        success: function (result) {
            console.log(result);
            if (result.code == 0) {
                $('#dlg').dialog('close');        // close the dialog
                $('#dg').datagrid('reload');    // reload the user data
            } else {
                $.messager.alert({    // show error message
                    title: 'Error',
                    icon: 'error',
                    msg: result.msg,
                    showType: 'slide',
                    style: {
                        right: '',
                        top: document.body.scrollTop + document.documentElement.scrollTop,
                        bottom: ''
                    }
                });
            }

        }

    });


}

function destroyUser() {
    var row = $('#dg').datagrid('getSelected');
    if (row) {
        $.messager.confirm('Confirm', '确定要删除该用户吗?', function (r) {
            if (r) {
                var data = {id: row.id};
                $.ajax({
                    type: 'DELETE',
                    url: '/admin/api/v1.0/users',
                    data: data,
                    success: function (result) {
                        console.log(result);
                        if (result.code == 0) {
                            $('#dg').datagrid('reload');    // reload the user data
                        } else {
                            $.messager.alert({    // show error message
                                title: 'Error',
                                icon: 'error',
                                msg: result.msg,
                                showType: 'slide',
                                style: {
                                    right: '',
                                    top: document.body.scrollTop + document.documentElement.scrollTop,
                                    bottom: ''
                                }
                            });
                        }

                    }

                });
            }
        });
    }
}