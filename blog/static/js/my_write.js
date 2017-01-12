$(document).ready(function(){
    $("#navbar li").click(function(){
        $(this).addClass('active');
        // $(this).siblings().removeClass('active');
    });
})