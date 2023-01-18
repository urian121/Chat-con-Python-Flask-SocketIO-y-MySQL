
window.addEventListener('load', (event) => {
    let miBody = document.body;
       miBody.classList.remove('loader');

});

window.addEventListener('DOMContentLoaded', (event) => {
    document.querySelector('#mensaje').focus();
});

const localStorage = ()=>{
    //Para eliminar todas las variables guardadas en el localStorage
    localStorage.clear(); 

    //Pregunto Existe el idUser en mi LocalStorage?
    if("idUser" in localStorage){
     let idUser = localStorage.getItem('idUser'); //Consulto el idUser desde mi localStorage
     return idUser;
    }else{
     //Si no existe, lo almaceno en mi LocalStorage.
    localStorage.setItem('idUser', idUser); 
    let idUser = localStorage.getItem('idUser'); //Consulto el idUser almacenado en mi localStorage
      return idUser;
   }
  }