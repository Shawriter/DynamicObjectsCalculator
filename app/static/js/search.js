
function search() {
    let timeout = null;

    document.getElementById('search-box').addEventListener('input', function(e) {
        clearTimeout(timeout);
    
        timeout = setTimeout(function() {
            var search = e.target.value;
    
            fetch('/search?q=' + encodeURIComponent(search))
                .then(response => response.json())
                .then(data => {
                    var resultsDiv = document.getElementById('results');
                    resultsDiv.innerHTML = '';
                    data.forEach(item => {
                        var div = document.createElement('div');
                        div.textContent = item.title;
                        resultsDiv.appendChild(div);
                    });
                });
        }, 300); 
    });}