$(document).ready(function () {
    $('select#id_targeted_audiances').select2({
        placeholder: catalog.autocomplete_placeholder,
        language: 'fr',
        theme: 'bootstrap4',
        width: '',
    });
});
