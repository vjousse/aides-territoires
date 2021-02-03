(function (exports) {
    "use strict";

    exports.trackResultsAlertButtonClick = function(alert_link, source) {
        alert_link.click(function(evt) {
            if (_paq) {
                _paq.push(['trackEvent', 'Alerte bouton', source]);
            }
        });
    }
})(this);

$(document).ready(function () {
    // Track clicks on alert button above the search form
    var resultsFormAlertButton = $('a#save-alert-btn');
    if (resultsFormAlertButton) {
        trackResultsAlertButtonClick(resultsFormAlertButton, 'Alerte bouton click (résultats > formulaire)');
    }

    // Track clicks on alert button in the aid results (alert block)
    var resultsBlockAlertButton = $('a#save-alert-block-btn');
    if (resultsBlockAlertButton) {
        trackResultsAlertButtonClick(resultsBlockAlertButton, 'Alerte bouton click (résultats > encart)');
    }
});
