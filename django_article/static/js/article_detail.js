$(function(){
    
    _setImgWidthHeight();
    $(window).resize(function() {
       _setImgWidthHeight();
    });

    function _setImgWidthHeight() {
        var width = document.body.clientWidth;
        $(".title-image").css({'width': width - 42,'height' : (width - 42) * 0.4895});
    }
})

var app = new Vue({
    el: '#app',
    data: {
        aid: aid,
        article:{},
        prev_article:{},
        next_article:{},
    },
    created:function() {
        this.articleDetail();
    },
    methods: {
        articleDetail: function () {
            _dqRequest('/api/article/', 'POST', {
                aid: this.aid,
                csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
            }, function (r) {
                if (r.return_code == 0) {
                    app.article = r.data.article;
                    app.prev_article = r.data.prev_article;
                    app.next_article = r.data.next_article;
                } else {
                    toastr.error(r.return_message);
                }
            });

        }
    }
});


