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
        // console.log(data);
        var old_symptoms = document.getElementsByClassName("old_symptom");
        console.log(old_symptoms);
        var bad_symptoms = data.bad_symptoms;
        console.log(bad_symptoms);
        for (var i = 0; i<old_symptoms.length; i++)
        {
          old_symptoms[i].style.visibility = 'visible';
          var id = old_symptoms[i].getAttribute('id');
          if (bad_symptoms.indexOf(id) >= 0)
          {
            old_symptoms[i].style.visibility = 'hidden';
          }
        }
        // console.log(old_symptoms);

        // console.log(data.symptom_list)
        // for (var i = 0; i<data.symptom_list.length; i++) {
        //   console.log(data.symptom_list[i]);
        //   $('.responses').prepend('<br><span>'+ data.symptom_list[i]+ '</span>')
        // }
      },
      complete:function(){},
      error:function (xhr, textStatus, thrownError){}
  });
}
$(document).ready(function(){
    $('.submit_search_button').click(function(){
        // alert('you clicked the searchBar');
        searchSymptoms();
    });
});