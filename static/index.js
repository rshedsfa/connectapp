
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



/* window.onload = function() {
    document.getElementById("editeBtn").checked = true;    
    editeMode()
}; */
/* 
function editeMode(){
    const editeMode_ON = document.getElementsByClassName("editeMode_ON");
    const botton_w = document.getElementsByClassName("botton_w");
    const botton_c = document.getElementsByClassName("botton_c");
    const nameAndClass = document.getElementsByClassName("nameAndClass");
    if(document.getElementById("editeBtn").checked){
        document.getElementById("swichBtn").disabled = true;

        for (let i = 0; i < editeMode_ON.length; i++) {
            editeMode_ON[i].style.display="block";
        }
        for (let i = 0; i < botton_w.length; i++) {
            botton_w[i].style.display="none";
        }
        for (let i = 0; i < botton_c.length; i++) {
            botton_c[i].style.display="none";
        }
        for (let i = 0; i < nameAndClass.length; i++) {
            nameAndClass[i].style.display="none";
        }
    }
    else{
        document.getElementById("swichBtn").disabled = false;

        for (let i = 0; i < editeMode_ON.length; i++) {
            editeMode_ON[i].style.display="none";
        }
        for (let i = 0; i < nameAndClass.length; i++) {
            nameAndClass[i].style.display="block";
        }
        convert_Btn()
    }
}

function editeModeOff(){
    const editeMode_ON = document.getElementsByClassName("editeMode_ON");
    document.getElementById("editeBtn").checked = false;    
    editeMode()
}


 */


