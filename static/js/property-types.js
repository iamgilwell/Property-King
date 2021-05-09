$(document).ready(function () {
  
  var BASE_ENDPOINT = new URL('/', location.href).href;
  var propertyAddForm = document.getElementById("add-property-type-form");
  var spinner = document.getElementById('spinner');
  var formSubmitBtn = document.getElementById('form-submit-btn');
  var txtName = document.getElementById('property_name');
  var txtNotes = document.getElementById('notes');
  var formError = document.getElementById('form-error');

  spinner.style.visibility = 'hidden';
  spinner.style.display = 'none';
  formError.style.display = "none"

  var csrftoken =  $('input[name=csrfmiddlewaretoken]').val();

  $('#form-submit-btn').click('submit', function (e) {
    e.preventDefault();
    if (txtName.value === '' || txtNotes.value === '') {
      if(txtName.value === ''){
        txtName.classList.add("is-invalid")
      }
      if(txtNotes.value === ''){
        txtNotes.classList.add("is-invalid")
      }
    } 

    // else {
    spinner.style.visibility = 'visible';
    spinner.style.display = '';
    formSubmitBtn.disabled = true;

    $.ajax({
      type: 'POST',
      headers: {
        "X-CSRFTOKEN": csrftoken
},
      url: BASE_ENDPOINT + 'properties/save-property-types/',      
      data: {
        name: txtName.value,
        notes: txtNotes.value,
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        // action: 'post',
      },
      // data: JSON.stringify(_data),      
      success: function (json) {
        console.log('Submission was successful.');
        console.log(json);
        formError.style.display = "none"
        propertyAddForm.reset();
      
      },
      error: function (xhr, errmsg, err) {
        console.log(xhr)

        spinner.style.visibility = 'hidden';
        formSubmitBtn.disabled = false;
        spinner.style.display = 'none';
        if(xhr.status == 400){
          var error = xhr.responseJSON['error']
          formError.style.display = "block"
          console.log(error)
        }
      },
    }).done(function (data) {
      setTimeout(function () {
        spinner.style.visibility = 'hidden';
        spinner.style.display = 'none';
        formSubmitBtn.disabled = false;
        $('#addPropertyTypeModal').modal('hide');
        $('body').removeClass('modal-open');
        $('.modal-backdrop').remove();
        $('#property-table').append(setValue(data));
        formError.style.display = ""
      }, 1500);
      setTimeout(function () {
        $('#alertSuccess').show(); //or fadeIn
        setTimeout(function () {
          $('#alertSuccess').hide(); //or fadeOut
        }, 5000);
      }, 2000);
    });
    // }
  });
});

function showalert(message, alerttype) {
  $('#alert_placeholder').fadeIn(
    '<div id="alertdiv" class="alert ' +
      alerttype +
      '" role="alert"><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>' +
      message +
      '</div>'
  );
  setTimeout(function () {
    $('#alertdiv').remove();
  }, 5000);
}

function setValue(data) {
  var html = '';
  html += '<tr>';
  html += '<td>' + data.name + '</td>';
  html += '<td>' + data.notes + '</td>';
  html += '<td>' + data.created_date + '</td>';
  html += '<td>' + data.updated_date + '</td>';
  html += '</tr>';
  return html;
}

// $(document).on('submit', '#add-property-type-form',function(e){
//     console.log("This is the submit")
//     $.ajax({
//         type:'POST',
//         // {% comment %} url:'{% url "create" %}', {% endcomment %}
//         data:{
//             title:$('#title').val(),
//             description:$('#description').val(),
//             csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
//             action: 'post'
//         },
//         success:function(json){
//             document.getElementById("add-property-type-form").reset();
//             $(".posts").prepend('<div class="col-md-6">'+
//                 '<div class="row no-gutters border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">' +
//                     '<div class="col p-4 d-flex flex-column position-static">' +
//                         '<h3 class="mb-0">' + json.title + '</h3>' +
//                         '<p class="mb-auto">' + json.description + '</p>' +
//                     '</div>' +
//                 '</div>' +
//             '</div>'
//             )
//         },
//         error : function(xhr,errmsg,err) {
//         console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
//     }
//     });
// })
