$.ajaxSetup({ 
     beforeSend: function(xhr, settings) {
         function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = jQuery.trim(cookies[i]);
                     // Does this cookie string begin with the name we want?
                 if (cookie.substring(0, name.length + 1) == (name + '=')) {
                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                     break;
                 }
             }
         }
         return cookieValue;
         }
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     } 
});//end of ajax setup

function searchSymptoms() {
  var filter_term = $('.search_term').val();
  console.log(filter_term);
    $.ajax({
      url:'/filterSymptoms/',
      type: "GET",
      dataType: 'json',
      data: {filter_term: filter_term},
      success:function(data){
        var old_symptoms = document.getElementsByClassName("old_symptom");
        var bad_symptoms = data.bad_symptoms;
        for (var i = 0; i<old_symptoms.length; i++)
        {
          var id = old_symptoms[i].getAttribute('id');
          var index = bad_symptoms.indexOf(id);
          if (index == -1) //its not a bad symptom
          {
            old_symptoms[i].style.display = 'block';
          }
          else
          {
            old_symptoms[i].style.display = 'none';
          }
        }
      },
      complete:function(){},
      error:function (xhr, textStatus, thrownError){}
  });
}
$(document).ready(function(){
    $('.search_term').keypress(function(){
      searchSymptoms();
    });
});