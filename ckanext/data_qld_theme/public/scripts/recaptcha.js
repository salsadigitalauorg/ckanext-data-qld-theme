(function($) {
    "use strict";
    $(document).ready(function() {
      let sitekey = "";
      let form_capable = $("form");
      if (form_capable.attr("data-recaptcha") === true) {
        $.getScript(
          "https://www.google.com/recaptcha/api.js?render=" + sitekey,
          function() {}
        ).promise()
          .done(function() {
            grecaptcha.ready(function() {
              grecaptcha
                .execute(sitekey, { action: "homepage" })
                .then(function(token) {
                  form_capable
                    .find('input[type="submit"], button[type="submit"]')
                    .on("click", e => {
                      e.preventDefault();
                      var subBtn = e.target;
                      var form = $(subBtn).parents("form");
                      var greptcha = $('input[name="g-recaptcha-response"]');
                      if (greptcha.length > 0) {
                        if (
                          greptcha.attr("value") !== "" ||
                          greptcha.attr("value").length !== 0 ||
                          greptcha.attr("value") !== undefined
                        ) {
                          greptcha.val(token);
                          form.submit();
                        }
                      }
                    });
                });
            });
          });
       }
    });
  })(jQuery);
  
