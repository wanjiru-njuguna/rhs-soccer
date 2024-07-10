/* Project specific Javascript goes here. */
document.addEventListener('htmx:beforeOnLoad', function(evt) {
    var xhr = evt.detail.xhr;
    if (xhr.getResponseHeader('Content-Type').indexOf('application/json') > -1) {
      var response = JSON.parse(xhr.responseText);
      if (!response.authenticated) {
        evt.preventDefault();
        fetch(response.redirect_to)
          .then(response => response.text())
          .then(html => {
            document.querySelector('#loginModal .modal-content').innerHTML = html;
            var loginModal = new bootstrap.Modal(document.getElementById('loginModal'));
            loginModal.show();
          });
      }
    }
  });
  document.addEventListener('htmx:beforeOnLoad', function(evt) {
    var xhr = evt.detail.xhr;
    if (xhr.getResponseHeader('Content-Type').indexOf('application/json') > -1) {
      var response = JSON.parse(xhr.responseText);
      if (!response.authenticated) {
        evt.preventDefault();
        fetch(response.redirect_to)
          .then(response => response.text())
          .then(html => {
            document.querySelector('#loginModal .modal-content').innerHTML = html;
            var loginModal = new bootstrap.Modal(document.getElementById('loginModal'));
            loginModal.show();
          });
      }
    }
  });

  document.addEventListener('htmx:afterOnLoad', function(evt) {
    var xhr = evt.detail.xhr;
    if (xhr.getResponseHeader('Content-Type').indexOf('application/json') > -1) {
      var response = JSON.parse(xhr.responseText);
      if (response.success) {
        var loginModal = bootstrap.Modal.getInstance(document.getElementById('loginModal'));
        loginModal.hide();
        // Trigger the original modal after successful login
        fetch('{% url "modal_content" %}')
          .then(response => response.text())
          .then(html => {
            document.querySelector('#exampleModal .modal-content').innerHTML = html;
            var exampleModal = new bootstrap.Modal(document.getElementById('exampleModal'));
            exampleModal.show();
          });
      }
    }
  });