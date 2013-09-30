$(document).ready(function() {    
    
    $('.item').bind('click',function(){
        if($(this).attr('style') != "color:red;") {
            $(this).attr('style', 'color:red;');
        }
        else{
            $(this).attr('style', 'color:black;');
        }
    });


    $('.listsAdd').bind('click', function() {    
        $('.getDishes').find('.item').each(function(){

            if ($(this).attr('style') == "color:red;") {              
                $(this).attr('style', 'color:black;');
                if ($(this).attr('data-choice') != "true") {
                    $(this).attr('data-choice', "true")                
                    $(this).clone(true).appendTo($('.check'));
                    $(this).find('td').each(function(){
                        $(".menu_items").append('<input data-name='+$(this).attr("data-name")+' name='+$(this).attr("class")+' type="hidden" value='+JSON.stringify($(this).html())+'>')
                    })
                }
            }
        });
    });
    
    $('.listsDel').bind('click', function() {
        $('.makeMenu').find('.item').each(function(){
            if ($(this).attr('style') == "color:red;") {
                dataName = $(this).attr('data-name')              
                $(this).remove();
                $('.getDishes').find('.item').each(function(){
                    if($(this).attr('data-name') == dataName) {
                        $(this).attr('data-choice','false')
                    }
                });
                
                $('.menu_items').find('input').each(function(){
                    if ($(this).attr('data-name') == dataName) {
                        $(this).remove();
                    }
                })
            }
        });
    });
});
