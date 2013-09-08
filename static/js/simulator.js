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
function getClues(symptom_type){
    $.ajax({
      url:'/getClues/',
      type: "GET",
      data: {symptom_type: symptom_type, illness: illness},
      success:function(data){
        $('.responses').prepend(data);
      },
      complete:function(){},
      error:function (xhr, textStatus, thrownError){}
  });
}
function getSymptoms(symptom_type) {
    $.ajax({
      url:'/getSymptoms/',
      type: "GET",
      dataType: 'json',
      data: {symptom_type: symptom_type, illness: illness},
      success:function(data){
        console.log(data);
        console.log(data.symptom_list)
        for (var i = 0; i<data.symptom_list.length; i++) {
          console.log(data.symptom_list[i]);
          $('.responses').prepend('<br><span>'+ data.symptom_list[i]+ '</span>')
        }
      },
      complete:function(){},
      error:function (xhr, textStatus, thrownError){}
  });
}
$(document).ready(function(){
    $('.symptom_type_class').click(function(){
        getSymptoms($(this).text());
    });
});