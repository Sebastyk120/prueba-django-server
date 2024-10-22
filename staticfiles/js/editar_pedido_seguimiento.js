$(document).ready(function () {

    var itemId = null;

    $('.mover-button').click(function () {
        itemId = $(this).data('pedido-id');
        $.ajax({
            url: '/comercial/pedido_editar_seguimiento',
            type: 'get',
            data: {'pedido_id': itemId},
            success: function (data) {
                $('.modal-content').html(data.form);
                $('#moverItemModal').modal('show');
            }
        });
    });

    $(document).on('submit', '#moverItemForm', function (event) {
        event.preventDefault();
        var serializedData = $(this).serialize() + '&pedido_id=' + itemId;
        console.log(serializedData); // Imprimir los datos serializados
        $.ajax({
            url: '/comercial/pedido_editar_seguimiento',
            type: 'post',
            data: serializedData,
            success: function (data) {
                if (data.success) {
                    $('#moverItemModal').modal('hide');
                    location.reload();
                } else {
                    console.log(data);
                    var errorMessage = data.error;
                    $('#errores').html('<div class="alert alert-danger">' + errorMessage + '</div>');
                }
            },
            error: function (jqXHR, textStatus, errorThrown) {
                console.log("AJAX Error: ", textStatus, errorThrown);
            }
        });
    });

});
