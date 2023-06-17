window.arr = '';

$(document).ready(function() {
    console.log('документ готов');
    arr = $('.image > img').attr('src');
    for( let i=1 ; i < 6 ; i += 2 ){
        $('.pi:eq(' + i + ')').html('10');
        $('.pi:eq(' + (i-1) + ')').attr({'min': '5', 'max': '30', 'value': '10'});
        $('.strelkam:eq(' + (i-1) + '), .strelkam:eq(' + i + '), .strelkap:eq(' + (i-1) + '), .strelkap:eq(' + i + ')').attr({'num': (i-1)/2});
    }
    for( let p=7 ; p < 12 ; p += 2 ){
        $('.pi:eq(' + p + ')').html('5');
        $('.pi:eq(' + (p-1) + ')').attr({'min': '0', 'max': '15', 'value': '5'});
        $('.strelkam:eq(' + (p-1) + '), .strelkam:eq(' + p + '), .strelkap:eq(' + (p-1) + '), .strelkap:eq(' + p + ')').attr({'num': (p-1)/2});
    }
});

$('.strelkam.double').click(function(){
    let er = $(this).attr('num');
    if (er < 3){
        $('.pi:eq(' + (er*2) + ')').attr({'value': '5'});
        $('.pi:eq(' + (er*2+1) + ')').html('5');
        let n = 0;
        for(let i=0; i < 3; i++){
            n += parseInt($('.pi:eq(' + (i*2) + ')').attr('value'));
        }
        $('#13').text(30-n);
    }
    else if (er >= 3){
        $('.pi:eq(' + (er*2) + ')').attr({'value': '0'});
        $('.pi:eq(' + (er*2+1) + ')').html('0');
        let n = 0;
        for(let i=3; i < 6; i++){
            n += parseInt($('.pi:eq(' + (i*2) + ')').attr('value'));
        }
        $('#46').text(15-n);
    }
});

$('.strelkam:not(.double)').click(function(){
    let er = $(this).attr('num');
    if (er < 3){
        let k = parseInt($('.pi:eq(' + (er*2+1) + ')').html());
        if (k > 5) {
            $('.pi:eq(' + (er*2) + ')').attr({'value': k-1});
            $('.pi:eq(' + (er*2+1) + ')').html(k-1);
        }
        let n = 0;
        for(let i=0; i < 3; i++){
            n += parseInt($('.pi:eq(' + (i*2) + ')').attr('value'));
        }
        $('#13').text(30-n);
        
    }
    else if (er >= 3){
        let k = $('.pi:eq(' + (er*2+1) + ')').html();
        if (k > 0) {
            $('.pi:eq(' + (er*2) + ')').attr({'value': k-1});
            $('.pi:eq(' + (er*2+1) + ')').html(k-1);
        }
        let n = 0;
        for(let i=3; i < 6; i++){
            n += parseInt($('.pi:eq(' + (i*2) + ')').attr('value'));
        }
        $('#46').text(15-n);
    }
});

$('.strelkap.double').click(function(){
    let er = $(this).attr('num');
    if (er < 3){
        let n = 0;
        for(let i=0; i < 3; i++){
            n += parseInt($('.pi:eq(' + (i*2) + ')').attr('value'));
        }
        let num = parseInt($('.pi:eq(' + (er*2) + ')').attr('value'));
        $('.pi:eq(' + (er*2) + ')').attr({'value': 30-n+num});
        $('.pi:eq(' + (er*2+1) + ')').html(30-n+num);
        $('#13').text(0);
    }
    else if (er >= 3){
        let n = 0;
        for(let i=3; i < 6; i++){
            n += parseInt($('.pi:eq(' + (i*2) + ')').attr('value'));
        }
        let num = parseInt($('.pi:eq(' + (er*2) + ')').attr('value'));
        $('.pi:eq(' + (er*2) + ')').attr({'value': 15-n+num});
        $('.pi:eq(' + (er*2+1) + ')').html(15-n+num);
        $('#46').text(0);
    }
});

$('.strelkap:not(.double)').click(function(){
    let er = $(this).attr('num');
    if (er < 3){
        let n = 0;
        for(let i=0; i < 3; i++){
            n += parseInt($('.pi:eq(' + (i*2) + ')').attr('value'));
        }
        let k = parseInt($('.pi:eq(' + (er*2+1) + ')').html());
        if (n < 30) {
            $('.pi:eq(' + (er*2) + ')').attr({'value': k+1});
            $('.pi:eq(' + (er*2+1) + ')').html(k+1);
            $('#13').text(30-n-1);
        }
        else {
            $('#13').text(30-n);
        }
    }
    else if (er >= 3){
        let n = 0;
        for(let i=3; i < 6; i++){
            n += parseInt($('.pi:eq(' + (i*2) + ')').attr('value'));
        }
        let k = parseInt($('.pi:eq(' + (er*2+1) + ')').html());
        if (n < 15) {
            $('.pi:eq(' + (er*2) + ')').attr({'value': k+1});
            $('.pi:eq(' + (er*2+1) + ')').html(k+1);
            $('#46').text(15-n-1);
        }
        else {
            $('#46').text(15-n);
        }
    }
});

$("div.fieldset > label").click(function() {
    let str = $(this).html();
    console.log(str, arr);
    if (str == 'Мужчина'){
        $('.image').html('<img src="'+ arr + '" alt="">');
    }
    else if (str == 'Женщина') {
        $('.image').html('<div> пизда </div>');
    }
});