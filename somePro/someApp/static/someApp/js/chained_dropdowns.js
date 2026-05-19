document.addEventListener("DOMContentLoaded", function () {
  if (typeof django !== "undefined" && django.jQuery) {
    (function ($) {
      $(document).ready(function () {
        var local_ajax_establecimientos = "/api/ajax/load-establecimientos/";
        var local_ajax_estamentos = "/api/ajax/load-estamentos/";

        var $redSelect = $("#id_red");
        var $establecimientoSelect = $("#id_establecimiento");
        var $estamentoSelect = $("#id_estamento");

        function updateEstablecimientos(initialEst) {
          var redId = $redSelect.val();
          if (redId) {
            $.ajax({
              url: local_ajax_establecimientos,
              data: {
                red_id: redId,
              },
              success: function (data) {
                $establecimientoSelect.html(
                  '<option value="">---------</option>',
                );
                $.each(data, function (index, item) {
                  $establecimientoSelect.append(
                    '<option value="' +
                      item.id +
                      '">' +
                      item.nombre_establecimiento +
                      "</option>",
                  );
                });
                if (initialEst) {
                  $establecimientoSelect.val(initialEst);
                }
                // Trigger change to cascade to estamentos
                $establecimientoSelect.trigger("change", [true]);
              },
            });
          } else {
            $establecimientoSelect.html('<option value="">---------</option>');
            $establecimientoSelect.trigger("change", [true]);
          }
        }

        function updateEstamentos(initialEstam) {
          var establecimientoId = $establecimientoSelect.val();
          if (establecimientoId) {
            $.ajax({
              url: local_ajax_estamentos,
              data: {
                establecimiento_id: establecimientoId,
              },
              success: function (data) {
                $estamentoSelect.html('<option value="">---------</option>');
                $.each(data, function (index, item) {
                  $estamentoSelect.append(
                    '<option value="' +
                      item.id +
                      '">' +
                      item.nombre_estamento +
                      "</option>",
                  );
                });
                if (initialEstam) {
                  $estamentoSelect.val(initialEstam);
                }
              },
            });
          } else {
            $estamentoSelect.html('<option value="">---------</option>');
          }
        }

        $redSelect.on("change", function (e, isCascading) {
          if (!isCascading) updateEstablecimientos();
        });

        $establecimientoSelect.on("change", function (e, isCascading) {
          if (!isCascading) updateEstamentos();
        });

        // Initialize lists on page load to handle editing existing records
        var currentEst = $establecimientoSelect.val();
        var currentEstam = $estamentoSelect.val();
        
        if ($redSelect.val()) {
            updateEstablecimientos(currentEst);
            setTimeout(function() {
                var newEst = $establecimientoSelect.val();
                if (newEst) {
                    updateEstamentos(currentEstam);
                }
            }, 300);
        } else {
            $establecimientoSelect.html('<option value="">---------</option>');
            $estamentoSelect.html('<option value="">---------</option>');
        }
      });
    })(django.jQuery);
  }
});
