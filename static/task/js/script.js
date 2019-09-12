// ------------------------------------------- //
// ユーティリティ
// ------------------------------------------- //

// 関数遅延実行
function sleep(waitSec, callbackFunc) {
    var spanedSec = 0;
    var id = setInterval(function () {
        spanedSec++;
        if (spanedSec >= waitSec) {
            clearInterval(id);
            if (callbackFunc) callbackFunc();
        }
    }, 1000);
}
// モーダルメッセージ
function modal_message(message){
    document.getElementById("result_message").innerHTML = message;
    $('.js-modal-message').fadeIn();
    sleep(1,function(){
        $('.js-modal-message').fadeOut();
    });
    $('.modal__message').find('.message').text('');
    return false;
}

// ------------------------------------------- //
// 画面操作
// ------------------------------------------- //
// タスクのドラッグ＆ドロップ
$(function(){
    Sortable.create(movement, {
        group: "hoge",
        handle: ".taskblock",
        animation: 200
    });
});

// モーダル画面の切替
$(function(){
    $('.js-modal-create-open').on('click',function(){
        $('.js-modal-create').fadeIn();
        return false;
    });
    $('.js-modal-create-close').on('click',function(){
        $('.js-modal-create').fadeOut();
        $(this).parent().find('input').val('');
        $(this).parent().find('label').removeClass('active');
        return false;
    });
});


// 登録フォームのラベル移動
$(function(){
    $('input').on('focusin', function() {
    $(this).parent().find('label').addClass('active');
    }).on('focusout', function() {
    if (!this.value) {
        $(this).parent().find('label').removeClass('active');
    }
    });
});

// ajax処理
$(function(){
    // ステータスの更新
    $('span.status').on('click', function(){
        var status = $(this).parent().find('input#status').attr('value') == "0" ? 1 : 0 ;
        var status_after_string = status == 0 ? 'incomplete' : 'complete' ;
        var status_before_string = status == 0 ? 'complete' : 'incomplete' ;
        var id = $(this).parent().attr('id').slice(1);
        $.ajax({
            'url': $(this).parent().attr('action'),
            'type': 'POST',
            'data':{
                'csrfmiddlewaretoken' : $(this).parent().find('input').attr('value'),
                'status': status,
                'id': id,
            },
            'datatype': 'json',
        })
        .then(
                function(data){
                    $('.status.'+ status_before_string +'#' + id).html(status_after_string);
                    $('.status.'+ status_before_string +'#' + id).attr('class', 'status ' + status_after_string);
                    $('form#i' + id).find('input#status').attr('value', data['status'])
                },
                function(){
                    $('.status.'+ status_before_string +'#' + id).html(status_after_string);
                    $('.status.'+ status_before_string +'#' + id).attr('class', 'status ' + status_after_string);
                    $('form#i' + id).find('input#status').attr('value', data['status'])
                }
        );
    });

    // タスクの削除
    $('i#delbtn').on('click', function(){
        var id = $(this).parent().attr('id');
        $.ajax({
            'url': $(this).parent().attr('action'),
            'type': 'POST',
            'data':{
                'csrfmiddlewaretoken' : $(this).parent().find('input').attr('value'),
                'id': id,
            },
            'datatype': 'json',
        })
        .then(
                function(data){
                    $('#i' + id + '.taskblock').addClass('fadeout');
                    sleep(1, function(){
                        $('#i' + id + '.taskblock').remove();
                    });
                    modal_message("Task was deleted.")
                },
                function(){
                    modal_message("Can't delete Task.")
                }
        );
    });
});