$('a.likeable').click(function(e) {
  e.preventDefault();
  var self = this;
  $.ajax({
    type: 'POST',
    url: self.attr('href'),
    dataType: 'json',
    success: function(res) {
      $(self).fadeOut("slow", function() {
        $(this).html('<span class="badge badge-important likes-badge"><span class="icon-heart"></span> ' + res.counter + '</span></span>');
        $(this).fadeIn("slow");
      });
    },
    error: function(res, err) {
      alert("ERROR" + res.responseText);
    }
  })
});
