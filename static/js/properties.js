$(document).ready(function(){
    console.log("This is the submit")
    var BASE_ENDPOINT = new URL('/', location.href).href;

    console.log("BASE_ENDPOINT", BASE_ENDPOINT)

    $('#add-property-type-form').on('submit', function(e){
    e.preventDefault();
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
            document.getElementById("add-property-type-form").reset();
            console.log('Submission was successful.');
            console.log(json);
            $(".posts").prepend('<div class="col-md-6">'+
                '<div class="row no-gutters border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">' +
                    '<div class="col p-4 d-flex flex-column position-static">' +
                        '<h3 class="mb-0">' + json.name + '</h3>' +
                        '<p class="mb-auto">' + json.notes + '</p>' +
                    '</div>' +
                '</div>' +
            '</div>' 
            )
        },
        error : function(xhr,errmsg,err) {
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    }
    });
})
});

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
