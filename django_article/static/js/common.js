/*
* set global delimiters in Vue.js 2.0
*/
Vue.options.delimiters = ['[[', ']]'];
Vue.config.productionTip = false;

window.canRequest = new Array();

/***
 * Send http POST request and get response data
 * @param url
 * @param method
 * @param param
 * @param callback
 * @private
 */
function _dqRequest(url, method, param, callback) {

    if (window.canRequest[callback] == undefined || window.canRequest[callback]) {
        window.canRequest[callback] = false;
        window.deviceClientWidth = document.body.clientWidth;
        $.ajax(url, {
            data: param,
            crossDomain: true == !(document.all),
            xhrFields: {
                withCredentials: true
            },
            dataType: 'json',
            type: method,
            timeout: 30000,
            beforeSend: function () {
                if (window.deviceClientWidth < 1200) {
                    Vue.prototype._beforeSendAjax();
                }
            },
            complete: function () {
                if (window.deviceClientWidth < 1200) {
                    Vue.prototype._completeAjax();
                }
            },
            success: function (response) {
                delete window.canRequest[callback];
                if (response && response.hasOwnProperty('return_code')) {
                    callback(response);
                } else {
                    console.log('Incorrect data format');
                }
                if (window.deviceClientWidth < 1200) {
                    Vue.prototype._completeAjax();
                }
            },
            error: function (xhr, type, errorThrownhr) {
                delete window.canRequest[callback];
                // console.log(new Date() + '【AJAX:ERR】-|T:' + type + '|H:' + errorThrownhr);
                if (window.deviceClientWidth < 1200) {
                    Vue.prototype._completeAjax();
                }
            }
        }); //ajax end
    }
}
