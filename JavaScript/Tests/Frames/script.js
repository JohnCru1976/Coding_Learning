let web = 1;
function changeWeb (){
    if (web == 1){
        web = 2;
        let frame = document.getElementById("web");
        frame.src = "web2.html"
    } else {
        web = 1;
        let frame = document.getElementById("web");
        frame.src = "web1.html"
    }
}