/**
 * Handles the aid alert creation form.
 */
(function (exports, catalog) {
    'use strict';

    var searchForm = $('form#search-form');

    var queryField = $('form#search-form input#id_text');
    var perimeterField = $('form#search-form select#id_perimeter');
    var alertNameField = $('form#alert-form input#id_title');
    var emailField = $('form#alert-form input#id_email');


    /**
     * Prepend current search parameters to the form data.
     *
     * The "alert creation form" does not actually holds the fields
     * for the current search. Hence, we have to append the search fields
     * (that are held in a different form) to the currently posted data.
     */
    exports.appendQuerystringToForm = function (event) {
        var querystring = searchForm.serialize();
        // if in aid detail, searchForm is empty. Use CURRENT_SEARCH instead
        if (!querystring && (typeof CURRENT_SEARCH !== "undefined")) {
            // var querystring = CURRENT_SEARCH.split("&")
            //                                 .filter(e => /^(?!.*(order_by|action)).*$/i.test(e))
            //                                 .join("&");
            var EMPTY_SEARCH = "integration=&text=&apply_before=&&order_by=";
            var querystring = CURRENT_SEARCH || EMPTY_SEARCH;
        }
        var input = $('<input />');
        input.attr('type', 'hidden');
        input.attr('name', 'querystring');
        input.attr('value', querystring);
        input.appendTo(this);
        return true;
    };

    /**
     * Prefill the "alert title" field upon aid modal opening.
     */
    exports.prefillAlertNameField = function (event) {
        var nameSuggestion;

        var query = queryField.val() || '';
        var perimeter = perimeterField.children('option:selected').text();
        var perimeterName = perimeter.split(' (')[0];

        if (query !== '' && perimeterName !== '') {
            nameSuggestion = perimeterName + ' — ' + query;
        } else {
            nameSuggestion = perimeterName + ' ' + query;
        }

        alertNameField.val(nameSuggestion.trim());
    };

    exports.focusForm = function (event) {
        emailField.focus();
    };

})(this, catalog);

$(document).ready(function () {
    $('div#alert-search-modal').on('show.bs.modal', prefillAlertNameField);
    $('div#alert-search-modal').on('shown.bs.modal', focusForm);
    $('form#alert-form').on('submit', appendQuerystringToForm);
});
