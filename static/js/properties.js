$(document).ready(function(){
    console.log("This is the submit")
    var BASE_ENDPOINT = new URL('/', location.href).href;
    // var spinner = $('#spinner');
    var spinner = document.getElementById('spinner');
    var formSubmitBtn = document.getElementById('form-submit-btn');
    spinner.style.visibility = "hidden";
    spinner.style.display = "none";


    $('#add-property-type-form').on('submit', function(e){
    e.preventDefault();
    spinner.style.visibility = "visible";
    spinner.style.display = "";
    formSubmitBtn.disabled = true;
    $.ajax({
        
        type:'POST',
        url: BASE_ENDPOINT+'properties/save-property-types/',

        // url: '{% url "properties:save-property-types" %}', 
        data: {
            name: $('#name').val(),
            notes: $('#notes').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            action: 'post'
        },
        
        success:function(json){
            console.log('Submission was successful.');
            console.log(json);
        },
        error : function(xhr,errmsg,err) {
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    }
    }).done(function(data) {
        console.log("Done -----------------> resp ",data);
        // $(".table").html(resp);
        

        setTimeout(function () {
        spinner.style.visibility = "hidden";
        spinner.style.display = "none";
        formSubmitBtn.disabled = false;
        $('.modal').modal('hide');
        $('body').removeClass('modal-open');
        $('.modal-backdrop').remove();
        } , 1500);
        // $('#property-table').html(resp);
        $('#property-table').append(setValue(data));
        // $(".table").ajax.reload();
        // location.reload();
      });
})
});

function setValue(data) {
    console.log(" setValue(data) ----------------->  setValue(data) ",data);
    console.log(" setValue(data) ----------------->  setValue(data) ",data.length);
    var html = "";

    html += '<tr>';
            html += '<td>' + data.name + '</td>';
            html += '<td>' + data.notes  + '</td>';
            html += '<td>' + 'data.response.Result[i].start' + '</td>';
            html += '<td>' + 'data.response.Result[i].finish' + '</td>';
            html += '</tr>';


    // if (data.response == 1) {
    //     for (i = 0; i < data.response.length; i++) {
    //         html += '<tr>';
    //         html += '<td>' + (i + 1) + '</td>';
    //         html += '<td>' + 'data.response.Result[i].name '+ '</td>';
    //         html += '<td>' +' data.response.Result[i].notes' + '</td>';
    //         html += '<td>' + 'data.response.Result[i].start' + '</td>';
    //         html += '<td>' + 'data.response.Result[i].finish' + '</td>';
    //         html += '</tr>';
    //     }
    // }
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
