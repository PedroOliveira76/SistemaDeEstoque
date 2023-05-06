///

$(document).ready(function () {
    $('.btn').click(function () {
        var btnIndex = $(this).index();
        var divs = $('.funcionaPF');
        var visibleDiv = divs.filter(function () {
            return $(this).css('display') !== 'none';
        });

        if (visibleDiv.length && visibleDiv.index() === btnIndex) {
            visibleDiv.toggle();
        } else {
            visibleDiv.slideUp(function () {
                divs.eq(btnIndex).slideDown();
            });
        }
    });

    $(()=>{
        lista_divs = document.querySelectorAll('.funcionaPF')
        $.each(lista_divs, function (){ 
             $(this).draggable({
                containment: "window"
             })
        });
    });
});

///


$('#addProduto').click(function (e) {

    if (e.button != 1) {
        $('#cadastrarProd').toggle();
    }

    

    return false;
});

$('#editProduto').click(function (e) {

    if (e.button != 1) {
        $('#editar').toggle();
    }
    return false;
});

$('#procurarProduto').click(function (e) {
    if (e.button != 1) {
        $('#procurar').toggle();
    }
    return false;

});

$('#excluirProduto').click(function (e) {
    if (e.button != 1) {
        $('#deletar').toggle();
    }
    return false;

});

$('#btnSair').click(function (e) {
    alert('Voltando ao login')
}); 

$('#refresh').click(function (e) {
    location.reload()
}); 
