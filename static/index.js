// from regular call to whatsapp call
function convert_Btn(){
    const botton_w = document.getElementsByClassName("botton_w");
    const botton_c = document.getElementsByClassName("botton_c");

    if(document.getElementById("swichBtn").checked){
        for (let i = 0; i < botton_w.length; i++) {
            botton_w[i].style.display="none";
        }
        for (let i = 0; i < botton_c.length; i++) {
            botton_c[i].style.display="block";
        }
    }
    
    else{
        for (let i = 0; i < botton_w.length; i++) {
            botton_w[i].style.display="block";
        }
        for (let i = 0; i < botton_c.length; i++) {
            botton_c[i].style.display="none";
        }
    }
}



//responsive navbar
function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
      x.className += " responsive";
    } else {
      x.className = "topnav";
    }
  }