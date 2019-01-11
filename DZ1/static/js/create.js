var update_button = document.getElementById("add");
var year = document.getElementById("id_year");
var pages = document.getElementById("id_pages");
var modal = document.getElementById('myModal');
var btn = document.getElementById("myBtn");
var span = document.getElementsByClassName("close")[0];
var form_create = document.getElementById("form_create");

btn.onclick = function(e) {
    modal.style.display = "block";
};

span.onclick = function() {
    modal.style.display = "none";
};

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
};

$("#id_year").on('click', function () {
    $("#id_year").removeClass('error');
});

$("#id_pages").on('click', function () {
    $("#id_pages").removeClass('error');
});

update_button.onclick = function (e) {
    e.preventDefault();

    const formData = new FormData(form_create);

    y = parseInt(year.value);
    p = parseInt(pages.value);

    $("#id_year").removeClass('error');
    $("#id_pages").removeClass('error');

    if (!(y < 1000 || y > 2018 || p < 0)) {
        $.ajax({
            type: 'POST',
            url: '/book/create/',
            data: formData,
            processData: false,
            contentType: false,

            success: (result) => {
              modal.style.display = "none";
              $("#books").prepend(result);
            },

            error: (result) => {
              alert('Ошибка')
            }
        });
    }
    if (y < 1000 || y > 2018) {
        $("#id_year").addClass('error');
    }
    if (p < 0) {
        $("#id_pages").addClass('error');
    }
};