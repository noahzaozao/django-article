$(function () {

    _setImgWidthHeight();
    $(window).resize(function () {
        _setImgWidthHeight();
    });

    function _setImgWidthHeight() {
        var width = document.body.clientWidth;
        $(".article-image").css({'width': width - 42, 'height': (width - 42) * 0.4895});
    }
});

var app = new Vue({
    el: '#app',
    data: {
        articles: [],
    },
    created: function () {
        this.articleList();
    },
    methods: {
        articleList: function () {
            _dqRequest('/api/article/list/', 'POST', {
                csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
            }, function (r) {
                if (r.return_code == 0) {
                    app.articles = r.data.articles;
                } else {
                    toastr.warning(r.return_message);
                }
            });

        }
    }
});


