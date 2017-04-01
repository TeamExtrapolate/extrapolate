var login = (function () {
    var form, formData, url;

    function login(e) {
        e.preventDefault();
        formData = new FormData(this);
        url = location.href;
        $.ajax({
            url: url,
            type: 'POST',
            contentType: !1,
            processData: !1,
            data: formData,
            responseType: "json",
            success: function () {
                location.href = '../predictions/';
            },
            error: function () {

            }
        })
    }

    return {
        init: function () {
            form = document.getElementById("login-form");
            form.addEventListener('submit', login);
        }
    };

})();