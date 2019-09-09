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

$(function(){
    $('input').on('focusin', function() {
    $(this).parent().find('label').addClass('active');
    }).on('focusout', function() {
    if (!this.value) {
        $(this).parent().find('label').removeClass('active');
    }
    });
});