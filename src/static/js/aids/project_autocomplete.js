$(document).ready(function () {

    CATEGORIES = []

    $('select#id_categories').change(function(){
        $( "select#id_categories option:selected" ).each(function() {
            CATEGORIES = $(this).text().split("> ").pop()
            console.log(CATEGORIES)
          });
    })

    $('select#id_projects').select2({
        placeholder: catalog.project_placeholder,
        language: 'fr',
        minimumInputLength: 0,
        language: {
            inputTooShort: function() { return catalog.autocomplete_placeholder; },
        },
        ajax: {
            url: '/api/projects/',
            dataType: 'json',
            delay: 100,
            data: function (params) {
                var query = {
                  q: params.term,
                  is_published: true,
                  categories: CATEGORIES,
                  page: params.page || 1
                }
                return query;
              },
              processResults: function (data, params) {
                  params.page = params.page || 1;
                  console.log(CATEGORIES)
                  if (data.results.length === 0) {
                    $("#other_project_box").removeClass("d-none");
                  } 
                  return {
                      results: data.results,
                      pagination: {
                          more: data.next != null
                      }
                  };
              }
        },
        theme: 'bootstrap4',
        width: '',
    });
});
