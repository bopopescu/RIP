// Загрузка элементов
function loadBands(pageNumber) {
    csrf_token = '{{ csrf_token }}';

    // Показываем загрузку
    $("#band-pages").append("<p id=\"progress\" style=\"text-align: center;\n\">🔎 Loading..</p>");
    console.log('Error with response:')
    $.ajax({
        url: 'band/page=' + pageNumber,
        type: 'GET',
        headers: {'X-CSRFToken': csrf_token},
        success: function (response) {
            // Удаляем загрузку
            $('#progress').remove()

            // Добавляем новую порцию элементов
            var rows = $(response).find('#row')
            $('#band-pages').append(rows);
        },
        error: function (response) {
            console.log('Error with response: ' + response) // ошибка загрузки порции
        }
    });
}