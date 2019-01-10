// Обработка нажатия на "Send transaction"
$('#transaction-form').on('submit', function(event){
    event.preventDefault();
    send_transaction();
});

// AJAX-запрос на отправку транзакции
function send_transaction() {
    var csrf_token = '{{ csrf_token }}';

    // Создаем AJAX-запрос
    $.ajax({
        url : "modal_transaction/", // выход
        type : "POST", // метод
        data : {
            "account_to" : $('#account_to').val(),
            "account_from" : $('#account_from').val(),
            "money" : $('#money').val(),
            "comments" : $('#comments').val()
        }, // json с данными

        headers : {'X-CSRFToken': csrf_token},

        // Обрабатываем success
        success : function(json) {


            var idTransactions = json['idTransactions']
            var accountId_from = json['accountId_from']
            var fio_from = json['fio_from']
            var accountId_to = json['accountId_to']
            var money = json['money']
            var currency = json['currency']
            var comments = json['comments']
            var time_t = json['time_t']

            $('#money_minus').append(
                "<h5> id Транзакции: " + idTransactions + "</h5>" +
                "<h5> id счета отправителя: " + accountId_from + "<br>" +
                "ФИО: " + fio_from + "</h5>" +
                "<h5> id Счета (на какой): " + accountId_to + "</h5>" +
                "<h5> Сумма: " + money + " " + currency + "</h5>" +
                "<h5> Комментарии: " + comments + "</h5>" +
                "<h6 class=\"text-primary\"> Дата: " + time_t + "</h6>" +
                "<div class=\"well well-sm\"></div>")

        },

        // Обрабатываем error
        error : function(xhr,errmsg,err) {

            // Показываем алерт с ошибкой
            $('#transaction-form').prepend("<div class=\"alert alert-danger alert-dismissible fade show\" role=\"alert\" style=\"border-radius: 15px\">" +
                "                          <button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\">" +
                "                              <span aria-hidden=\"true\">&times;</span>" +
                "                          </button>" +
                "                          <strong>Oops!</strong> We have encountered an error: " +
                "                      </div>")        }
    });
};


//валидация формы
function showError(container, errorMessage){

    container.className = 'error';
    var msgElem = document.createElement('span');
    msgElem.className = "error-message";
    msgElem.innerHTML = errorMessage;
    container.appendChild(msgElem);
}

function resetError(container){
    container.className = '';
    if (container.lastChild.className == "error-message"){
        container.removeChild(container.lastChild);
        }
}

function validate(form){
    var elems = form.elements;

    resetError(elems.account_to.parentNode);
    if (!elems.account_to.value){
        showError(elems.account_to.parentNode, ' Укажите куда');
    }

    resetError(elems.money.parentNode);
    if (!elems.money.value){
        showError(elems.money.parentNode, ' Сколько переводить будем?');
    }
    if (elems.money.value > elems.money_now.value){
        showError(elems.money.parentNode, ' Недостаточно средств для перевода')
    }

    resetError(elems.comments.parentNode);
    if (!elems.comments.value){
        showError(elems.comments.parentNode, ' Укажите комментарии');
    }

}