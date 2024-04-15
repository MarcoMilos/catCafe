**Nombres:**
*Pedro Luis Pérez Collado,*
*Franco Muñoz Ceballos,*
*Marco Miloslavich Airola,*
*Alejandro Miloslavich Airola*

**En login:**
1. **$(document).ready(function() {...});:** *Esta función de jQuery se ejecuta cuando el DOM está completamente cargado. Es un buen lugar para inicializar código que necesita acceder a elementos del DOM.*
2. **$('#loginForm').on('submit', function(e) {...});:** *Este código agrega un manejador de eventos al formulario con id "loginForm". Cuando se envía este formulario, se ejecuta la función proporcionada. La función toma un parámetro "e" que representa el evento de envío.*
3. **e.preventDefault();:** *Esto evita que el formulario se envíe de forma predeterminada, lo que significa que no se recargará la página cuando se envíe el formulario.*
4. **var username = $('input[name="uname"]').val();:** *Este código obtiene el valor del campo de entrada con el atributo "name" igual a "uname", que generalmente sería el campo de nombre de usuario.*
5. **var password = $('input[name="psw"]').val();:** *Similar al anterior, esto obtiene el valor del campo de entrada de contraseña.*
6. **$.ajax({ ... });:** *Este es el inicio de la solicitud AJAX utilizando jQuery. Aquí se especifican los detalles de la solicitud, como la URL a la que se enviará la solicitud, el método HTTP (POST en este caso), el tipo de contenido y los datos que se enviarán.*
7. **success: function(response) {...}:** *Este bloque de código maneja la respuesta exitosa de la solicitud AJAX. Si la respuesta contiene un error, se muestra una alerta con el mensaje de error. Si no hay errores, se redirige al usuario a diferentes páginas según su rol (admin o usuario regular).*
8. **error: function(xhr) {...}:** *Este bloque de código maneja los errores de la solicitud AJAX. En caso de un error, se muestra una alerta con el estado del error.*

**En el registro:**
1. **success: function(response) {...}:** *Este bloque de código maneja la respuesta exitosa de la solicitud AJAX. Si el registro es exitoso, muestra una alerta de éxito y redirige al usuario a la página de inicio de sesión. Si hay algún error en el registro, muestra una alerta con el mensaje de error proporcionado por el servidor.*
2. **error: function(xhr, status, error) {...}:** *Este bloque de código maneja los errores de la solicitud AJAX. En caso de un error, muestra una alerta con un mensaje genérico de error y registra detalles del error en la consola del navegador.*

**Descripción de los dos endpoints:**
1. **/login:** *Este endpoint maneja las solicitudes de inicio de sesión. Cuando se recibe una solicitud POST en este endpoint, se espera que los datos del formulario incluyan un campo 'username' y un campo 'password'. Luego, se utiliza la función checkUser(username, password) para verificar si el usuario existe en la base de datos y si la contraseña proporcionada coincide.*
   *Si se encuentra un usuario y la contraseña es correcta, se devuelve un objeto JSON con la información del usuario, incluido un indicador booleano que especifica si el usuario es un administrador o no. Si no se encuentra un usuario o la contraseña es incorrecta, se devuelve un objeto JSON con un mensaje de error.*
2. **/register:** *Este endpoint maneja las solicitudes de registro de nuevos usuarios. Cuando se recibe una solicitud POST en este endpoint, se espera que los datos del formulario incluyan un campo 'username' y un campo 'password'. Luego, se utiliza la función insertUser(username, password) para insertar un nuevo usuario en la base de datos con el nombre de usuario y la contraseña proporcionados.*
   *Si el usuario se inserta correctamente, se devuelve un objeto JSON con un indicador de éxito establecido en verdadero. Si hay algún problema al intentar insertar el usuario, se devuelve un objeto JSON con un mensaje de error.*

**Carga y Evento de Envío del Formulario:**
1. El código se ejecuta cuando el documento HTML ha sido completamente cargado (**'DOMContentLoaded'**).
2. Se selecciona el formulario con el ID 'submit_application' y se escucha el evento de envío (**'submit'**).
3. Cuando se intenta enviar el formulario, primero se previene el envío automático con **'event.preventDefault()'** para realizar validaciones.
4. Se itera sobre cada campo del formulario usando 'FormData' y se verifica si cada campo está lleno (sin contar espacios en blanco). Si un campo está vacío, se muestra un mensaje de error y se marca el formulario como inválido.
5. Si todos los campos están llenos y válidos, se muestra un mensaje de confirmación con **'alert'** y luego se envía el formulario al servidor. También se menciona la posibilidad de usar AJAX para un envío sin recargar la página.

**Validación en Tiempo Real:**
- Para cada campo del formulario (excepto botones de envío), se añade un evento **'input'** que valida el contenido del campo en tiempo real. Si el campo está vacío, se muestra un mensaje de error; si no, se limpia el mensaje de error.

**Navegación en el Formulario:**
1. Se maneja la navegación dentro del formulario mediante botones de "siguiente" y "atrás". El botón "siguiente" (**'nextBtn'**) activa una clase CSS (*secActive*) en el formulario si todos los campos de la sección actual están llenos. Esto puede ser usado para mostrar u ocultar secciones del formulario.
2. El botón "atrás" (**'backBtn'**) remueve la clase *'secActive'*, lo que podría usarse para regresar a una sección anterior del formulario.

**Evento de carga del DOM:**
- El código espera a que el DOM de la página esté completamente cargado antes de ejecutarse.

**Obtención de elementos del DOM:**
Se obtienen tres elementos del DOM utilizando sus identificadores:
- **cartSummary:** *Representa el elemento donde se mostrará un resumen del carrito de compras.*
- **finalizePurchase:** *Representa un botón (o algún otro elemento) que permite finalizar la compra.*
- **miauSound:** *Representa un elemento de audio que probablemente reproduzca un sonido de "miau".*
- **Obtención del carrito desde el almacenamiento local:** *Se obtiene el contenido del carrito de compras desde el almacenamiento local del navegador.*
  *Si no hay nada en el carrito, se inicializa como un array vacío.*

**Mostrar elementos del carrito:**
- Por cada elemento en el carrito, se crea un párrafo (<p>) que muestra el nombre del producto, su precio y la cantidad seleccionada. Este párrafo se agrega al elemento cartSummary.

**Evento de clic en "finalizar compra":**
Se añade un evento de clic al elemento finalizePurchase. Cuando se hace clic en este elemento:
- *Se reproduce un sonido de "miau" utilizando el elemento miauSound.* 
- *Se muestra una alerta con el mensaje "Gracias por tu compra!".*
- *Opcionalmente, se limpia el carrito de compras almacenado en el navegador utilizando localStorage.clear().*

**Inicialización de Elementos y Listeners:**
- *Selecciona y asigna varios elementos del DOM a variables para facilitar su manipulación, como el icono del carrito, botones, y áreas de contenido donde se mostrarán los productos y el carrito.*
- *Se añaden eventListeners para gestionar la apertura y cierre del carrito de compras mediante cambios de clase CSS que afectan la visualización del carrito.*

**Gestión de Productos y Carrito:**
- **addDataToHTML():** *Rellena la lista de productos en la interfaz de usuario. Crea elementos HTML para cada producto y los agrega al DOM.*
- **addToCart():** *Añade un producto al carrito o incrementa la cantidad si ya está en el carrito, luego actualiza la visualización y el almacenamiento local.*
- **addCartToMemory():** *Guarda el estado actual del carrito en el almacenamiento local del navegador para persistencia.*
- **addCartToHTML():** *Actualiza la visualización del carrito en la interfaz de usuario, incluyendo la cantidad total de items en el icono del carrito.*

**Modificación de Cantidades en el Carrito:**
- *Escuchadores de eventos en la lista del carrito permiten incrementar o decrementar la cantidad de un producto cuando se interactúa con los botones más (+) y menos (-).*
- *changeQuantity(): Modifica la cantidad de un producto en el carrito y actualiza la interfaz y el almacenamiento local según el tipo de acción (plus o minus).*

**Inicialización de la Aplicación:**
- *initApp(): Carga productos de un archivo JSON y los muestra. También recupera el estado del carrito del almacenamiento local si existe y lo muestra.*

**Navegación entre Pestañas:**
- *openMenu(): Oculta todas las pestañas y muestra solo la seleccionada. Cambia la clase CSS del enlace activo para reflejar el estado activo visualmente.*

**Eventos Adicionales:**
- *El evento click automático en "myLink" probablemente para activar alguna acción inmediatamente después de cargar la página o script.*
- *Un evento onclick en "btRegreso" para navegar de regreso a una página específica, presumiblemente la página principal del usuario de productos.*
