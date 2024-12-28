//Función para cerrar ventana luego de editar IP
function cerrarVentana(event) {
    event.preventDefault(); 
    const form = event.target;
    fetch(form.action, {
        method: form.method,
        body: new FormData(form)
    })
    .then(response => {
        if (response.ok) {
            if (window.opener) {
                window.opener.location.reload();
            }
            window.close();
        } else {
            console.error("Error al enviar el formulario");
        }
    })
    .catch(error => {
        console.error("Error al enviar el formulario:", error);
    });
}
// Abrir ventana para editar información 
function openCenteredWindow(url) {
    var width = 800; 
    var height = 600; 
    var left = (window.innerWidth - width) / 2; 
    var top = (window.innerHeight - height) / 2; 
    var windowFeatures = "width=" + width + ",height=" + height + ",left=" + left + ",top=" + top + "resizable=yes"; 
    window.open(url, "_blank", windowFeatures); } 

// Confirmación para eliminar registro    
 function confirmDeletion(id) { if (confirm("¿Estás seguro de que deseas eliminar esta IP?")) { window.location.href = "/eliminar_ip?id=" + id; } } 



