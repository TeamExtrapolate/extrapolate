var post_file = (function () {
    var form, formData, url, xhr;

    function successCall() {
        $('.to-hide').hide();
        $('.ul-success').removeClass("hidden");
    }

    function failCall() {
        $('.ul-fail').removeClass("hidden");
        $('.load-icon').addClass("hidden");
    }

    function submit(e) {
        e.preventDefault();
        $('.load-icon').removeClass("hidden");
        if(!$('.ul-fail').hasClass("hidden"))
            $('.ul-fail').addClass("hidden");
        url = location.href;
        formData = new FormData(this);
        xhr = new XMLHttpRequest();
        xhr.open('POST', url);
        xhr.responseType = 'blob';
        xhr.onload = function () {
            if (this.status === 200) {
                var filename = "";
                var disposition = xhr.getResponseHeader('Content-Disposition');
                if (disposition && disposition.indexOf('attachment') !== -1) {
                    var filenameRegex = /filename[^;=\n]*=((['"]).*?\2|[^;\n]*)/;
                    var matches = filenameRegex.exec(disposition);
                    if (matches != null && matches[1]) filename = matches[1].replace(/['"]/g, '');
                }
                var type = xhr.getResponseHeader('Content-Type');

                var blob = new Blob([this.response], {type: type});
                console.log("Blob" + blob)
                if (typeof window.navigator.msSaveBlob !== 'undefined') {
                    // IE workaround for "HTML7007: One or more blob URLs were revoked by closing the blob for which they were created. These URLs will no longer resolve as the data backing the URL has been freed."
                    window.navigator.msSaveBlob(blob, filename);
                } else {
                    var URL = window.URL || window.webkitURL;
                    var downloadUrl = URL.createObjectURL(blob);

                    if (filename) {
                        // use HTML5 a[download] attribute to specify filename
                        var a = document.createElement("a");
                        // safari doesn't support this yet
                        if (typeof a.download === 'undefined') {
                            window.location = downloadUrl;
                        } else {
                            a.href = downloadUrl;
                            a.download = filename;
                            document.body.appendChild(a);
                            a.click();
                        }
                    } else {
                        window.location = downloadUrl;
                    }

                    setTimeout(function () {
                        URL.revokeObjectURL(downloadUrl);
                    }, 100); // cleanup
                }
                successCall();
            }
            else if (this.status === 422) {
                failCall();
            }
        }
        xhr.send(formData);

    }

    return {
        init: function () {
            form = document.getElementById('predict-form');
            form.addEventListener('submit', submit);
        }
    };
})();