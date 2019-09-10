//モーダル画面の切替
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

//登録フォームのラベル移動
$(function(){
    $('input').on('focusin', function() {
    $(this).parent().find('label').addClass('active');
    }).on('focusout', function() {
    if (!this.value) {
        $(this).parent().find('label').removeClass('active');
    }
    });
});

//ステータスボタン押下でajax処理（ステータス更新）
$(function(){
    $('span.status').on('click', function(){
        var status = $(this).parent().find('input#status').attr('value') == "0" ? 1 : 0 ;
        var status_after_string = status == 0 ? 'incomplete' : 'complete' ;
        var status_before_string = status == 0 ? 'complete' : 'incomplete' ;
        var id = $(this).parent().attr('id');
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
                    $('.status#' + id).html(status_after_string);
                    $('.status#' + id).attr('class', 'status ' + status_after_string);
                    $('form#' + id).find('input#status').attr('value', status)
                },
                function(){
                    $('.status#' + id).html(status_after_string);
                    $('.status#' + id).attr('class', 'status ' + status_after_string);
                    $('form#' + id).find('input#status').attr('value', status)
                }
        );
    });
});