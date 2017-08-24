var elements;

$(function() {

    elements = {
      search: document.getElementById('search'),
      search_results: document.getElementById('search-results'),
      user_select: document.getElementsByClassName('user-select'),
    }

    elements.search.addEventListener('keyup', (function() {
        $.ajax({
            type: 'POST',
            url: '/connections/search/',
            data: {
                'search_text': elements.search.value
            },
            success: searchSuccess,
            dataType: 'html'
        });

        if (this.value == '') {
            elements.search_results.style.display = 'none';
        } else {
            elements.search_results.style.display = 'block';
        }
    }));
});

function searchSuccess(data, textStatus, jqXHR) {
    elements.search_results.innerHTML = data;
} 





