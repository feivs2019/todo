$(function(){
    $('.js-modal-create-open').on('click',function(){
        $('.js-modal-create').fadeIn();
        return false;
    });
    $('.js-modal-create-close').on('click',function(){
        $('.js-modal-create').fadeOut();
        return false;
    });
});