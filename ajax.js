var ajax_req = (function () {
    var url, formData;

    function make_request(event) {
        event.preventDefault();
        url = '/'; // endpoint
        formData = new FormData(this);
        $.ajax({
            url: url,
            type: 'POST',
            data: formData,
            contentType: !1,
            processData: !1,
            dataType: "json",
            success: function () {

            },
            error: function () {

            }
        })
    }

    return {
        init: function () {
            var form = document.getElementsById(''); // put form-id here
            form.addEventListener('submit', make_request);
        }
    }
})();