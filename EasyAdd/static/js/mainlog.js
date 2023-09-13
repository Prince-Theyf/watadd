$(document).ready(function(){
    $('input').keyup(function(){
        let entry = $(this).val();
        if(entry ==""){
            if(!$(this).hasClass('is-invalid')){
                $(this).addClass('is-invalid');
            }
            else{
                $(this).removeClass('is-invalid');
            }
        }
    })
})